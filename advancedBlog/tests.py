from django.test import TestCase
from .models import Post, Category, Comments
from .forms import CategoryForm, PostForm
from django.contrib.auth.models import User

class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a test user
        user = User.objects.create(username='testuser')
        # Create a test category
        category = Category.objects.create(categoryName='Test Category')
        # Create a test post
        Post.objects.create(author=user, title='Test Title', tag='Test Tag',
                            category=category.categoryName, description='Test Description')

    def test_title_content(self):
        # Retrieve the test post and check if its title matches
        post = Post.objects.get(id=1)
        self.assertEqual(post.title, 'Test Title')

    def test_tag_content(self):
        # Retrieve the test post and check if its tag matches
        post = Post.objects.get(id=1)
        self.assertEqual(post.tag, 'Test Tag')

class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a test category
        Category.objects.create(categoryName='Test Category')

    def test_category_name(self):
        # Retrieve the test category and check if its name matches
        category = Category.objects.get(id=1)
        self.assertEqual(category.categoryName, 'Test Category')

class CommentsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a test user
        user = User.objects.create(username='testuser')
        # Create a test category
        category = Category.objects.create(categoryName='Test Category')
        # Create a test post
        post = Post.objects.create(author=user, title='Test Title', tag='Test Tag',
                                   category=category.categoryName, description='Test Description')
        # Create a test comment associated with the test post
        Comments.objects.create(post=post, name='Test Name', comment='Test Comment')

    def test_comment_name(self):
        # Retrieve the test comment and check if its name matches
        comment = Comments.objects.get(id=1)
        self.assertEqual(comment.name, 'Test Name')

class PostFormTest(TestCase):
    def test_valid_form(self):
        # Create a test category
        category = Category.objects.create(categoryName='Test Category')
        # Prepare data for a valid form submission
        form_data = {'title': 'Test Title', 'tag': 'Test Tag', 'category': category.pk,
                     'image': None, 'description': 'Test Description'}
        form = PostForm(data=form_data)
        # Check if the form is valid
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        # Prepare data for an invalid form submission (empty data)
        form = PostForm(data={})
        # Check if the form is invalid
        self.assertFalse(form.is_valid())

class CategoryFormTest(TestCase):
    def test_valid_form(self):
        # Prepare data for a valid category form submission
        form_data = {'categoryName': 'Test Category'}
        form = CategoryForm(data=form_data)
        # Check if the form is valid
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        # Prepare data for an invalid category form submission (empty data)
        form = CategoryForm(data={})
        # Check if the form is invalid
        self.assertFalse(form.is_valid())

class HomeViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        # Test whether the home view URL exists and returns a status code of 200 (OK)
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        # Test whether the home view uses the correct HTML template
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
