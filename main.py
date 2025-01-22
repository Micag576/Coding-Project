print("Welcome to my Survival Game Tracker. Determine if your players survived or not.")

def calc_avg(scores):
    total=sum(scores) 
    avg= total/len(scores)
    return avg

def status(avg):
    if avg  >=70:
        return "Escaped"
    else:
        return "Game Over"
    
def main():
    players = []
    num_of_players = int(input("How many Victims? "))
    for _ in range(num_of_players):
        name = input("Enter victim's name: ")
        games = []
        num_of_games = int(input(f"How many games did {name} play? "))
        for game in range(1, num_of_games + 1):
            score = float(input(f"Enter the score for game {game}: "))
            games.append(score)
        players.append({'name': name, 'scores': games})
    print(" \nSurvivor Results: ")
    for player in players:
        Av = calc_avg(player['scores'])
        stat =  status(Av)
        print(f"{player['name']} - Average Score: {Av:.2f} - Status : {stat}")

if __name__ == "__main__":
    main()
