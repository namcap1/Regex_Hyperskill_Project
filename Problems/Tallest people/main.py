def tallest_people(**name):
    tallest = max(name.values())
    for key, value in sorted(name.items()):
        if value == tallest:
            print(key, ':', value)
