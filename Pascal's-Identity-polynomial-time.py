 
	#Pascal Indentity diferentiation concept replacing newton series
	#Coments coming soon in both lenguages, stay put.
	#Open Source Over symplified solution for All possible combinations given "r" static numberrs looking for convergence in "arr"
	#Given a conditional "n".
	#Effective for Hyper+
	                                                                                     
	def printCombination(arr, n, r): 
	
	data = [0]*r; 
	combinationUtil(arr, data, 0, 
					n - 1, 0, r); 

def combinationUtil(arr, data, start, 
					end, index, r): 
						
	if (index == r): 
		for j in range(r): 
			print(data[j], end = " "); 
		print(); 
		return; 

	i = start; 
	while(i <= end and end - i + 1 >= r - index): 
		data[index] = arr[i]; 
		combinationUtil(arr, data, i + 1, 
						end, index + 1, r); 
		i += 1; 

arr = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 , 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]; 
r = 2; 
n = len(arr);
printCombination(arr, n, r);


#with open('nseries.txt', 'w') as f:
	 #f.write(Combination(arr, n, r))
