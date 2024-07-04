import os
class TextProcessor:
    def __init__(self):
        # Initialize the TextProcessor class
        pass

    def find_match_count(self, predefined_words_file, text_file):
        """
        Counts the frequency of predefined words in a text file.

        Args:
            predefined_words_file (str): File name of the predefined words file.
            text_file (str): File name of the text file.

        Returns:
            dict: A dictionary containing the frequency of predefined words.
        """
        # Create an empty dictionary to store the frequency of predefined words
        pre_defined_freq_dict = {}
        try:
            with open(predefined_words_file, 'r') as words:
                # Read the predefined words file and store the words in the dictionary
                for line in words:
                    final_text = ''.join(char for char in line if char.isalpha())
                    original_word = [str(final_text), int(0)]
                    pre_defined_freq_dict[final_text.lower()] = original_word
        except FileNotFoundError:
            raise FileNotFoundError(f"The file '{predefined_words_file}' doesn't exist in the path")
        # Process the text file
        try:
            with open(text_file, 'r') as text:
                # Read the text file and count the frequency of predefined words
                for line in text:
                    words = line.split()
                    for word in words:
                        final_word = ''.join(char for char in word if char.isalpha())
                        if final_word.lower() in pre_defined_freq_dict:
                            pre_defined_freq_dict[final_word.lower()][1] += 1
        except FileNotFoundError:
            raise FileNotFoundError(f"The file '{text_file}' doesn't exist in the path")
        final_result = {}
        for value in pre_defined_freq_dict.values():
            final_result[value[0]]=value[1]
        # Return the frequency dictionary
        return final_result