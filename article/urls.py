"""article URL Configuration
"""
from django.conf.urls import url
from django.urls import path
from django.views.generic.base import TemplateView
from article import views

urlpatterns = [
    # url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'add/', views.article_add, name='article_add'),    
    #url(r'vote/(?P<article_id>[0-9])/', views.article_vote, name='article_vote'),    
    path(r'vote/<int:article_id>/', views.article_vote, name='article_vote'),    
    url(r'', views.index, name='index'),    
]
