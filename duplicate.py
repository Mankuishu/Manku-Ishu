def remove_duplicate(lst):
	return list(dict.fromkeys(lst))
print(remove_duplicates([1,2,2,3,4,4,5]))