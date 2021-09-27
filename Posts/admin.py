from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin): 
  list_display = ('user_id','text', 'post', 'date')
  list_filter = ('active', 'date')
  search_fields = ('user_id', 'text')
  actions = ['approve_comments']

  def approve_comments(self, request, queryset): 
    queryset.update(active=True)
