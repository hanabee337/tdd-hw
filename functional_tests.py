import unittest

from selenium import webdriver


# browser = webdriver.Chrome()
# browser.get('http://localhost:8000')
# assert 'To-Do' in browser.title, "Browser title was " + browser.title
# browser.quit()


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 에디스는 몃진 작업 목록 온라인 앱이 나왔다는 소식을 듣고
        # 해당 웹 사이트를 확인하러 간다
        self.browser.get('http://localhost:8000')

        # 웹 페이지 타이틀과 헤더가 'To-Do'를 표시하고 있다
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # 그녀는 바로 작업을 추가하기로 한다

# 파이썬 스크립트가 다른 스크립트에 import된 것이 아니라,
# 커맨드 라인을 통해서 실행됐다는 것을 확인하는 코드
if __name__ == '__main__':
    # unittest 테스트 실행자를 실행
    unittest.main(warnings='ignore')
