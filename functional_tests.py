from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()

  def tearDown(self):
    self.browser.quit()

  def test_can_start_a_list_and_retreive_it_later(self):
    # Edith goes to homepage
    self.browser.get('http://localhost:8000')

    # She notices the page title and header mention to-do lists
    self.assertIn('To-Do', self.browser.title)
    self.fail('Finish the test!')

    # She is invited to enter a to-do item

    # She types "Buy peacock feathers" into a text box

    # When she hits enter, the page updates.  Now the page lists "1: Buy peacock feathers"
    # as an item in a to-do list

    # There is still a textbox inviting her to add another item.
    # She enters "Use peacock feathers to make a fly"

    # The page updates again, and now she sees both items on her list

    # Edith Wonders weather the site will remember her list, then she sees that the site has
    # Generated a unique url for her.  There is some explanitory text to that effect.

    # She visits that URL.  her to-do list is still there.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
