def calcularVf(t):
    g = 9.8 
    vf = g * t
    return vf

def calcularAltura(altuaEdificio, tiempo):
    altura = (1/2) * 9.8 * tiempo**2
    return altuaEdificio - altura

#100 y 10 xd

alturaEdificio = float(input("Digite la altura de la construccion en metros: "))
tiempoCaida = float(input("Digite el tiempo de caida en segundos: "))

vf = calcularVf(tiempoCaida)
print("La velocidad final del objeto a los ",tiempoCaida," segundos es: ",vf," m/s")

altura = calcularAltura(alturaEdificio, tiempoCaida)
print("La altura del edificio es: ",altura," metros")
