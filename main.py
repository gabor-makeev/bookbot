import sys
from stats import get_book_words_count, get_book_characters_count, get_sorted_char_count

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  book_path = sys.argv[1]

  print("============ BOOKBOT ============")

  print(f"Analyzing book found at {book_path}")

  book_text = get_book_text(book_path)
  book_words_count = get_book_words_count(book_text)
  
  print("----------- Word Count ----------")
  print(f"Found {book_words_count} total words")

  book_characters_count = get_book_characters_count(book_text)
  sorted_char_count_list = get_sorted_char_count(book_characters_count)

  print("--------- Character Count -------")

  for item in sorted_char_count_list:
    if item["char"].isalpha() == False:
      continue

    print(f"{item["char"]}: {item["num"]}")

  print("============= END ===============")


def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()

main()