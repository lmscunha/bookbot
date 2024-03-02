from dotenv import load_dotenv
import os

load_dotenv()

book_path = os.environ.get('BOOK_PATH')

with open(book_path) as f:
    book = f.read()


class Bookbot:
    def __init__(self, book):
        self.book = book

    def __count_words(self, book_text):
        total = 0
        words = book_text.split()

        for word in words:
            total += 1

        return total

    def __count_letters(self, book_text):
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

    def generate_report(self):
        count_letters_dic = self.__count_letters(self.book)
        count_letters_list = list(count_letters_dic.keys())
        count_letters_list.sort()

        print(f"--- Begin report of {book_path} ---")

        print(f"{self.__count_words(self.book)} words found in the document")

        print()

        for letter in count_letters_list:
            print(
                f"The '{letter}' character was found " +
                f"{count_letters_dic[letter]} times")

        print("--- End report ---")


book_bot = Bookbot(book)
book_bot.generate_report()
