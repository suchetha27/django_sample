from django.test import TestCase

# Create your tests here.

from . import views

class HomePageTests(TestCase):
    def test_home_page_status_code(self):
        response=self.client.get('/')
        self.assertEquals(response.status_code,200)
    
    def test_home_page_contains_correct_html(self):
        response=self.client.get('/')
        self.assertContains(response,'<h1>Homepage</h1>')

    def test_home_page_does_not_contains_incorrect_html(self):
        response=self.client.get('/')
        self.assertNotContains(response,'Hi there!I should not be the page')
    
    def test_view_uses_correct_template(self):
        response=self.client.get('/')
        self.assertTemplateUsed(response,'testpage.html')
