word = input().title().split()
word_list = []
for i in word:
    word_list.append(i)

word_list[0] = word_list[0].lower()
print("".join(word_list))
