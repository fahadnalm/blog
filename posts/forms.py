from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post # bring me post model
		fields = ['title', 'content', 'img', 'draft', 'publish']

		widgets={
        'publish': forms.DateInput(attrs={"type":"date"}),
        }
