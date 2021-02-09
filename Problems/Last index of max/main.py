def last_indexof_max(numbers):
    current = 0
    ans = 0
    for x in range(0,len(numbers)):
        if numbers[x] >= current:
            current = numbers[x]
            ans = x

    return ans
    # write the modified algorithm here
