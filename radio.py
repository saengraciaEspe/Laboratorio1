#Reglas 
    #Locaciones A, B y C
    #Posibles valores de estado
    #0 indica transmisión de la emisora
    #1 indica sin transmisión de la emisora
cont_habit=0
#Se tiene las habitaciones A,B y C
habitaciones=['A','B','C']
print("---Radio IA---")
costo=0;
#En este caso se usa recorre las habitaciones A,B y c usando el bucle for
for x in habitaciones:
    print("-----Radio en habitación "+habitaciones[cont_habit]+"-----")
    estados_ideales="A:0,B:0,C:0";
   
    
    #Se toma el estado inicial de la habitación
    estado_inicial=int(input("Estado de habitación "+habitaciones[cont_habit]+": ")) 
    print("Estados ideales "+estados_ideales)
    #Se almacena el estado de la habitación A como boolean
    estados_iniciales={habitaciones[cont_habit]:bool(estado_inicial)}
   

    if not estados_iniciales[habitaciones[cont_habit]]:
        #Si transmite la emisora en la habitación entonces
        #Se muestra la habitación y el correspondiente estado
        print("Si transmite la emisora en la habitación: "+habitaciones[cont_habit]);
        #Como si transmite no es necesario sintonizar otra emisora,
        #por lo tanto no aumenta el costo
        print("Costo actual: "+str(costo))
    else:
        #En caso de que no hay transmisión 
        print("No hay transmisión en la habitación: "+habitaciones[cont_habit]);
        print("Se cambia de emisora")
        #Ahora se procede a cambiar el estado 
        estados_iniciales[habitaciones[cont_habit]]=False
        costo+=1#Costo aumenta por cambiar de emisora
        print("Costo actual: "+str(costo))
    cont_habit+=1;

