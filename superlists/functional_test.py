from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        # 将关闭浏览器的方法放到tearDown（）,避免测试发生失败时，浏览器不能关闭。如果setUp()方法执行异常，将不会执行tearDown()方法。
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8100')
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

if __name__ == '__main__':
    #启动unittest的测试运行程序，在文件中自动查找测试类和方法，然后运行
    unittest.main()