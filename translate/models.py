from django.db import models
from mixins import UUIDMixin
from django.forms import ModelForm
from django import forms
# Create your models here.

class Translate(UUIDMixin):
    article = models.JSONField(default=dict)
    