from django.shortcuts import get_object_or_404, render

from .models import Blog

# Create your views here.


def list_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/list.html', {'blogs': blogs})


def detail_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog/detail.html', {'blog': blog})
