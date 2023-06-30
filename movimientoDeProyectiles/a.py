#TRABAJO FISISCA


def rc (num):

      return num**0.5

def sin (num):

      return rc(2)/2

def cos (num):

      return  rc(2)/2

print ("para saber la velocidad horizontal se debe ingresar la inicial por el angulo")
print ("")

veloini = float(input ("Inggresa la v. inicial: "))
print ("")
print ("la velocidad inicial es: ",veloini," m/s")
print ("")


grados = float(input ("Inggresa la los grados de inclinación: "))
print ("")
print ("llos grados de inclinación es: ",grados,"°")
print ("")


vx = (veloini * (cos(45)))
print ("")
print ("la velocidad horizontal es: ",vx," m/s")
print ("")



vy = (veloini * (sin(45)))
print ("")
print ("la velocidad vertical es: ",vy," m/s")
print ("")

g = 9.8
print ("teniendo en cuenta que la gravedad vale ",g,"m/s^2")
print ("")
tv = (2*vy)/g

print ("y por ende el tiempo de vuelo sería: ",tv,"s")
print ("")

Am = (vy**2)/(2*g)

print ("y la altura maxima seria: ",Am,"m" )
print ("")

ah= vx*tv

print ("y el alcance horizontal sería: ",ah,"m")
print ("")



