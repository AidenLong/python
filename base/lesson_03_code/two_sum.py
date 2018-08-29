def two_sum(numbers, target):
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if (numbers[i] + numbers[j]) == target:
                return [i, j]

    return [-1, -1]

ret = two_sum([2, 7, 11, 15], 18)
print(type(ret))
print(two_sum([2, 7, 11, 15], 18))
print(two_sum([2, 7, 11, 15], 30))
