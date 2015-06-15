def purify(numbers):
	odd = []	
	for index, num in enumerate(numbers):
		if num % 2 == 0:
			odd.append(num) 	
	print odd	
	return odd 

purify([13, 5, 7, 11, 2])
