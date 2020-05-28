# Program to find a common word in a text file.

def get_common_word(filename, word):
    try:
        with open(filename, encoding='utf-8') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print("File not found.")
    else:
        """Count the number of times a word appears."""
        num_words = contents.lower().count(word)
        print(num_words)


filenames = ['text_files/alice.txt', 'text_files/siddhartha.txt', 'text_files/moby_dick.txt', 'text_files/little_women.txt']
for file in filenames:
    get_common_word(file, 'the')


