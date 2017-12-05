from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Post, Like
from .forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import Http404
from django.utils import timezone 
from django.db.models import Q
from django.http import JsonResponse
from .forms import UserSignup, UserLogin
from django.contrib.auth import authenticate, login, logout



def ajax_like(request, post_slug):
	post_object = Post.objects.get(slug=post_slug)
	new_like, created = Like.objects.get_or_create(user=request.user, post=post_object)

	if created:
		action="like"
	else:
		new_like.delete()
		action="unlike"

	post_like_count = post_object.like_set.all().count()
	response = {
		"action": action,
		"post_like_count": post_like_count,
	}
	return JsonResponse(response, safe=False)


def some_function(request):
	dictionary = {
		"key": "with a value",
	}
	return render(request, "post.html", dictionary)

def post_list(request):
	today = timezone.now().date()
	objects = Post.objects.filter(draft=False).filter(publish__lte=today)
	if request.user.is_staff or request.user.is_superuser:
		objects = Post.objects.all()

	query = request.GET.get("q")
	if query:
		objects = objects.filter(
			Q(title__icontains=query)|
            Q(content__icontains=query)|
            Q(author__first_name__icontains=query)|
            Q(author__last_name__icontains=query)
            ).distinct()


	paginator = Paginator(objects, 4)
	number = request.GET.get('page')

	try:
		objects = paginator.page(number)
	except PageNotAnInteger: 
		objects = paginator.page(1)
	except EmptyPage:
		objects = paginator.page(paginator.num_pages)

	context = {
		"post_items": objects,
		"title": "List",
		"user": request.user,
		"today": today
	}
	return render(request, "list.html", context)

def post_detail(request, post_slug):
	item = get_object_or_404(Post, slug=post_slug)
	if item.publish>timezone.now().date() or item .draft:
		if not (request.user.is_staff or request.user.is_superuser):
			raise Http404
	if request.user.is_authenticated():
		if Like.objects.filter(post=item, user=request.user).exists():
			Liked = True
		else:
			Liked = False
	post_like_count = item.like_set.all().count()
	context = {
		"title": "Detail",
		"item": item,
		"share_string": (item.content),
		"post_like_count": post_like_count,
		"Liked": Liked,
	}
	return render(request, "detail.html", context)

def post_create(request):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404
	form = PostForm(request.POST or None, request.FILES or None) # as model

	if form.is_valid():
		post = form.save(commit = False)
		post.author = request.user
		post.save() 
		messages.success(request, "Congrats!")
		return redirect("list")
	context = {
		'title': 'Create',
		"form": form,
	}
	return render(request, 'post_create.html', context)
def post_update(request, post_slug):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404
	item = get_object_or_404(Post, slug=post_slug) # getting specific object
	form = PostForm(request.POST or None, request.FILES or None, instance=item) # this form request.post to send it to server

	if form.is_valid():
		form.save()
		messages.info(request, "Done!")
		return redirect("list") #transfer me to list page
	context = {
		"form": form,
		"item": item,
		"title": "Update",
	}
	return render(request, 'post_update.html', context)

def post_delete(request, post_slug):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404
	item = get_object_or_404(Post, slug=post_slug)
	item.delete()
	messages.warning(request, "good for you!")
	return redirect("list")


def usersignup(request):
	form = UserSignup()
	context = {
		'form': form
	}
	if request.method == 'POST':
		form = UserSignup(request.POST)
		if form.is_valid():
			user = form.save()
			username = user.username
			password = user.password

			user.set_password(password)
			user.save()

			auth_user = authenticate(username=username, password=password)
			login(request, auth_user)

			return redirect("list")
		messages.error(request, form.errors)
		return redirect("signup")
	return render(request, 'signup.html', context)

def userlogin(request):
	form = UserLogin()
	context = {
		'form': form
	}
	if request.method == 'POST':
		form = UserLogin(request.POST)
		if form.is_valid():

			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			auth_user = authenticate(username=username, password=password)
			if auth_user is not None:
				login(request, auth_user)
				return redirect("list")

			messages.error(request, "Wrong username/password combination. Please try again.")
			return redirect('login')
		messages.error(request, form.errors)
		return redirect('login')
	return render(request, 'login.html', context)

def userlogout(request):
	logout(request)
	return redirect('list')

