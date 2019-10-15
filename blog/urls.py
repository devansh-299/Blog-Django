from django.urls import path 
from . import views      # . for parent directory!
urlpatterns  = [
	path('',views.post_list,name='post_list'),
	 path('post/<int:pk>/', views.post_detail, name='post_detail'),	  # I guess here int: pk is that we receive an integer that is primary key number of the given post
]

