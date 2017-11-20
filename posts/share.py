from django import templates
from urllib.parse import quote

register = 

@register.filter
def share(value):
	return quote(value)