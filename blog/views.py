from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render (request,'blog/post_list.html',{'posts': posts})        # note this posts returns all the filtered posts in List forn!
	
	
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)          # i guess this get_object_or_404 is django's built in method!
    return render(request, 'blog/post_detail.html', {'post': post})