from django.test import SimpleTestCase
from .forms import AddBlogForm

# Create your tests here.

class TestAddBlogForm(SimpleTestCase):

    def test_blog_title_is_required(self):
        form = AddBlogForm({'title':''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_blog_category_is_required(self):
        form = AddBlogForm({'category':''})
        self.assertFalse(form.is_valid())
        self.assertIn('category', form.errors.keys())
        self.assertEqual(form.errors['category'][0], 'This field is required.')

    def test_blog_banner_is_required(self):
        form = AddBlogForm({'banner':''})
        self.assertFalse(form.is_valid())
        self.assertIn('banner', form.errors.keys())
        self.assertEqual(form.errors['banner'][0], 'This field is required.')

    def test_blog_descritpion_is_required(self):
        form = AddBlogForm({'description':''})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(form.errors['description'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = AddBlogForm()
        self.assertEqual(form.Meta.fields, ('title', 'category', 'banner','description'))