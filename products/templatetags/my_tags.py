from django import template

register = template.Library()

@register.simple_tag(name="get_rating_range")
def get_rating_range(value):
    rating_len = []
    for i in range(value):
        rating_len.append(i)

    return rating_len


@register.simple_tag(name="python")
def python(value):
    return "python lang"