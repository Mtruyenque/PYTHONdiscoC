def promedio(numb1, numb2, numb3):
    resultado = numb1 + numb2 + numb3 
    resultado = resultado / 3
    return resultado
nota = promedio (10, 20, 30,)
print("el promedio es :" , nota )
    
#_______________________________________________
    
def promedio(numb1, numb2, numb3):
    return (numb1 + numb2 + numb3)/3
nota = promedio(20, 20, 50,)
print(nota)
#___________________________________
def restamos(numb1, numb2):
    return (numb1 - numb2) 

print(restamos(40, 20 ))
print(restamos (50, 40 ))
print(restamos(100, 20))

#____________________________________________

print(restamos(numb1=5, numb2=10)) # se puede intercambiar datos 
#________________________________________________________
def saludo (nombre , apellido,edad):
    print("Me llamo", nombre, apellido,"y tengo", edad , "años ")
saludo("moises", "spencer", 29) 
saludo("juan", "del carpio", 27)  #Ayuda a no escribir tanto print
saludo("melany" , "zahara", 31)
#_____________________________________________________________
def saludo (nombre , apellido,edad):
    print(f"Me llamo {nombre} {apellido} y tengo {edad} años ") #las llaves
saludo("moises", "spencer", 29)                     #permite mostran en pantalla sin 
saludo("juan", "del carpio", 27)                    #tanta comillas y comas 
saludo("melany" , "zahara", 31)
