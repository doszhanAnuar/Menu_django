from django import template
from django.urls import reverse

from main.models import Menu

register = template.Library()

@register.simple_tag(takes_context=True)
def show_menu(context, menu_name):
    # Получаем текущий URL
    current_url = context.request.path

    # Получаем все пункты меню с заданным именем
    menu_items = Menu.objects.filter(menu_name=menu_name)

    # Строим древовидное меню
    menu_html = build_menu(menu_items, current_url)

    return menu_html

def build_menu(items, current_url):
    menu_html = '<ul>'

    for item in items:
        menu_html += '<li class="active">' if current_url == item.url else '<li>'
        menu_html += '<a href="%s">%s</a>' % (reverse(item.url) if item.url.startswith('/') else item.url, item.title)

        if item.children.count():
            menu_html += build_menu(item.children.all(), current_url)

        menu_html += '</li>'

    menu_html += '</ul>'

    return menu_html
