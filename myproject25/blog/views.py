from django.views.generic import ListView , DeleteView , DetailView , UpdateView , CreateView
from django.urls import reverse_lazy
from .models import Post

#LIST_VIEW
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

#DETAIL_VIEW
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

#CREATE_VIEW
class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title','content']

#UPDATE_VIEW
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title','content']

#DELETE_VIEW
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')