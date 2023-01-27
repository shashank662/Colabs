import imp
from urllib import request
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views import View

from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post, Comment,Contact
from .forms import PostForm, CommentForm,ContactForm
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView, RedirectView)

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class AboutView(TemplateView):
    template_name = 'blog/about.html'

    
class IndexView(TemplateView):
    template_name="blog/index.html"
    def get(self,request):
        # student=Post.objects.all()
        last_ten = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:6]
        return render(request,'blog/index.html',{"student":last_ten})
    
class RedirectToHome(RedirectView):
    pattern_name='index'
    
    
class PostListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    model = Post
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(LoginRequiredMixin,DetailView):
    login_url = '/login/'
    model = Post
    # context_object_name=post
    
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['current_user']=Post.objects.get(author=User.username)
    #     return context
    
    # def get_queryset(self):
    #     return User.objects.get(author=User.username)


class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm
    
    model = Post
    def post(self,request):
        form = PostForm(request.POST or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            print("Hello")
            post.save()
            
        return  HttpResponseRedirect(reverse('post_detail',kwargs={'pk':post.pk}))
        
    def get(self,request):
        form=PostForm()
        return render(request,'blog/post_form.html',{"form":form})
        

        
            
   
   
   #post form using form api


class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    #using default template name
    form_class = PostForm

    model = Post


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    template_name = 'blog/post_draft_list.html'
    context_object_name='draft'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('-created_date')
    
    
    
    

def contact_view(request):
   
    if request.method == 'POST':
        Contact_form = ContactForm(request.POST)
        if Contact_form.is_valid():
            Contact_form.save()
            return render(request, 'blog/success.html')
    
    Contact_form = ContactForm()
    context = {'form': Contact_form}
    return render(request, 'blog/blog_contact.html', context)

#######################################
## Functions that require a pk match ##
#######################################

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # post =Post.objects.get(pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
        form1=Post.objects.get(pk=pk);
        return render(request, 'blog/comment_form.html', {'form': form,'form1':form1})

# pk passed from url
# @login_required
# def comment_approve(request, pk):
#     #get request of the instance of the model
#     comment = get_object_or_404(Comment, pk=pk)
#     comment.approve()
#     return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    # comment = Comment.objects.get(pk=pk)
    post_pk = comment.post.pk
    # we are using comment 
    comment.delete()
    return redirect('post_detail', pk=post_pk)

