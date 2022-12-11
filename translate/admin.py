from cProfile import label
from contextlib import nullcontext
from multiprocessing.spawn import old_main_modules
from unicodedata import name
from django.contrib import admin
from .models import Translate
from .util import translate
from django import forms
import ast
from ws_bckend.settings import LANGUAGES
from copy import copy


class TranslateAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, change=False, **kwargs):
        return TranslateForm
    list_display = ['article']

class TranslateForm(forms.ModelForm):
    class Meta:
        model = Translate
        exclude = []

    def __init__(self, *args, instance=None, **kwargs):
        # The following dynamically add three fields to the model form
        if instance:
                
            self.base_fields["article"] = forms.CharField(label="article", initial=instance.article, max_length=1041)
            for lang in LANGUAGES:
                label = f"Article Title ({lang[0]})"
                self.base_fields[label] = forms.CharField(label=label, initial=instance.article.get(lang[0], '') ,max_length=256)
                
                
        else:
            self.base_fields["article"] = forms.CharField(label="article", initial=None, max_length=1041)
            for lang in LANGUAGES:  
                label = f"Article Title ({lang[0]})"
                self.base_fields[label] = forms.CharField(label=label, required=False ,max_length=256)
                    
        super().__init__(*args, instance=None, **kwargs)


    def save(self, commit=True):
        
        articleStr = self.cleaned_data.get("article", '')
        
        if isinstance(articleStr , str):
            self.instance.article = ast.literal_eval(articleStr)
        else:
            self.instance.article = articleStr    
            
        oldArticle = copy(self.instance.article)
        
        for key, name in LANGUAGES:
            label = f"Article Title ({key})"
            if self.cleaned_data.get(label):
                self.instance.article[key] = self.cleaned_data.get(label)
            # else:
            #     del self.instance.article[key]

        call = super(TranslateForm, self).save(commit=False)
        
        Translate.objects.filter(article=oldArticle).delete()
        
        return call

    
admin.site.register(Translate, TranslateAdmin)
# admin.site.register(Translate)