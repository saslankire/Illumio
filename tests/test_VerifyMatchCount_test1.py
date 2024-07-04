import unittest
from Application import text_processor


class TestTextProcessor(unittest.TestCase):

    def setUp(self):
        """Creating instances of TextProcessor for testing."""
        self.processor = text_processor.TextProcessor()

    def test_find_match_count(self):
        """Tests word counts for existing files."""
        expected_result = {
            'Dursley': 7,
            'Dursleys': 5,
            'Think': 2
        }
        result = self.processor.find_match_count(predefined_words_file="tests/preDefinedWordFiles/preDefinedWords2.txt", text_file="tests/textFiles/testFile1.txt")
        self.assertEqual(result, expected_result)

    def test_find_match_count_two(self):
        """Tests word counts for existing files."""
        expected_result = {
            'Mrs': 7,
            'goodForNothing':1
        }
        result = self.processor.find_match_count(predefined_words_file="tests/preDefinedWordFiles/preDefinedWords3.txt",
                                                 text_file="tests/textFiles/testFile1.txt")
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
