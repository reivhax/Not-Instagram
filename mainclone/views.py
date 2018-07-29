from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='/accounts/login/')
def home(request):
    image_form = PostForm()
    images = Post.objects.all()
    commentform = CommentForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            request.user.profile.post(form)
    return render(request, 'landing.html', locals())


@login_required(login_url='/accounts/login/')
def mine(request):
    images = request.user.profile.posts.all()
    user_object = request.user
    user_images = user_object.profile.posts.all()
    user_saved = [save.photo for save in user_object.profile.saves.all()]
    user_liked = [like.photo for like in user_object.profile.mylikes.all()]
    print(user_liked)
    return render(request, 'myprofile.html', locals())\@login_required(login_url='/accounts/login/')
@login_required(login_url='/accounts/login/')
def save(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    request.user.profile.save(post)
    return JsonResponse({}, safe=False)


@login_required(login_url='/accounts/login/')
def unlike(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    request.user.profile.unlike(post)
    return JsonResponse(post.count_likes, safe=False)
@login_required(login_url='/accounts/login/')
def find(request, name):
    results = Profile.find_profile(name)
    return render(request, 'searchresults.html', locals())