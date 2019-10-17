from django import forms
from .models import Post

class PostForm (forms.ModelForm):

	class Meta:                # meta class defines how a class behaves (general definition)
								# here we are using meta to tell which django model to use to create form
		model = Post
		fields=('title','text')   # here we tell which fields should be displayed in our form !