import random

# Score
scpu1 = 0
scpu2 = 0
scpu3 = 0
spl1 = 0
spl2 = 0
spl3 = 0

verification = True
moves = ["Rock", "Paper", "Scissors"]

# Menu
game_mode = int(input("Choose a game mode: CPU X CPU(1), Player x Player(2), Player x CPU(3): "))
while verification:

    # CPU vs CPU
    if game_mode == 1:
        cpu1 = random.choice(moves)
        cpu2 = random.choice(moves)
        print("-----------------------------------")
        print("JO \nKEN \nPO")
        print("-----------------------------------")
        print("CPU 1 choose:", cpu1)
        print("CPU 2 choose:", cpu2)

        # CPU 1 chooses rock

        if cpu1 == "Rock" and cpu2 == "Rock":
            print("Draw")
        elif cpu1 == "Rock" and cpu2 == "Paper":
            print("CPU 2 Wins!")
            scpu2 += 1
        elif cpu1 == "Rock" and cpu2 == "Scissors":
            print("CPU 1 Wins!")
            scpu2 += 1

        # CPU 1 chooses paper
    
        elif cpu1 == "Paper" and cpu2 == "Rock":
            print("CPU 1 Wins!")
            scpu1 += 1
        elif cpu1 == "Paper" and cpu2 == "Paper":
            print("Draw")
        elif cpu1 == "Paper" and cpu2 == "Scissors":
            print("CPU 2 Wins!")
            scpu2 += 1

        # CPU 1 chooses scissors

        elif cpu1 == "Scissors" and cpu2 == "Rock":
            print("CPU 2 Wins!")
            scpu2 += 1
        elif cpu1 == "Scissors" and cpu2 == "Paper":
            print("CPU 1 Wins!")
            scpu1 += 1
        elif cpu1 == "Scissors" and cpu2 == "Scissors":
            print("Draw")

    # Player vs Player

    elif game_mode == 2:
        player1_action = input("Player 1 Turn \nEnter a choice: Rock, Paper or Scissors: ")
        player2_action = input("Player 2 Turn \nEnter a choice: Rock, Paper or Scissors: ")
        print("-----------------------------------")
        print("JO \nKEN \nPO")
        print("-----------------------------------")
        print("Player 1 choose: ", player1_action)
        print("Player 2 choose: ", player2_action)

        # Player 2 chooses rock

        if player1_action == "Rock" and player2_action == "Rock":
            print("Draw")
        elif player1_action == "Paper" and player2_action == "Rock":
            print("Player 1 Wins!")
            spl1 += 1
        elif player1_action == "Scissors" and player2_action == "Rock":
            print("Player 2 Wins!")
            spl2 += 1

        # Player 2 chooses paper

        if player1_action == "Rock" and player2_action == "Paper":
            print("Player 2 Wins!")
            spl2 += 1
        elif player1_action == "Paper" and player2_action == "Paper":
            print("Draw")
        elif player1_action == "Scissors" and player2_action == "Paper":
            print("Player 1 Wins!")
            spl1 += 1

        # Player 2 chooses scissors

        if player1_action == "Rock" and player2_action == "Scissors":
            print("Player 1 Wins!")
            spl1 += 1
        elif player1_action == "Paper" and player2_action == "Scissors":
            print("Player 2 Wins!")
            spl2 += 1
        elif player1_action == "Scissors" and player2_action == "Scissors":
            print("Draw")

    # Player vs CPU

    else:
        cpu3 = random.choice(moves)
        player3_action = input("Enter a choice: Rock, Paper or Scissors: ")
        print("-----------------------------------")
        print("JO \nKEN \nPO")
        print("-----------------------------------")
        print("CPU chose:", cpu3)
        print("You chose:", player3_action)

        # Player chooses rock

        if cpu3 == "Rock" and player3_action == "Rock":
            print("Draw")
        elif cpu3 == "Paper" and player3_action == "Rock":
            print("You lose")
            scpu3 += 1
        elif cpu3 == "Scissors" and player3_action == "Rock":
            print("You win!")
            spl3 += 1

        # Player chooses paper

        if cpu3 == "Rock" and player3_action == "Paper":
            print("You win!")
            spl3 += 1
        elif cpu3 == "Paper" and player3_action == "Paper":
            print("Draw")
        elif cpu3 == "Scissors" and player3_action == "Paper":
            print("You lose")
            scpu3 += 1

        # Player chooses scissors

        if cpu3 == "Rock" and player3_action == "Scissors":
            print("You lose")
            scpu3 += 1
        elif cpu3 == "Paper" and player3_action == "Scissors":
            print("You win!")
            spl3 += 1
        elif cpu3 == "Scissors" and player3_action == "Scissors":
            print("Draw")

    # Play again

    play_again = int(input("Play again? Yes(1) No(2): "))
    print1 = 0
    print2 = 0
    if play_again == 1:
        verification = True
    else:
        if game_mode == 1:
            print1 = scpu1
            print2 = scpu2
        elif game_mode == 2:
            print1 = spl1
            print2 = spl2
        else:
            print1 = spl3
            print2 = scpu3
        print("-----------------------------------\nThanks for playing \nScoreboard: User 1: {0} / User 2: {1} ".format(print1, print2))
        verification = False