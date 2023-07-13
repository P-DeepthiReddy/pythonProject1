from collections import Counter
n = int(input())
words_list = [input() for _ in range(n)]
word_count = Counter(words_list)
print(len(word_count))
print(*word_count.values())