
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.root, name= 'root' ), 
    path('comment_classifier/', include('toxic_comment_classifier.urls')),
    path('admin/', admin.site.urls),
]
