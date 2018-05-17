from django.shortcuts import render, get_object_or_404, redirect
from .models import UserMeta, Category, Post
from django.shortcuts import render_to_response
from django.template import RequestContext
from juntan.settings import local

def handler404(request):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {}, context_instance=RequestContext(request))
    response.status_code = 500
    return response

# Create your views here.
def homepage(request):
    ctx = {
        "current_user": UserMeta.objects.get(id=1),
        # 5/13 added blog category
        "digital": Post.objects.filter(category__name__in=["Code", "Design"]).order_by('-date', 'title')[:6],
        "analog": Post.objects.filter(category__name__in=["Photo", "Writing"]).order_by('-date', 'title')[:6],
        "local": local,
    }
    return render(request, 'index.html', context=ctx)

def archive(request):
    ctx = {
        "count": len(Post.objects.all()),
        "digital": Post.objects.filter(category__name__in=["Code", "Design"]).order_by('-date', 'title'),
        "analog": Post.objects.filter(category__name__in=["Photo", "Writing"]).order_by('-date', 'title'),
        "local": local,
    }

    return render(request, 'archive.html', context=ctx)

def post(request, post_slug):
    if not post_slug:
        return redirect("/archive")
    requested_post = get_object_or_404(Post, slug=post_slug)

    if requested_post.external_link:
        # push out to link
        return redirect(requested_post.external_link)

    related_posts = Post.objects.filter(category__name=requested_post.category.name).exclude(slug=post_slug).order_by('-date', 'title')[:3]

    context = {
        "current_user": UserMeta.objects.get(id=1),
        "post": requested_post,
        "related_posts": related_posts,
        "local": local
    }

    return render(request, 'post.html', context)
