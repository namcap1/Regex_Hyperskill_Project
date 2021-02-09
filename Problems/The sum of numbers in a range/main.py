def range_sum(numbers, start, end):
    ans = 0
    for i in numbers:
        if i >= start and i <= end:
            ans += i
    return ans

input_numbers = list(map(int, input().split()))
a, b =  map(int, input().split())
print(range_sum(input_numbers, a, b))
