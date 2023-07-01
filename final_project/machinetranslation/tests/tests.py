from translator import englishToFrench, frenchToEnglish
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertNotEqual(englishToFrench('Hello'), 'Pain')
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertNotEqual(englishToFrench('car'), 'maman')
        self.assertEqual(englishToFrench('I love my wife'), "J'aime ma femme.")
        self.assertEqual(frenchToEnglish('maison'), 'mosaic to you')
        self.assertEqual(frenchToEnglish('Comment allez vous?'), 'How are you doing? ')
        
unittest.main()