with open("books/frankenstien.txt") as f:
    file_contents = f.read()
words = file_contents.split()
wc = 0
for word in words:
    wc += 1
print("--- Begin report of books/frankenstein.txt ---")
print (f"{wc} words found in the document")
lower = file_contents.lower()
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz' 
count = {}
for char in ascii_lowercase:
    count[char] = lower.count(char) 
for letter in count:
    print(f"The '{letter}' character was found {count[letter]} times")
print("--- End Report ---")