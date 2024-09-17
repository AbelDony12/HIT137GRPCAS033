Group Name: [Group CAS033]

Group Members:
[Name: Saj Pradhan] -[ID: S309494]
[Name: Imran Masud] -[ID: S376952]
[Name: Abel Aynikkadan Dony] -[ID: S379301]
[Name: Ibrahim Salman] -[ID: S376575]

def separate_and_convert(input_str):
    number_str = ''.join(char for char in input_str if char.isdigit())
    letter_str = ''.join(char for char in input_str if char.isalpha())

    even_numbers = [char for char in number_str if int(char) % 2 == 0]
    ascii_numbers = [ord(char) for char in even_numbers]

    ascii_letters = [ord(char) for char in letter_str if char.isupper()]

    return ''.join(map(str, ascii_numbers)), ''.join(map(str, ascii_letters))

input_str = '56aAww1984sktr235270aYmn145ss785fsq31D0'
result_numbers, result_letters = separate_and_convert(input_str)

print(f'Number String: {result_numbers}')
print(f'Letter String: {result_letters}')
