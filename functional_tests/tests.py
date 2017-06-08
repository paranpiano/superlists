from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
import  time

import unittest

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self , row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 에디스(Edith)는 멋진 작업 목록 온라인 앱이 나왔다는 소식을 듣고
        # 해당 웹 사이트를 확인하러 간다
        self.browser.get(self.live_server_url)

        # 웹 페이지 타이틀과 헤더가 ‘To-Do’를 표시하고 있다
        header_text = self.browser.find_element_by_tag_name('h1').text

        # 그는 바로 작업을 추가하기로 한다
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'input a task item'
        )

        # 엔터키를 누르면 새로운 URL로 바뀐다. 그리고 작업 목록에
        # "1: 공작깃털 사기" 아이템이 추가된다
        inputbox.send_keys('Buying peacock feather')
        inputbox.send_keys(Keys.ENTER)

        time.sleep(1)
        chajin_list_url = self.browser.current_url
        print('redirected url : ' + chajin_list_url)
        self.assertRegex(chajin_list_url, '/lists/.+')

        time.sleep(1)
        self.check_for_row_in_list_table('1: Buying peacock feather')

        # 추가 아이템을 입력할 수 있는 여분의 텍스트 상자가 존재한다
        # 다시 "공작깃털을 이용해서 그물 만들기"라고 입력한다 (에디스는 매우 체계적인 사람이다)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('making a net with peacock feather')
        inputbox.send_keys(Keys.ENTER)

        # 페이지는 다시 갱신되고, 2개 아이템이 목록에 보여진다
        time.sleep(1)
        self.check_for_row_in_list_table('2: making a net with peacock feather')
        self.check_for_row_in_list_table('1: Buying peacock feather')

        # 새로운 사용자인 natalia 사이트에 접속한다

        ## 새로운 브라우저 세션을 이용해서 에디스의 정보가
        ## 쿠키를 통해 유입되는 것을 방지한다
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # natalia 가 홈페이지에 접속한다
        # chajin 리스트는 보이지 않는다
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buying peacock feather',page_text)
        self.assertNotIn('making a net with peacock feather',page_text)

        # 프란시스가 새로운 작업 아이템을 입력하기 시작한다
        # 그는 에디스보다 재미가 없다
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buying milk')
        inputbox.send_keys(Keys.ENTER)

        #natalia가 전용 URIL을 취득한다.
        natalia_list_url = self.browser.current_url
        self.assertRegex(natalia_list_url, '/lists/.+')
        self.assertNotEqual(natalia_list_url, chajin_list_url)

        # chajin 입력한 흔적이 없다는 것을 다시 확인한다
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buying peacock feather', page_text)
        self.assertIn('Buying milk' , page_text)

        # 둘 다 만족하고 잠자리에 든다


