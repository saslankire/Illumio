# Illumio Take Home Problem 

---

## Project Overview

This project implements a `TextProcessor` class in Python that counts the frequency of predefined words in a text file. It handles scenarios where files may not be found and provides unit tests to verify its functionality.

## Installation Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your_username/your_repository.git
   cd your_repository
    ```
2. **Install dependencies:**
    ```
   pip install -r requirements.txt
   ```
3. **Usage Example:**
    Please refer main.py file in the root directory to run the program.
    ```python
    from Application import text_processor
    temp = text_processor.TextProcessor()
    result = temp.find_match_count(predefined_words_file="tests/preDefinedWordFiles/preDefinedWords1.txt", text_file="tests/textFiles/baseFile.txt")
    print(result)
    ```
4. **Unit Tests:**
    Please refer to the test file to refer the basic unitests verifies the **FileNotFoundError** and also verifies the word match count in the sample files provided. 
   To run the sample tests please run the following bash commands in root directory path. One might face errors in running the files in test directory due to Ambiguity of paths.
    ```bash
      python -m tests/testFileName
    ```
5. **Assumptions:**
    All the assumptions that were given in the problem statement were taken into consideration but howerever in the cases of special characters arising in a word, special characters have been cleaned and the entire word text has been concatenated.
    ```text
       good-for-nothing -> goodfornothing
       Dursley's -> Dursleys
       AI. -> AI
    ```
6. **Complexity of the code**
    We are traversing the entire preDefined Words file once and text file once and are only counting the words in the predDefined Word, to Ignore the case sensitivity we are keeping track of lowercase word as key in the map along with the orginal word. Returning dict,values() would have been sufficient for better readability we are Copying the values into a new dictionary.
