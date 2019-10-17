from django.urls import path 
from . import views      # . for parent directory!
urlpatterns  = [
	path('',views.post_list,name='post_list'),
	 path('post/<int:pk>/', views.post_detail, name='post_detail'),	  # here int: pk is that we receive an integer that is primary key number of the given post
	 path('post/new/', views.post_new, name='post_new'),        # here we are defining url /now/ for our new post form
	 path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]

