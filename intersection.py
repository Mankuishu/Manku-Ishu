def intersection(list1,list2):
    return [value for value in list1 if value in list2]
list1=[1,2,3,4,5]
list2=[4,5,6,7,8]
print(intersection(list1,list2))