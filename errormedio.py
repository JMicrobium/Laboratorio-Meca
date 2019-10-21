from math import pow
deltasABC=[50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]

tiemposA=[0.0116, 0.0113, 0.0115, 0.0113, 0.0113, 0.0112, 0.0111, 0.0109, 0.0103, 0.0098, 0.0094, 0.0089, 0.0085, 0.0087, 0.0086, 0.0085, 0.0083, 0.0085, 0.0085, 0.0090, 0.0085 ,0.0086, 0.0088, 0.0089, 0.0080, 0.0080, 0.0082, 0.0081, 0.0081, 0.0083, 0.0076, 0.0074, 0.0073, 0.0072, 0.0071, 0.0071, 0.0071, 0.0072, 0.0070, 0.0071, 0.0070, 0.0069, 0.0068, 0.0067, 0.0067, 0.0067, 0.0066, 0.0066, 0.0066, 0.0066, 0.0065, 0.0066, 0.0065, 0.0064, 0.0064, 0.0062, 0.0062, 0.0061, 0.0060, 0.0060, 0.0060]
tiemposB=[ 0.0088, 0.0086, 0.0086, 0.0087, 0.0087, 0.0082, 0.0083, 0.0079, 0.0078, 0.0079, 0.0078, 0.0077, 0.0078, 0.0076, 0.0073, 0.0074, 0.0072, 0.0072, 0.0070, 0.0068, 0.0067, 0.0066, 0.0066, 0.0066, 0.0066, 0.0065, 0.0064, 0.0063, 0.0062, 0.0065, 0.0063, 0.0057, 0.0053, 0.0059, 0.0057, 0.0055, 0.0055, 0.0053, 0.0054, 0.0053, 0.0054, 0.0055, 0.0052, 0.0054, 0.0054, 0.0055, 0.0055, 0.0058, 0.0057, 0.0056, 0.0058, 0.0057, 0.0054, 0.0052, 0.0052, 0.0052, 0.0050, 0.0057, 0.0055, 0.0052, 0.0054]
tiemposC=[0.0124, 0.0120, 0.0118, 0.0111, 0.0109, 0.0107, 0.0102, 0.0100, 0.0091, 0.0087, 0.0087, 0.0087, 0.0084, 0.0082, 0.0081, 0.0081, 0.0082, 0.0076, 0.0076, 0.0080, 0.0079, 0.0075, 0.0073, 0.0073, 0.0071, 0.0071, 0.0072, 0.0070, 0.0069, 0.0066, 0.0066, 0.0066, 0.0063, 0.0063, 0.0064, 0.0063, 0.0062, 0.0062, 0.0061, 0.0060, 0.0061, 0.0060, 0.0059, 0.0059, 0.0058, 0.0058, 0.0058, 0.0057, 0.0056, 0.0057, 0.0056, 0.0055, 0.0055, 0.0056, 0.0053, 0.0053, 0.0054, 0.0054, 0.0053, 0.0052, 0.0051]

d=(1.5)

velocidadesA=[(d/i) for i in tiemposA]
velocidadesB=[(d/i) for i in tiemposB]
velocidadesC=[(d/i) for i in tiemposC]

s=0
l=0

A=[(i-20) for i in deltasABC]
s=sum(A)
B=[(i**2) for i in A]
l=sum(B)
f=sum(velocidadesA)
g=sum(velocidadesB)
h=sum(velocidadesC)

Q=[(i*j) for i,j in zip(A,velocidadesA)]
q=sum(Q)
W=[(i*j) for i,j in zip(A,velocidadesB)]
w=sum(W)
E=[(i*j) for i,j in zip(A,velocidadesC)]
e=sum(E)

"alpha"

a0=(((s*q)-(l*f)))/((s**2)-(61*(l)))

a1=((s*f)-(61*q))/((s**2)-(61*l))

"beta"

b0=((s*w)-(l*g))/(((s**2)-(61*l)))

b1=((s*g)-(61*w))/((s**2)-(61*l))

"Gammma"

c0=((s*e)-(l*h))/((s**2)-(61*l))

c1=((s*h)-(61*e))/((s**2)-(61*l))
#de aqui hacia arriba es copia de "ecuaciones de regresion"

"deltas"

al= [(a0+(a1*x)-y) for x,y in zip(A,velocidadesA)]#error entre el ajuste y los datos
bl= [(b0+(b1*x)-y) for x,y in zip(A,velocidadesB)]#error entre el ajuste y los datos
cl= [(c0+(c1*x)-y) for x,y in zip(A,velocidadesC)]#error entre el ajuste y los datos


Al=[(i**2) for i in al]#valores de las listas al cuadrado
Bl=[(i**2) for i in bl]#valores de las listas al cuadrado
Cl=[(i**2) for i in cl]#valores de las listas al cuadrado

As=0
Bs=0
Cs=0

As=sum(Al)#sumatoria de los valores al cuadrado
Bs=sum(Bl)#sumatoria de los valores al cuadrado
Cs=sum(Cl)#sumatoria de los valores al cuadrado

af=(As/60)**(1/2)
bf=(Bs/60)**(1/2)
cf=(Cs/60)**(1/2)

print(af,bf,cf)#correción lista
