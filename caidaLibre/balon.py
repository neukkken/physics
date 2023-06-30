def calcular_t_caída(h):
    g = 9.8 
    t =((2 * h / g))
    return t

h = float(input("Digite la altura para saber el tiempo en el que toca el suelo: "))


tiempo_caída = calcular_t_caída(h)

print("El balón tarda ",tiempo_caída," segundos en tocar el suelo.")


