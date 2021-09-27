from django.test import TestCase

from Posts.models import Post

class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Post.objects.create(title='Sample Title', text='Sample text')

    def test_title_label(self):
        post = Post.objects.get(id=1)
        title = post._meta.get_field('title').verbose_name
        self.assertEqual(title, 'title')

     def test_text_label(self):
        post = Post.objects.get(id=1)
        title = post._meta.get_field('text').verbose_name
        self.assertEqual(title, 'text')

    def test_title_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('title').max_length
        self.assertEqual(max_length, 50)

    def test_get_absolute_url(self):
        post = Post.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(post.get_absolute_url(), '/post/1')