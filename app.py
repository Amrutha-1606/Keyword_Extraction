import re
from collections import Counter

# Get text from the user
text = input("Enter a paragraph: ")

# Check if text is empty
if not text.strip():
    print("Please enter some text.")
    exit()

# Convert text to lowercase
text = text.lower()

# Extract words
words = re.findall(r'\b[a-zA-Z]+\b', text)

# Common words to ignore
stop_words = {
    "the", "is", "a", "an", "and",
    "or", "of", "to", "in", "on",
    "for", "are", "was", "were",
    "this", "that", "with", "from",
    "it", "as", "by"
}

# Remove common words
keywords = [
    word for word in words
    if word not in stop_words
]

# Count keyword frequency
frequency = Counter(keywords)

# Display top keywords
print("\nTop Keywords:")

for word, count in frequency.most_common(5):
    print(word, "-", count, "time(s)")