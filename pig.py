import random


def roll():
    return random.randint(1, 6)


# Ask for players
while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

max_score = 50
player_scores = [0 for _ in range(players)]

# GAME STARTS
while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\n--- Player", player_idx + 1, "turn ---")
        print("Total score:", player_scores[player_idx])

        current_score = 0

        while True:
            should_roll = input("Roll? (y) ")
            if should_roll.lower() != "y":
                break

            value = roll()
            print("You rolled:", value)

            if value == 1:
                print("Rolled a 1! Turn wasted.")
                current_score = 0
                break

            current_score += value
            print("Current turn score:", current_score)

        player_scores[player_idx] += current_score
        print("New total score:", player_scores[player_idx])

        if player_scores[player_idx] >= max_score:
            break

# GAME OVER
print("\n=======================")
print("       GAME OVER")
print("=======================\n")

# Show scoreboard
for i, score in enumerate(player_scores):
    print("Player", i + 1, "final score:", score)

# Winner
winner_index = player_scores.index(max(player_scores))
winner_score = max(player_scores)

print("\n🏆 Winner: Player", winner_index + 1, "with", winner_score, "points!")
