from django.shortcuts import render, get_object_or_404

from .models import Blog

# Create your views here.
def blog_home(request):
    blogs = Blog.objects
    return render(request, "blogs/blog.html", {"blogs":blogs})

def detail(request, blog_id):
    blogDetail = get_object_or_404(Blog, pk=blog_id)

    return render(request, "blogs/detail.html", {"blog":blogDetail})
