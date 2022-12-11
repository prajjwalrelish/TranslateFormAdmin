from gettext import gettext
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate

def translate(language, text):
    cur_language = get_language()
    
    try:
        activate(language)
        text = _(text)
    finally:
        activate(cur_language)
    return text

