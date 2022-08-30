from django import template
from web_site.models import Category

register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.simple_tag()
def get_sorted():
    sorters = [
        {
            'title': 'По цене',
            'sorters': (
                ('price', 'По возрастанию'),
                ('-price', 'По убыванию')
            )
        },
        {
            'title': 'По названию',
            'sorters': (
                ('title', 'От А до Я'),
                ('-title', 'От Я до А')
            )
        },
        {
            'title': 'По дате добавления',
            'sorters': (
                ('created_at', 'Давно добавленные'),
                ('-created_at', 'Недавно добавленные')
            )
        }
    ]
    return sorters
