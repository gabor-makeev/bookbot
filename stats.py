def get_book_words_count(book_text):
  book_words = book_text.split()
  return len(book_words)

def get_book_characters_count(book_text):
  book_characters = list(book_text.lower())
  book_characters_count = {}

  for book_character in book_characters:
    if book_character in book_characters_count:
      book_characters_count[book_character] += 1
      continue
    
    book_characters_count[book_character] = 1

  return book_characters_count