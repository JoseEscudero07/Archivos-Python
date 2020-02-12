i=1

dato = int(input("Digite un valor: "))
suma_notas=0
while i<=dato:
    nota = float(input("Digite su nota Nº {0}:".format(i)))
    suma_notas+=nota
    i+=1
print("el promedio es: ",suma_notas/dato)
