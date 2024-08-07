from django.views.generic.base import TemplateView


class About(TemplateView):
    """О проекте."""
    template_name = 'pages/about.html'


class Rules(TemplateView):
    """Наши Правила."""
    template_name = 'pages/rules.html'
