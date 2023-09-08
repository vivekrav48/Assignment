def are_anagrams(word1, word2):
    return sorted(word1.lower()) == sorted(word2.lower())

def find_anagrams(word, word_list):
    anagrams = [w for w in word_list if are_anagrams(word, w)]
    return anagrams

# Example usage:
word = "listen"
word_list = ["enlist", "silent", "tinsel", "apple", "inlets"]

result = find_anagrams(word, word_list)
print(f"The anagrams of '{word}' in the list are: {result}")