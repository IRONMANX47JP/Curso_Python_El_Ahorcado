import random
opciones = ['Piedra','Papel','Tijeras']
kurva = random.choice(opciones)
JPOption = input('Elija una opcion: ')
print('La computadora eligio: '+ kurva)
if JPOption == kurva:
    print('Empate!')
elif kurva == 'Piedra' and JPOption == 'Papel':
    print('El Jugador Gana!')
elif kurva == 'Piedra' and JPOption == 'Tijeras':
    print('La computadora Gana!')
elif kurva == 'Tijeras' and JPOption == 'Piedra':
    print('El Jugador Gana!')
elif kurva == 'Tijeras' and JPOption == 'Papel':
    print('La computadora Gana!')
elif kurva == 'Tijeras' and JPOption == 'Piedra':
    print('El Jugador Gana!')
elif kurva == 'Papel' and JPOption == 'Piedra':
    print('La computadora Gana!')
elif kurva == 'Papel' and JPOption == 'Tijeras':
    print('El Jugador Gana!')
print('Gracias por Jugar!')