from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings

class Post(models.Model):
  title = models.CharField(max_length=50)
  text = models.TextField()
  date = models.DateTimeField(auto_now_add=True)
  user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, default='')

  class Meta: 
    ordering = ['date']

  def get_absolute_url(self):
    return reverse('post', args=[str(self.id)])

class Comment(models.Model): 
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
  user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, default='')
  text = models.TextField()
  date = models.DateTimeField(auto_now_add=True)
  active = models.BooleanField(default=False)

  class Meta: 
    ordering = ['date']

  def __str__(self): 
    return 'Comment {} by {}'.format(self.text, self.user_id)



