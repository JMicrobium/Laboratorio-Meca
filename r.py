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
z=0
x=0

A=[(i-20) for i in deltasABC]
s=(sum(A))/(61)#promedio de dist
l=(sum(velocidadesA))/(61)#promedio de vA
z=(sum(velocidadesB))/(61)#promedio de Vb
x=(sum(velocidadesC))/(61)#promedio de Vc

a=0
s=0
d=0
f=0

Q=[(i-s) for i in A]
W=[(i-l) for i in velocidadesA]
E=[(i-z) for i in velocidadesB]
R=[(i-x) for i in velocidadesC]

a=sum(Q)#suma de valores-promedio distancia
s=sum(W)#suma de valores-promedio A
d=sum(E)#suma de valores-promedio velocidades B
f=sum(R)#suma de valores-promedio C

rA=(((a)*(s))**(2))/((a**2)*(s**2))
rB=(((a)*(d))**(2))/((a**2)*(d**2))
rC=(((a)*(f))**(2))/((a**2)*(f**2))
print(rA,rB,rC)#correción lista