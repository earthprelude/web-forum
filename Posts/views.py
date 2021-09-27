from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Post, Comment 
from .forms import PostForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(ListView):
  model = Post
  template_name='index.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      num_visits = self.request.session.get('num_visits', 0)
      self.request.session['num_visits'] = num_visits + 1
      context['num_visits'] = num_visits
      return context
  
class PostPageView(DetailView):
  model = Post
  template_name = 'post_page.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      post = context['post']
      comments = post.comments.all()
      context['comments'] = comments
      return context

class CommentCreateView(LoginRequiredMixin, CreateView):
  model = Comment
  form_class = CommentForm
  template_name = "create_comment.html"

  def form_valid(self, form):
      form = form.save(commit=False)
      form.user_id = self.request.user
      form.post_id = self.kwargs['pk']
      form.save()
      return super().form_valid(form)
  def get_form_kwargs(self, *args, **kwargs):
      kwargs = super(CommentCreateView, self).get_form_kwargs(*args, **kwargs)
      kwargs['user_id'] = self.request.user
      return kwargs
  def get_success_url(self): 
      return reverse('post', args=[str(self.kwargs['pk'])])

class PostCreateView(LoginRequiredMixin, CreateView):
  model = Post
  form_class = PostForm
  template_name = 'new_post.html'

  def form_valid(self, form):
      form = form.save(commit=False)
      form.user_id = self.request.user
      form.save()
      return super().form_valid(form)
  def get_form_kwargs(self, *args, **kwargs):
      kwargs = super(PostCreateView, self).get_form_kwargs(*args, **kwargs)
      kwargs['user_id'] = self.request.user
      return kwargs
  def get_success_url(self): 
      return reverse('home')


class PostUpdateView(LoginRequiredMixin, UpdateView):
  model = Post
  template_name = 'update_post.html'
  fields = ['title','text']

class PostDeleteView(LoginRequiredMixin, DeleteView):
  model = Post
  template_name = 'delete_post.html'
  success_url = reverse_lazy('home')







