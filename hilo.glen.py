# Card game where player guesses if next card will be higher or lower

# Set starting points to 300
points = 300

# Loop while player has more than 0 points
while points > 0:

    # Get current card
    current_card = int(input("The card is: "))

    # Get player guess for next card
    guess = input("Higher or lower? (h/l): ")

    # Get next card
    next_card = int(input("Next card was: "))

    # If player guessed correctly, award 100 points
    if (guess == "h" and next_card > current_card) or \
            (guess == "l" and next_card < current_card):
        print("You guessed correctly!")
        points += 100

    # Otherwise player guessed incorrectly, deduct 75 points
    else:
        print("You guessed incorrectly...")
        points -= 75

    # Print current points
    print("Your score is:", str(points))

    # Check if player wants to keep playing
    keep_playing = input("Play again? (y/n): ")

    # If player does not want to keep playing, end game
    if keep_playing != "y":
        print("Thanks for playing!")
        break

