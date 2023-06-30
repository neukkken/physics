import math

def calcular_tiempo_vuelo(velocidad_inicial, angulo):
    angulo_rad = math.radians(angulo)
    tiempo_vuelo = (2 * velocidad_inicial * math.sin(angulo_rad)) / 9.8
    return tiempo_vuelo

def calcular_distancia_maxima(velocidad_inicial, angulo):
    angulo_rad = math.radians(angulo)
    distancia_maxima = (velocidad_inicial ** 2 * math.sin(2 * angulo_rad)) / 9.8
    return distancia_maxima

velocidad = float(input("Ingrese la velocidad inicial (m/s): "))
angulo = float(input("Ingrese el ángulo de lanzamiento (en grados): "))

tiempo_vuelo = calcular_tiempo_vuelo(velocidad, angulo)
distancia_maxima = calcular_distancia_maxima(velocidad, angulo)

print("Tiempo de vuelo:", tiempo_vuelo, "segundos")
print("Distancia máxima:", distancia_maxima, "metros")