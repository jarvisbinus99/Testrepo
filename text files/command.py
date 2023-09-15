import sys
import wordcount
from wordcount import count_words
if len(sys.argv) != 2:
    print("Usage: python wordcount.py <filename>")
else:
    filename = sys.argv[1]
    word_count = count_words(filename)
    if word_count:
        for word, count in word_count.items():
            print(f"{word}: {count} occurrences")
        
