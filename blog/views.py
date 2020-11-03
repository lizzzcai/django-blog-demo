from django.shortcuts import render


def index(request):
    return render(request, 'blog/index.html', context={
        'title': 'My Blog Page',
        'welcome': 'Welcome to my blog!'
    })
