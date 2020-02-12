#import random

from random import randint
elementos = ["uva","manzana","pera"]
print(elementos[:])
for i in elementos:
    print(i)

mi_Lista = []

for x in range(10):
    mi_Lista.append(randint(1,20))

print(mi_Lista[:])


