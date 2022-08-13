Beatles = []
print("Paso 1:", Beatles)

Beatles.append("Jhon Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")
print("Paso 2:", Beatles)

for i in range(2):
    Beatles.append(input("ingrese miembro: "))

print("Paso 3:", Beatles)

del Beatles[4]
del Beatles[3]
print("Paso 4:", Beatles)

Beatles.insert(0,"Ringo Starr")
print("Paso 5:", Beatles)


# probando la longitud de la lista
print("Los Fav", len(Beatles))

