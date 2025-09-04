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

def get_sorted_char_count(chars_count_dict):
  chars_count_list = []

  for char in chars_count_dict:
    chars_count_list.append({
      "char": char,
      "num": chars_count_dict[char]
    })

  chars_count_list.sort(reverse=True, key=sort_on)

  return chars_count_list

def sort_on(item):
  return item["num"]