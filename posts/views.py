from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .models import Post

from .forms import PostForm

from django.contrib import messages

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

def post_create(request):
	form = PostForm(request.POST or None) # as model

	if form.is_valid():
		form.save()
		messages.success(request, "Congrats!")
		return redirect("list")
	context = {
		"form": form
	}
	return render(request, 'post_create.html', context)
def post_update(request, post_id):
	item = Post.objects.get(id=post_id) # getting specific object

	form = PostForm(request.POST or None, instance=item) # this form request.post to send it to server

	if form.is_valid():
		form.save()
		messages.info(request, "Done!")
		return redirect("list") #transfer me to list page
	context = {
		"form": form,
		"item": item,
	}
	return render(request, 'post_update.html', context)

def post_delete(request, post_id):
	Post.objects.get(id=post_id).delete()
	messages.warning(request, "good for you!")
	return redirect("list")
