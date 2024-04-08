def CHOOSE():
    t1 = input("PLAYER 1 THROW YOUR HAND: ").lower()
    if t1 not in ["rock","paper","scissors"]:
        print("ENTER FROM ROCK PAPER OR SCISSORS")
        CHOOSE()
    t2 = input("PLAYER 2 THROW YOUR HAND: ").lower()
    if t2 not in ["rock","paper","scissors"]:
        print("ENTER FROM ROCK PAPER OR SCISSORS")
        CHOOSE()
    if t1 == t2:
        print("SAME THROW AGAIN")
        CHOOSE()
    elif (t1 == "rock" and t2 == "paper") or (t1 == "paper" and t2 == "scissors") or (t1 == "scissors" and t2 == 'rock')  :
        print("P2 wins")
        exit()
    else:
        print("P1 wins")
CHOOSE()
