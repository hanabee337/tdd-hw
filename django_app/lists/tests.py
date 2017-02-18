from django.http import HttpResponse
from django.template.loader import render_to_string
from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page

# Create your tests here.
# class SmokeTest(TestCase):
#     def test_bad_maths(self):
#         self.assertEqual(1 + 1, 3)


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)


    def test_home_page_returns_correct_html(self):
        request = HttpResponse()
        response = home_page(request)
        # 템플릿을 이용한 렌더링 테스트 : render_to_string 함수를 이용.
        expected_html = render_to_string('home.html')
        self.assertTupleEqual(response.content.decode(), expected_html)