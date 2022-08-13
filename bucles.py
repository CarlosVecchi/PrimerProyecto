# contador de numeros pares e impares
odd_numbers = 0
even_numbers = 0

number = int(input("numero o 0 para detener"))

while number != 0:
    if number % 2 == 1:
        odd_numbers += 1
    else:
        even_numbers += 1
    number = int(input("numero o 0 para detener"))
print ("cuenta de numeros impares:", odd_numbers)
print ("cuenta de numeros pares:", even_numbers)

# otro ejercicio (adivina el numero)
secret_number = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")
adivina = int(input("adivina el numero: "))
while adivina != secret_number:
    print(" JA JA estas atrapado en mi bucle")
    adivina = int(input("adivina el numero: "))

print(" bien hecho, eres libre")

# bucle for

for i in range(10):
    print("El valor de i es actualmente",i)

# bucle while y breka en if
# adivina la palabra

palabra_secreta = "chupacabra"

while True:
    palabra = input(" ingrese la palabra secreta: ")
    if palabra == "chupacabra":
        print("has dejado el bucle con exito")
        break
    else: print("vuelve a intentarlo!!!")


#come vocales

user_word = input("ingrese una palabra: ")
user_word = user_word.upper()

for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else: print(letter)


# hipotesis de collatz

c0= int(input("ingrese el numero: "))
pasos = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0/2
    else:
        c0 = 3 * c0 + 1
    pasos += 1
    print(int(c0))

print("los pasos: ", pasos)

