import unittest
from Application import text_processor


class TestTextProcessor(unittest.TestCase):

    def setUp(self):
        """Creating instances of TextProcessor for testing."""
        self.processor = text_processor.TextProcessor()

    def test_file_not_found_predefined_words(self):
        """Tests FileNotFoundError for predefined words file."""
        with self.assertRaises(FileNotFoundError):
            self.processor.find_match_count(predefined_words_file="non_existent_file.txt", text_file="textFiles/baseFile.txt")

    def test_file_not_found_text_file(self):
        """Tests FileNotFoundError for text file."""
        with self.assertRaises(FileNotFoundError):
            self.processor.find_match_count(predefined_words_file="tests/preDefinedWordFiles/preDefinedWords1.txt", text_file="non_existent_file.txt")

    def test_find_match_count(self):
        """Tests word counts for existing files."""
        expected_result = {
            'Name': 2,
            'Detect': 0,
            'AI': 1
        }
        result = self.processor.find_match_count(predefined_words_file="tests/preDefinedWordFiles/preDefinedWords1.txt", text_file="tests/textFiles/baseFile.txt")
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
