from django.shortcuts import render

from .models import (
    Blog,
)


def home(request):
    blogs = Blog.objects.order_by('-created_date')
    context = {
        "blogs": blogs
    }
    return render(request, 'home.html', context)


def blogs(request):
    return render(request, 'blogs.html')
