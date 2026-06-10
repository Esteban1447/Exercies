player = {
    "name": (input("Ingrese el nombre del jugador: ")),
    "health": 100,
    "attack":20,
          }

enemy = {
    "name": "Orc",
    "health": 100,
    "attack": 15,
}

def battle(player, enemy):
    while player["health"] > 0 and enemy["health"] > 0:

        player["health"] -= enemy["attack"]
        enemy["health"] -= player["attack"]

    if player["health"] <= 0 and enemy["health"] <= 0:
        print("¡Es un empate!")
    elif player["health"] <= 0:
        print(f"{enemy['name']} ha ganado la batalla.")
    else:
        print(f"{player['name']} ha ganado la batalla.")
    


def main():
    battle(player, enemy)

if __name__ == "__main__":
    main()