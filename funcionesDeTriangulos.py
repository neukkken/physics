def calcular_seno(angulo, num_terminos):
    angulo_rad = angulo * (3.14159265358979323846 / 180)  # Convierte el ángulo a radianes
    seno = 0

    for n in range(num_terminos):
        termino = ((-1) ** n) * (angulo_rad ** (2 * n + 1)) / factorial(2 * n + 1)
        seno += termino

    return seno

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

angulo = 30  # Ángulo en grados
terminos = 50  # Número de términos en la serie de Taylor (mayor número, mayor precisión)

seno = calcular_seno(angulo, terminos)

print("El seno de", angulo, "grados es:", seno)
