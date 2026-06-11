import random

player = {
    "name": (input("Ingrese el nombre del jugador: ")),
    "health": 100,
    "attack": 0,
}

enemy = {
    "name": "Orc",
    "health": 100,
    "attack": 0,
}

def roll_damage():
    luck = random.randint(1, 100)
    if luck == 100:
        return 100
    if luck <= 5:
        return 0
    return random.randint(10, 20)

def roll_heal():
    amount = random.randint(10, 20)
    if random.randint(1, 100) == 100:
        return amount * 2, True
    return amount, False

def check_winner(player, enemy):
    if enemy["health"] <= 0:
        print(f"¡{player['name']} ha ganado! {enemy['name']} ha sido derrotado.")
        return True
    if player["health"] <= 0:
        print(f"¡{enemy['name']} ha ganado! {player['name']} ha sido derrotado.")
        return True
    return False

def battle(player, enemy):
    player["health"] = 100
    enemy["health"] = 100
    attempts = 0

    print("\n--- Simulación de batalla automática ---")

    while True:
        attempts += 1
        print(f"\n--- Turno {attempts} ---")
        attack(player, enemy)
        if check_winner(player, enemy):
            if enemy["health"] <= 0:
                print(f"¡{player['name']} ganó en {attempts} intentos!")
            return enemy["health"] <= 0
        heal(player)

def heal(player):
    amount, is_critical = roll_heal()
    player["health"] += amount
    if is_critical:
        print(f"¡Curación crítica! {player['name']} se ha curado {amount} puntos de vida (el doble de lo normal).")
    else:
        print(f"{player['name']} se ha curado {amount} puntos de vida.")
    print(f"{player['name']} ahora tiene {player['health']} puntos de vida.")
    return player["health"]

def attack(player, enemy):
    player_attack = roll_damage()
    enemy_attack = roll_damage()
    player["health"] = max(0, player["health"] - enemy_attack)
    enemy["health"] = max(0, enemy["health"] - player_attack)

    if player_attack == 100:
        print(f"¡Golpe de pura suerte! {player['name']} ataca a {enemy['name']} y le hace {player_attack} puntos de daño.")
    elif player_attack == 0:
        print(f"{player['name']} falla el ataque contra {enemy['name']}.")
    else:
        print(f"{player['name']} ataca a {enemy['name']} y le hace {player_attack} puntos de daño.")

    if enemy_attack == 100:
        print(f"¡Golpe de pura suerte! {enemy['name']} ataca a {player['name']} y le hace {enemy_attack} puntos de daño.")
    elif enemy_attack == 0:
        print(f"{enemy['name']} falla el ataque contra {player['name']}.")
    else:
        print(f"{enemy['name']} ataca a {player['name']} y le hace {enemy_attack} puntos de daño.")

    print(f"{player['name']} tiene {player['health']} puntos de vida.")
    print(f"{enemy['name']} tiene {enemy['health']} puntos de vida.")

def main():
    print("Bienvenido al simulador de batalla")
    while True:
        print("1. Atacar")
        print("2. Curar")
        print("3. Simular batalla")
        print("4. Salir")
        option = input("Seleccione una opción: ")
        if option == "1":
            attack(player, enemy)
            if check_winner(player, enemy):
                break
        elif option == "2":
            heal(player)
        elif option == "3":
            battle(player, enemy)
            break
        elif option == "4":
            print("Gracias por jugar")
            break

if __name__ == "__main__":
    main()
