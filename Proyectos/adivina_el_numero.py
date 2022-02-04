import random 
intentos = 5
num = random.randint(1,10)
print('Bienvenido a adivina el numero!')
while True:
   
    print('Tienes '+str(intentos)+' intentos')
    print('Ingrese un numero')
    
    userNumber = int(input())
    if num == userNumber:
        print('Felizitaciones has Ganado!!')
        break
    else:
        print('Intentalo de nuevo')
        intentos -= 1
    if intentos == 0:
        print('Haz perdido')
        break
