import math
g=  9.81
mayor=0
angulo =0

velocidadInicial = int(input("Por favor ingresar la velocidad inicial:"))

for i in range (0,95,5):
    
    vini=(2 * velocidadInicial *2* math.sin (i)* math.cos (i))/g
    if (vini > mayor):
        mayor=vini
        angulo=i

        print ( "El angulo con un lanzamiento mas largo es: "+str(angulo)+"y alcanza una mayor distancia de:"+
                str(mayor)+"metros por segundo")
