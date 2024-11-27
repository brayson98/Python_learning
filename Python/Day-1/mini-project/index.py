import random

def play():
    score_1 = 0  # Player 1's score
    score_2 = 0  # Player 2's score
    current_player = 1  # Tracks the current player (1 or 2)
    player_1_done = False  # Tracks if Player 1 has completed their turn
    player_2_done = False  # Tracks if Player 2 has completed their turn
    
    while not (player_1_done and player_2_done):
        print(f"\nPlayer {current_player}'s turn:")
        
        # Get the current player's decision
        dice_decision = input("Do you want to roll the dice? (Yes/No): ").strip().lower()
        
        if dice_decision == "yes":
            result = random.randint(1, 6)
            print(f"Player {current_player} rolled a {result}.")
            
            if result == 1:
                print(f"Unlucky! Player {current_player} rolled a 1. Turn is over, and score resets to 0.")
                if current_player == 1:
                    score_1 = 0
                else:
                    score_2 = 0
                
                # Mark the player's turn as done and switch to the other player
                if current_player == 1:
                    player_1_done = True
                    current_player = 2
                else:
                    player_2_done = True
                    current_player = 1
            else:
                if current_player == 1:
                    score_1 += result
                    print(f"Player 1's current score: {score_1}")
                else:
                    score_2 += result
                    print(f"Player 2's current score: {score_2}")
        elif dice_decision == "no":
            print(f"Player {current_player} has ended their turn.")
            # Mark the player's turn as done and switch to the other player
            if current_player == 1:
                player_1_done = True
                current_player = 2
            else:
                player_2_done = True
                current_player = 1
        else:
            print("Invalid input. Please type 'Yes' or 'No'.")
    
    # End of game: Compare scores and declare the winner
    print("\nGame over!")
    print(f"Player 1's final score: {score_1}")
    print(f"Player 2's final score: {score_2}")
    if score_1 > score_2:
        print("Player 1 wins!")
    elif score_2 > score_1:
        print("Player 2 wins!")
    else:
        print("It's a tie!")

# Start the game
play()
