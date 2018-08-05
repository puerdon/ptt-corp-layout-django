from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('segmentation', views.segmentation, name='segmentation'),
    path('collocation', views.collocation, name='collocation'),
    path('concordance', views.concordance, name='concordance'),
    path('sentipol', views.sentipol, name='sentipol'),
    path('wordcloud', views.wordcloud, name='wordcloud'),
    path('apidoc', views.apidoc, name='apidoc')
] 