from django.shortcuts import render
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.
from django.shortcuts import render,get_object_or_404

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render (request,'blog/post_list.html',{'posts': posts})        # note this posts returns all the filtered posts in List forn!
	# here we didn't need to specify exactly the template folder bcz django automatically searches for the folder
	
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)          # i guess this get_object_or_404 is django's built in method!
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
	if request.method =="POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date=timezone.now()
			post.save()
			return redirect('post_detail',pk=post.pk)   # takes us the detailed window for this post!
	else:
		form = PostForm()
	return render (request,'blog/post_edit.html',{'form':form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})