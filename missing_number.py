def find_missing_number(lst):
    n=len(lst)+1
    total_sum=n*(n+1)//2
    return total_sum-sum(lst)
number=[1,2,3,5]
print(find_missing_number(number))