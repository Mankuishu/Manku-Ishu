def most_frequent(lst):
	counter = Counter(lst)
	return counter.most_common(1)[0][0]
numbers = [1,2,2,3,3,3,4,4,4,4]
print(most_frequent(numbers)