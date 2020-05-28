from django.urls import path, include
from . import views

app_name = 'about'

urlpatterns = [
#BLOG URLS
    path('', views.AboutListView.as_view(), name='about_detail'),
    path('update/', views.CreateAboutView.as_view(), name='update_about')
]
