from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

from markdown import markdown

register = template.Library()


@register.filter
@stringfilter
def unsafe_markdown_to_html(value: str) -> str:
    """
    Accepts raw markdown and turns it to html

    Make sure the input to this filter is trusted e.g. flatpage content created by
    an admin, and not, say, a user bio.
    """
    return mark_safe(markdown(value))
