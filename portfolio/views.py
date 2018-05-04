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
    context = {
        "current_user": UserMeta.objects.get(id=1),
        "items": Post.objects.all().order_by('-date', 'title')[:12],
        "local": local
    }
    return render(request, 'index.html', context=context)

def about(request):
    user = UserMeta.objects.get(id=1)
    context = {
        "current_user": user,
        "local": local
    }
    return render(request, 'about.html', context=context)

def archive(request):
    context = {
        "count": len(Post.objects.all()),
        "code": Post.objects.filter(category__name="Code").order_by('-date', 'title'),
        "design": Post.objects.filter(category__name="Design").order_by('-date', 'title'),
        "photo": Post.objects.filter(category__name="Photo").order_by('-date', 'title'),
        "local": local,
    }

    return render(request, 'archive.html', context=context)

def landing(request, category):
    if not category or category != 'photo':
        return redirect("/")

    requested_category = Post.objects.filter(category__name="Photo").order_by('-date', 'title') # fixme: bad db design with capitalized letters

    context = {
        'category': requested_category,
        'local': local
    }

    return render(request, 'landing/' + category + '.html', context=context)

def post(request, post_slug):
    if not post_slug:
        return redirect("/archive")
    requested_post = get_object_or_404(Post, slug=post_slug)

    if requested_post.external_link:
        # push out to link
        return redirect(requested_post.external_link)

    related_posts = Post.objects.filter(category__name=requested_post.category.name).exclude(slug=post_slug).order_by('-date', 'title')[:3]

    context = {
        "post": requested_post,
        "related_posts": related_posts,
        "local": local
    }

    return render(request, 'post.html', context)
