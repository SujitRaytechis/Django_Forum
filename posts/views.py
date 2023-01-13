from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from .models import Post

from .forms import PostForm
# Create your views here.


def index(request):
    # if the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST)
       # if the form is valid
        if form.is_valid():
            # Yes , Save
            form.save()
        # Redirect to Home Page
            return HttpResponseRedirect('/')

        else:
            # No , Show Error
            return HttpResponseRedirect(form.erros.as_json())

     # Get all posts , limit = 20

    posts = Post.objects.all()[:20]

    # show

    return render(request, 'posts.html',
                  {'posts': posts})


def Delete(request, post_id):
    post=Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')
    # output = 'POST ID is ' + str(post_id)
    # return HttpResponse(output)
