# blog/templatetags/custom_filters.py
from django import template
from django.utils.html import strip_tags
from django.utils.safestring import mark_safe
import re

register = template.Library()

@register.filter
def truncatehtml(text, num_words):
    """
    Truncate HTML content to a certain number of words, keeping tags intact.
    """
    if not text:
        return ''
    
    words = strip_tags(text).split()
    if len(words) > num_words:
        words = words[:num_words]
        truncated_text = ' '.join(words) + '...'
    else:
        truncated_text = text

    return mark_safe(truncated_text)
