from django.test import TestCase

# class BasicTest(TestCase):
#     def test_fields(self):
#         pass

from django.test import TestCase
from django.contrib.auth.models import User
from .models import userPost


class userPostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', 
            password='testpass'
        )
        self.user_post = userPost.objects.create(
            user=self.user, 
            description='test description', 
            category='Business'
        )
        
    def test_user_post_str(self):
        self.assertEqual(str(self.user_post), 'test description')
        
    def test_user_post_upload_to(self):
        upload_to = self.user_post.itemPhoto.field.upload_to
        self.assertEqual(upload_to, 'images/')

# Create your tests here.
