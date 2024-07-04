# This is a sample Python script.


from Application import text_processor

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    temp = text_processor.TextProcessor()
    print(temp.find_match_count(predefined_words_file="tests/preDefinedWordFiles/preDefinedWords1.txt", text_file="tests/textFiles/baseFile.txt"))



