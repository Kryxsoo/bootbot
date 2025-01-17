def main():

  booked = book()
  counted = counter(booked)
  print(counted)

def counter(book):
  counted = len(book.split())
  return counted

def book():
  with open("books/frankenstein.txt") as f:
    content = f.read()
  return content

main()
