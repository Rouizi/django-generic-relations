from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from .models import Post, Comment, Profile
from .forms import CommentForm


def post_comment(request, instance, context):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data['author']
            content = form.cleaned_data['content']

            Comment.objects.create(content_object=instance, author=author, content=content)
            # or we can add a new comment like this:
            # instance.comments.create(author=author, content=content)
    else:
        form = CommentForm()    
    context['form'] = form


def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    # get all the comments for the current post
    comments = post.comments.all()

    context = {
        'post': post,
        'comments': comments,
    }
    post_comment(request, post, context)
    return render(request, 'post.html', context)


def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    # get all the comments for the current user profile
    comments = profile.comments.all()
    
    context = {
        'user': user,
        'profile': profile,
        'comments': comments,
    }
    post_comment(request, profile, context)
    return render(request, 'profile.html', context)