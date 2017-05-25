from django.conf.urls import url

from . import views

# list routes URLs to views
urlpatterns = [
    url(r'^decks/$', views.deckList, name = 'deckList'),
    url(r'^decks/([\d]+)/', views.viewCard, name='viewCard'),
    url(r'^new/$', views.addCard, name ='addCard'),
    url(r'^edit/([\d]+)/$', views.editCard, name ='editCard'),
     url(r'^delete/([\d]+)/$', views.deleteCard, name ='deleteCard'),
]