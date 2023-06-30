def calcularAlturaCaida(t):
    g = 9.8
    h = (1/2) * g * t**2
    return h

tiempoCaida = float(input("Digite el tiempo que se demoro en caer el objeto: "))

alturaCaida = calcularAlturaCaida(tiempoCaida)

print("La manzana cayó desde una altura de ",alturaCaida," metros.")
