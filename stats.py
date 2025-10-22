from collections import defaultdict

def count_words(file_contents):
    return len(file_contents.split())

def count_characters(file_contents):
    char_count = {}
    for char in file_contents.lower():
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

def sort_on(items):
    return items["num"]

def sorted_list(char_dict):
    sorted_char_list = []
    for char in char_dict:
        sorted_char_list.append({"char": char, "num": char_dict[char]})

    sorted_char_list.sort(reverse=True, key=sort_on)
    return sorted_char_list