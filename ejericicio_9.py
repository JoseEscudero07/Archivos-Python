edad = int(input("Digite su Edad: "))
  
if edad >= 5 and edad <=15:
    print("Es usted un niño")
elif edad >=16 and edad <=20:
    print("Es usted un Adolecente")
elif edad >=21 and edad <=30:
    print("Es usted un Joven")
elif edad >=31 and edad <=70:
    print("Es usted un Adulto Mayor")
elif edad >=71 and edad <=100:
    print("Esta usted en la vejez")
else:
    if edad > 100:
        print("es usted muy viejo")
    if edad < 5:
       print("es usted un Bebe")


