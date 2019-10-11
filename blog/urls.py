from django.urls import path 
from . import views      # . for parent directory!
urlpatterns  = [
	path('',views.post_list,name='post_list'),
]

