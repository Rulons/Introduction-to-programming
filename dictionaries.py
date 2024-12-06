from collections import Counter

# Step 1: Read the content from the file
with open('textfile.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Step 2: Clean and split the text into words
# Convert to lowercase to ensure case insensitivity and split by non-alphanumeric characters
words = text.lower().split()

# Step 3: Count word frequencies using a dictionary (Counter makes this easier)
word_count = Counter(words)

# Step 4: Find the 5 most common words
most_common_words = word_count.most_common(5)

# Print the 5 most common words
print("5 most common words and their frequencies:")
for word, count in most_common_words:
    print(f"{word}: {count}")
