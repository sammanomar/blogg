from django.test import SimpleTestCase
from .models import Category, Tag, Blog, Comment, Reply

# Create your tests here.

class TestViews(SimpleTestCase):

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, '/templates/home.html')
        
    # def test_blogs(self):
        
    # def test_category_blogs(self):
        
    # def test_tag_blogs(self):
    
    # def test_blog_details(self):

    # def test_add_reply(self):

    # def test_like_blog(self):

    # def test_search_blogs(self):

    # def test_my_blogs(self):
    
    # def test_add_blog(self):

    # def test_update_blog(self):
        