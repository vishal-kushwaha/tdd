import time

from selenium.webdriver.chrome.webdriver import WebDriver


from selenium import webdriver
import unittest

from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path='./drivers/chromedriver')

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(input_box.get_attribute('placeholder'), 'Enter a to-do item')

        # She types "Buy peacock feathers" into a text box (Edith's hobby is tying fly-fishing lures)
        input_box.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list table
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: Buy peacock feathers' for row in rows))

        # There is still a text box inviting her to add another item. She enters "Use peacock feathers to make a fly"
        # (Edith is very methodical)
        self.fail('Finish the test!')

        # The page updates again, and now shows both items on her list

        # Edith wonders whether the site will remember her list. Then she sees that the site has generated a unique URL
        # for her -- there is some explanatory text to that effect.

        # She visits that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep


# Edith has heard about a cool new online to-do app. She goes to check out its homepage.

# She notices the page title and header mention to-do lists
def test_can_start_a_list_and_retrieve_it_later(selenium: WebDriver) -> None:
    selenium.get('http://localhost:8000')
    assert 'To-Do' in selenium.title

    header_text = selenium.find_element_by_tag_name('h1').text
    assert 'To-Do' in header_text

    # She is invited to enter a to-do item straight away
    input_box = selenium.find_element_by_id('id_new_item')
    assert input_box.get_attribute('placeholder') == 'Enter a to-do item'

    # She types "Buy peacock feathers" into a text box (Edith's hobby is tying fly-fishing lures)
    input_box.send_keys('Buy peacock feathers')

    # When she hits enter, the page updates, and now the page lists "1: Buy peacock feathers" as an item in a to-do list
    input_box.send_keys(Keys.ENTER)
    time.sleep(1)

    table = selenium.find_element_by_id('id_list_table')
    rows = table.find_elements_by_tag_name('tr')
    assert any(row.text == '1: Buy peacock feathers' for row in rows)

    # There is still a text box inviting her to add another item. She enters "Use peacock feathers to make a fly"
    # (Edith is very methodical)
    raise AssertionError('Finish the test')

    # The page updates again, and now shows both items on her list

    # Edith wonders whether the site will remember her list. Then she sees that the site has generated a unique URL for
    # her -- there is some explanatory text to that effect.

    # She visits that URL - her to-do list is still there.

    # Satisfied, she goes back to sleep
