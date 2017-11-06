from __future__ import unicode_literals

from django.shortcuts import render

from .models import Post

def some_function(request):
	dictionary = {
		"key": "with a value",
	}
	return render(request, "post.html", dictionary)

def post_list(request):
	objects = Post.objects.all()
	context = {
		"post_items": objects,
	}
	return render(request, "list.html", context)

def post_detail(request, post_id):
	item = Post.objects.get(id=3)
	context = {
		"item": item,
	}
	return render(request, "detail.html", context)