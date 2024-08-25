from django.http import Http404
from django.shortcuts import render
from .posts_list import POSTS

POSTS_DATA = {post['id']: post for post in POSTS}


def index(request):
    """Лента записей."""
    template = 'blog/index.html'
    context = {'posts': POSTS[::-1],
               'title': 'Лента записей'}
    return render(request, template, context)


def post_detail(request, id):
    """Список постов с детальным описанием."""
    template = 'blog/detail.html'
    try:
        context = {'post': POSTS_DATA[id]}
    except KeyError:
        raise Http404(f'Страницы {id} не существует')
    return render(request, template, context)


def category_posts(request, category_slug):
    """Список постов по категории."""
    template = 'blog/category.html'
    context = {'category': category_slug}
    return render(request, template, context)
