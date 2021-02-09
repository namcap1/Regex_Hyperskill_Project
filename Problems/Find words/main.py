words = input().split()
words_with_s = [i for i in words if i.endswith('s')]
print("_".join(words_with_s))
