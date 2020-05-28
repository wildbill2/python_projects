# A simple program that opens a text file learning_python.txt and displays its content.

#Here is the filename
filename = 'text_files/learning_python.txt'


with open(filename) as file_object:
    lines = file_object.readlines()


text_string = ''
for line in lines:
    text_string += line



print(text_string.replace('Python', 'Java'))
print(text_string.strip())

