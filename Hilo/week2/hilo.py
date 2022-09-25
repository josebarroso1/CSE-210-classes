
def main():
    import random
    
    """Construction of a new director
    an instance of director"""
    
    points= int(300)    
    cards=(random.randint(1,13))
    cards1=(random.randint(1,13))
    guessHilo=""
    do_updates()

    """Starting the game by display the card"""
    print(f"The card is: {cards} ")

    """The player guesses if the next one will be higher or lower."""
    guessHilo=input("Higher or lower? [h/l] ")

    """the next card is displayed."""
    print(f"Next card was: {cards1} ")

    #The player earns 100 points if they guessed correctly.
    if guessHilo=="h":
        if cards <= cards1:

            points= points + 100
            print(f"Your score is: {points} ")

    if guessHilo=="l":
        if cards >= cards1:

            points= points + 100
            print(f"Your score is: {points} ")
    
    #The player loses 75 points if they guessed incorrectly.
    if guessHilo=="h":
        if cards > cards1:

            points= points - 75
            print(f"Your score is: {points} ")

    if guessHilo=="l":
        if cards < cards1:

            points= points - 75
            print(f"Your score is: {points} ")

    update(points)
    #If a player reaches 0 points the game is over.
    if points == 0:
        print("Game over!")

    """Ask if they want to keep playing."""
    keep= input("Keep playing(yes/no)? ")
    if keep == "yes" or "y":
        main()
    else:
        print("Game over!")
    
    def do_updates(main):
        points="";
    #If a player decides not to play again the game is over.
    update(points)
main()


