from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommentForm, PostForm
from .models import Comment, Post 


post_list = ListView.as_view(model=Post)

post_detail = DetailView.as_view(model=Post)

def post_new(request):
    form_cls = PostForm
    template_name = 'myapp/post_form.html'
    success_url = '/'

    if request.method == 'POST': 
        form = form_cls(request.POST, request.FILES)
        if form.is_valid():
            # post = Post.objects.create(**form.cleaned_data)
            post = form.save()
            return redirect(success_url)
    else:
        form = form_cls() 
        
    return render(request, template_name, {
        'form':form,
    })

def post_edit(request, pk):
    form_cls = PostForm
    template_name = 'myapp/post_form.html'
    success_url = '/'

    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST': 
        form = form_cls(request.POST, request.FILES, instance=post)
        if form.is_valid():
            # post = Post.objects.create(**form.cleaned_data)
            post = form.save()
            return redirect(success_url)
    else:
        form = form_cls(instance=post) 
        
    return render(request, template_name, {
        'form':form,
    })

