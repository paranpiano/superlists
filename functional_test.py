from selenium import webdriver
import unittest

class NewCisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # chajin heard a new tasks web site came out
        # and check the web site
        self.browser.get('http://localhost:8000/')

        # web pages , titel and header has 'To-Do'
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        #he decided to add a new task

        #input "공작 기털 사기" in text box
        #(his hobby is a net make for 날치 잡이용)

        # if key in Enter , reload a page ,
        # "1 : 공장 깃털 사기" item will be added

        # there are more text boxes for additional items' input
        # input "공작 깃털을 이용해서 그물 만들기"

        # page reloaded , two items are in the list.
        # he wants to check if the site stored the items.
        # the site creats to show them with a new URL
        # the URL's description shows.

        # if connect to the URL , he can see the items

        # he will be satisfied with it and sleep.

        browser.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')
