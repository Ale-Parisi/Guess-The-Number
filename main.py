import art
import random
print(art.logo)
print("Bienvenido/a al maravilloso Adivinator!")
print("Estoy pensando en un numero entre 1 y 100.")
chosen_one = random.choice(range(1,100))
print(f"Me dijeron que quizas el numero correcto sea {chosen_one}")

end_game = False
turnos_restantes = 0
guess_number = 0

def difficulty(turnos):
    difficulty = input("Selecciona tu dificultad escribiendo 'facil' o 'dificil': ")
    if difficulty == 'facil':
        turnos = 10
    elif difficulty == 'dificil':
        turnos = 5
    return turnos

turnos_restantes = difficulty(turnos_restantes)

while end_game != True: 
    print(f"Tienes {turnos_restantes} turnos restantes para adivinar el numero.")
    guess_number = int(input("Ingresa un numero: "))
    if chosen_one == guess_number:
        print(f"Felicitaciones, adivinaste! El numero elegido era {chosen_one}")
        end_game = True
    elif guess_number < chosen_one:
        print("El numero elegido es muy bajo.")
        turnos_restantes -= 1
    elif guess_number > chosen_one:
        print("El numero elegido es muy alto.")
        turnos_restantes -= 1
    if turnos_restantes == 0:
        print("Te quedaste sin turnos, perdiste =(")
        print(f"El numero correcto era {chosen_one}")
        end_game = True
    elif turnos_restantes > 0 and end_game != True:
        print("Intenta adivinar de nuevo.")