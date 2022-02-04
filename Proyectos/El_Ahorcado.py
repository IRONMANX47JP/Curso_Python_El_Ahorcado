import random
vidas = 10
palabra = random.choice(['Japón','India','China','Kazajistán','Armenia','Turquia','Serbia','Rusia','Francia','Alemania','Bielorusia','Noruega','Suecia','Finlandia','Reino Unido','Estados Unidos','Mexico','Brazil','Panamá'])
palabra = palabra.upper()
letras = list(palabra)
letras_utilizadas = []
#print(letras)
print('-'*35,'Bienvenido a el Ahorcado','-'*35,)
while True:
    print('Ingresa una letra: ')
    
    Letra = input().upper()
    if Letra in letras_utilizadas:
        pass
    else:
        letras_utilizadas.append(Letra)
    print('Estas son las listas utilizadas '+ str(letras_utilizadas))
    if Letra in letras:
        print('Letra correcta')
    else:
        print('Letra incorrecta')
        vidas -=1
    print('te quedan '+str(vidas)+' vidas')
    palabra_actual=''
    for letra in palabra:
        if letra in letras_utilizadas:
            palabra_actual += ' '+letra+' '
        else:
            palabra_actual += ' - '
    print(palabra_actual)
    if vidas == 0:
        break
    if '-' in palabra_actual:
        continue
    else:
        break
print('-'*70)