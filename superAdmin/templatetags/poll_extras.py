from django import template

register = template.Library()


@register.filter
def duration(td):
    try:
        data = str(td).split('.')[0]
    except:
        data = td
    return data
