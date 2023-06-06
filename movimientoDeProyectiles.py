
def raizC (num):

    return num ** 0.5

velocidad = 40
grados = 30

Voy = velocidad*1/2
Vox = velocidad*(raizC(3)/2)
g = 9.8

tiempoV = ((Voy/g)*2)
distancia = Vox*tiempoV

print(" ")
print(" ")
print("Tiempo total de vuelo: ",tiempoV,"Segundos")
print("Alcance horizontal del proyectil: ",distancia, "Metros")
print(" ")
print(" ")

