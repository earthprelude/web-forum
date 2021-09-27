from django.urls import path, include
from .views import HomePageView, PostPageView, PostCreateView, PostUpdateView, PostDeleteView
from .views import CommentCreateView

urlpatterns = [
  path('post/<int:pk>/add_comment',
  CommentCreateView.as_view(),name='create_comment'), 
  path('post/<int:pk>/',PostPageView.as_view(), name='post'), 
  path('create',PostCreateView.as_view(), name='create_post'),
  path('post/<int:pk>/edit/',PostUpdateView.as_view(), name='update_post'),
  path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='delete_post'),
  path('accounts/', include('django.contrib.auth.urls')),

  path('', HomePageView.as_view(), name='home'),
]