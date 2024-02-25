from dotenv import load_dotenv
import os

load_dotenv()

book_path = os.environ.get('BOOK_PATH')

with open(book_path) as f:
    file_contents = f.read()


def count_words(book_text):
    total = 0
    words = book_text.split()

    for word in words:
        total += 1

    return total


def count_letters(book_text):
    letters = {}

    for word in book_text:
        word_characters = word.lower().split()

        for character in word_characters:
            is_letter = character.isalpha()

            if is_letter:
                if letters.get(character) is None:
                    letters[character] = 1
                else:
                    letters[character] = letters.get(character) + 1

    return letters


def generate_report():
    count_letters_dic = count_letters(file_contents)
    count_letters_list = list(count_letters_dic.keys())
    count_letters_list.sort()

    print(f"--- Begin report of {book_path} ---")

    print(f"{count_words(file_contents)} words found in the document")

    print()

    for letter in count_letters_list:
        print(
            f"The {letter} character was found " +
            f"{count_letters_dic[letter]} times")

    print("--- End report ---")


generate_report()
