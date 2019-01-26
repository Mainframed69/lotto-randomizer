#P&R Marketing 2019
#Programado y comentado por Ronal L(Mainframed69). Open Source.
#Código de alto rendimiento Recur>> Convergente >> condicionales estáticas para generar,
#Todas las combinaciones posibles para 'N' en una serie de 'R' iterando a un índice "Y"(Remplazo de Series de Newton por identidades de Pascal )
                                                                             #>>arr:Condicional de serie / Storage Var / Arreglo Temporal <<
                                                                              #^^
#Uso de la función 'def combinationUtil' como printer de 'def printCombination(arr, n, r): //Python 3.7.1+ (virtual.env recomendado)
def printCombination(arr, n, r): 
	# Arreglo temporal para guardar variables
	# Todas las combinaciones una por una 
	data = [0] * r #Función
	# Imprimir todas las combinaciones al:
	# Arreglo temporal'data[]' 
	combinationUtil(arr, n, r, 0, data, 0) 

''' arr[] : Input Array 
n	 : Tamaño del arreglo de entrada 
r	 : Tamaño de una combinación para ser impresa; "Print"
index : Índice actual en data[] 
data[] : Array temporal para guardar variables
			Combinación actual
i	 : índice del elemento actual(n;r) en arr[]	 '''

def combinationUtil(arr, n, r, index, data, i): 

	# Combinación lista, 
	# Imprimir
	#Establecimiento de range(r) para imprimir arreglo tmeporal en la ubicación data[j]
	# 'end = " ")' iterando combinaciones  
	if (index == r): 
		for j in range(r): 
			print(data[j], end = " ") 
		print() 
		return

    #Condicional de regreso
	if (i >= n): 
		return

    #Rotaciones dentro del arreglo 'data[index]' iterando 'def combinationUtil(arr, n, r,)'
    #Establecer condicional para separar las series convergentes utilizando Identidades de Pascal.
    #Convergencia para Todas las series posibles utilizando
    #^^combinationUtil(arr, n, r, index + 1,>> 
								  #<<data, i + 1)>> 
	#<<combinationUtil(arr, n, r, index,>> 
					#<<data, i + 1)>>  
					
					#A continuación:
	data[index] = arr[i] 
	combinationUtil(arr, n, r, index + 1, 
					data, i + 1) 
 
	combinationUtil(arr, n, r, index, 
					data, i + 1) 

#Driver de exclusión para serie 1>28 alojada en arreglo temporal, 'data[r]'
#Excluir los números estáticos para crear convergencía.
if __name__ == "__main__": 
	arr = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 , 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
	#^^Excluir números estaticos de la serie para evtar repeticiones.
	r = 5 #//Ingresar número de series.
	n = len(arr)
	printCombination(arr, n, r)
