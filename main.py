def main():

    book_path = "books/frankenstein.txt"
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count(book_path)} words found in the document")
    print()
    
    ret_dict = char_count(book_path)
    key_value_list = [(key, value) for key, value in ret_dict.items()]
    key_value_list.sort(key = lambda tup: tup[1], reverse = True)

    for i in range(len(key_value_list)):
        print(f"The '{key_value_list[i][0]}' character was found {key_value_list[i][1]} times")

    print("--- End report ---")
def read_contents(path):
    with open(path) as f:
        return f.read()

def word_count(path):
    count = 0
    content = read_contents(path)
    words = content.split()
     
    for word in words:
        count += 1
    return count

def char_count(path):
    content = read_contents(path)
    content_lowercase = content.lower()
    words = content_lowercase.split()

    char_dict = {}

    for word in words:
        for character in word:
            if character.isalpha():
                if character in char_dict:
                    char_dict[character] += 1
                else:
                    char_dict[character] = 1
    return char_dict

main()