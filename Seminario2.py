#Grupo 13
#Oscar Delgado Miranda
#Miguel Angel Perez Garcia

def ListaPokemon():
	#Abrimos el fichero pokemon.txt en modo lectura
	fichero = open('pokemon.txt','r')
	
	#Cogemos todo el fichero como un string y con el metodo split()
	#devolvemos una lista de todas las palabras en el string 
	lista = fichero.read().split()
	
	#Creamos 2 listas adicionales, una auxiliar y otra donde tendremos 
	#la mayor combinacion de palabras que hayamos encontrado
	lista_aux = []
	lista_res = []

	for i in lista:
		ultima = i[-1] #Ultima letra de la palabra
		lista_aux.append(i) #Introducimos dicha palabra en la lista auxiliar

		primera = lista[0][0] #Primera letra de la primera palabra
		j = 0 
		
		while j < len(lista):
			#Si la palabra encontrada no es la misma de la que tenemos la ultima letra
			#y esa palabra no la hemos usado ya
			if i != lista[j] and lista[j] not in lista_aux:
				primera = lista[j][0] #primera letra de la palabra actual
				
				#Si coinciden la ultima letra que teniamos guardada
				#y la primera de la palabra actual que estamos comprobando
				if primera == ultima: 
					lista_aux.append(lista[j]) #La anadimos a la lista auxiliar
					ultima = lista[j][-1] #Cambiamos la ultima letra que teniamos por la de la nueva palabra
					j = -1 #Cambiamos el indice para recorrer de nuevo la lista desde el principio
				
			j = j + 1
		
		#Si la lista auxiliar es mas grande que la lista resultado que teniamos guardada
		#la lista auxiliar pasa a ser la lista resultado
		if len(lista_res) < len(lista_aux):
			del lista_res[:]
			lista_res.extend(lista_aux)
		
		del lista_aux[:]
	
	#Imprimimos la lista resultado que hemos generado
	print "La lista resultado tiene",len(lista_res), "palabras:"

	for i in lista_res:
		print i

ListaPokemon()
