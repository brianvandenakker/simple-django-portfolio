from django.urls import path, include
from . import views

app_name = 'projects'

urlpatterns = [
#BLOG URLS
    path('', views.PostListView.as_view(), name='post_list'),
    
]
