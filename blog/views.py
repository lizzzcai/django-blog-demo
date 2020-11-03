from django.shortcuts import render
from .models import Post


def index(request):
    post_list = Post.objects.all().order_by('-created_time') # add - means order reversely
    return render(request, 'blog/index.html', context={
        'title': 'My Blog Page',
        'welcome': 'Welcome to my blog!',
        'post_list': post_list
    })
