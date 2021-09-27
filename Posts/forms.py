from django.forms import ModelForm 
from .models import Post, Comment 

class PostForm(ModelForm): 
  class Meta: 
    model = Post
    fields = ['title', 'text']

  def __init__(self, *args, user_id=None, **kwargs):   
    super(PostForm, self).__init__(*args, **kwargs)
    self.user_id = user_id

class CommentForm(ModelForm): 
  class Meta: 
    model = Comment
    fields = ['text']

  def __init__(self, *args, user_id=None, **kwargs):   
    super(CommentForm, self).__init__(*args, **kwargs)
    self.user_id = user_id

class SignUpForm(): 
  pass