from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
import unittest

class NewUserSignupTest(unittest.TestCase):

    def setUp(self):
        self.display = Display()
        self.display.start()

        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.quit()
        self.display.stop()

    def test_can_upload_a_pet_and_see_it_later(self):
        # Michael hears about a site for dog breeders to socialize their dogs,
        # "Studbook"
        self.browser.get('http://michaelbaechle.pythonanywhere.com/')

        # and confirms that he ended up at the right website
        self.assertIn('Studbook', self.browser.title)

        # He notices there is a spot for him to get started right away
        inputbox = self.browser.find_element_by_id('new_dog_name')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'dog\'s name'
        )

        # by entering his dog's name...
        inputbox.send_keys('TEST: Rin-tin-tin')

        # a picture of the canine
        inputbox = self.browser.find_element_by_id('new_dog_pic')
        self.assertEqual(
            inputbox.get_attribute('type'),
            'file'
        )
        inputbox.send_keys('/home/MichaelBaechle/roverjobs_interview/functional_tests/rintintin.jpg');

        # and finally his name...
        inputbox = self.browser.find_element_by_id('new_owner_name')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'owner\'s name'
        )
        inputbox.send_keys('Lee Duncan')
        inputbox.send_keys(Keys.ENTER)


        # After submitting, he arrives at a new page with other's people's pets
        container = self.browser.find_element_by_id('stud-list')

        # and can also see a thumbnail of his own dog
        elem = self.browser.find_element_by_xpath("//*[contains(.,'TEST: Rin-tin-tin')]");

        # BARK!

if __name__ == '__main__':
    unittest.main()