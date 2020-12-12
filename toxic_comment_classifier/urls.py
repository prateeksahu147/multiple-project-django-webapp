from django.urls import path, include

from . import views

urlpatterns= [
    path('', views.classifier, name='classifier'),
    path('predict/', views.predict, name=  'predict_page'), 
]
