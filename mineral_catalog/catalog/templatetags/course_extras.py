from django import template

register = template.Library()


@register.filter('title_case')
def title_case(string):
    '''Title cases a given string'''
    return string.title()


@register.filter('strip_underline')
def strip_underline(string):
    '''Strips _ from given string'''
    return string.replace("_", " ")
