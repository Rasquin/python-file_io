# re library--> regular expresions
import re

# collections library --->  to count ocurrences of words
import collections

text= open('book.txt').read().lower()

#the findall() method ensures that all occurrences of the
#pattern are found. The pattern we're using is \w+
#The w denotes anything that's not a whitespace, and the plus denotes one or more. So, for every
#occurrence of one or more characters that are not whitespace, we view that as
#a word. We may get some false positives - it's not perfect but it works fine for
#our purposes here
words = re.findall('\w+', text)

print(collections.Counter(words).most_common(10))