def second_largest(lst):
    if len(lst) < 2:
        return None
    largest = second_largest = float('-inf')
    for num in lst:
        if num > largest:
            second_largest=largest=largest
            largest=num
        elif num>second_largest and num != largest:
            second_largest=num
    return second_largest
numbers=[1,2,3,4,5]
print(second_largest(numbers))