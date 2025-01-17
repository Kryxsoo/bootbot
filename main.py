def main():

  booked = book()
  counted = counter(booked)
  chars_dict = get_character(booked)
  print(chars_dict)

def char(booked):
  match = []
  alpha = 0
  for letter in booked:
    if letter == match:
      alpha += 1
    return alpha

def counter(book):
  counted = len(book.split())
  return counted

def get_character(book):
  chars = {}
  for c in book:
    lowered = c.lower()
    if lowered in chars:
      chars[lowered] += 1
    else:
      chars[lowered] = 1
  return chars

def book():
  with open("books/frankenstein.txt") as f:
    content = f.read()
  return content

main()
