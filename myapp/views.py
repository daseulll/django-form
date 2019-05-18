from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .forms import CommentForm, PostForm
from .models import Comment, Post 


post_list = ListView.as_view(model=Post)

post_detail = DetailView.as_view(model=Post)

# def post_new(request):
#     form_cls = PostForm
#     template_name = 'myapp/post_form.html'
#     success_url = '/'

#     if request.method == 'POST': 
#         form = form_cls(request.POST, request.FILES)
#         if form.is_valid():
#             # post = Post.objects.create(**form.cleaned_data)
#             post = form.save()
#             messages.success(request, '새 글을 저장했습니다.')
#             return redirect(success_url)
#     else:
#         form = form_cls() 
        
#     return render(request, template_name, {
#         'form': form,
#     })

class PostCreateView(CreateView):
    model = Post
    # form_class = PostForm
    # template_name = 'myapp/post_form.html'
    # success_url = "https://otherservice.com/hello/{id}/"
    fields = '__all__'
    
    def form_valid(self, form):
        res = super().form_valid(form)
        messages.success(self.request, '새 글을 저장했습니다.')
        return res

post_new = PostCreateView.as_view()


# def post_edit(request, pk):
#     form_cls = PostForm
#     template_name = 'myapp/post_form.html'
#     success_url = '/'

#     post = get_object_or_404(Post, pk=pk)

#     if request.method == 'POST': 
#         form = form_cls(request.POST, request.FILES, instance=post)
#         if form.is_valid():
#             # post = Post.objects.create(**form.cleaned_data)
#             post = form.save()
#             messages.success(request, '수정이 완료되었습니다')
#             return redirect(success_url)
#     else:
#         form = form_cls(instance=post) 
        
#     return render(request, template_name, {
#         'form':form,
#     })

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        res = super().form_valid(form)
        messages.success(self.request, '새 글을 저장했습니다.')
        return res
        
post_edit = PostUpdateView.as_view()

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'myapp/post_confirm_delete.html', {
        'post' : post,
    })

# post_delete = DeleteView.as_view(model=Post, success_url=reverse_lazy('post_list') )


def comment_new(request, post_pk):
    form_cls = CommentForm
    template_name = 'myapp/comment_form.html'
    success_url = '/'
    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'POST': 
        form = form_cls(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.ip = request.META['REMOTE_ADDR']
            comment.save()
            messages.success(request, '댓글이 등록되었습니다')
            return redirect(success_url)
    else:
        form = form_cls() 
        
    return render(request, template_name, {
        'form':form,
    })

def comment_edit(request, post_pk, pk):
    form_cls = CommentForm
    template_name = 'myapp/comment_form.html'
    success_url = '/'
    comment = get_object_or_404(Comment, pk=pk)

    if request.method == 'POST': 
        form = form_cls(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            comment = form.save()
            messages.success(request, '댓글이 수정되었습니다')
            return redirect(success_url)
    else:
        form = form_cls(instance=comment) 
        
    return render(request, template_name, {
        'form':form,
    })


from rest_framework.generics import ListCreateAPIView
from .serializers import PostSerializer

class PostListCreateAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

post_list_create = PostListCreateAPIView.as_view()