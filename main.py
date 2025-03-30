from stats import get_num_words, char_count, sorted_char_count
import sys

def get_book_text(path_to_book):
    with open(path_to_book) as f:
        file_content = f.read()
    return file_content

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    book_text = get_book_text(path)
    dict_to_sort = char_count(book_text)
    word_count = get_num_words(book_text)
    sorted_count = sorted_char_count(dict_to_sort)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words ")
    print("--------- Character Count -------")

    for c in sorted_count:
        char = c["char"]
        count = c["count"]

        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")


main()
