def average_mark(*marks):
    total = 0
    for i in marks:
        total += i
    return round((total / len(marks)),1)
