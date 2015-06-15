def count (sequence, item):
	total = 0
	
	if isinstance(sequence, list):
		
		for find in sequence:	
			if item == find:
				total = total + 1
	
   	print total 	
    	return total
       

count(["Aditya",4,5,6,7,8, 1.234, "Aditya", 'A'], "Aditya")
#count('Aditya is good', 'is')
#count(2, 1)
#count('A', 'A')


