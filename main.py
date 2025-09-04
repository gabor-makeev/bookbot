from stats import get_book_words_count, get_book_characters_count

def main():
  book_path = "books/frankenstein.txt"
  book_text = get_book_text(book_path)
  book_words_count = get_book_words_count(book_text)
  
  print(f"{book_words_count} words found in the document")

  book_characters_count = get_book_characters_count(book_text)

  print(book_characters_count)

def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()

main()