from django.shortcuts import render, get_object_or_404, redirect
from .models import UserMeta, Category, Post
from django.shortcuts import render_to_response
from django.template import RequestContext
from juntan.settings import local

def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response

# Create your views here.
def homepage(request):
    ctx = {
        "current_user": UserMeta.objects.get(id=1),
        "items": Post.objects.all().order_by('-date', 'title'),
        "local": local
    }
    return render(request, 'index.html', context=ctx)

def about(request):
    user = UserMeta.objects.get(id=1)
    ctx = {
        "current_user": user,
        "local": local
    }
    return render(request, 'about.html', context=ctx)

def archive(request):
    ctx = {
        "count": len(Post.objects.all()),
        "code": Post.objects.filter(category__name="Code").all().order_by('-date', 'title'),
        "design": Post.objects.filter(category__name="Design").all().order_by('-date', 'title'),
        "photo": Post.objects.filter(category__name="Photo").all().order_by('-date', 'title'),
        "local": local,
    }

    return render(request, 'archive.html', context=ctx)

def post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)

    if post.external_link:
        return redirect(post.external_link)

    context = {
        "post": post,
        "local": local
    }

    return render(request, 'post.html', context)
