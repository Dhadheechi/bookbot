from stats import count_words
from stats import count_characters, sorted_list
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    file_contents = get_book_text(filepath)
    # print(count_characters(file_contents))
    sorted_list_dicts = sorted_list(count_characters(file_contents))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(file_contents)} total words")
    print("--------- Character Count -------")

    for dict in sorted_list_dicts:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")

    print("============= END ===============")


main()