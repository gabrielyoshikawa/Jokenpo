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
gameMode = int(input("Choose a game mode: CPU X CPU(1), Player x Player(2), Player x CPU(3): "))
while verification:

    # CPU vs CPU
    if gameMode == 1:
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

        # CPU 1 chosses paper
    
        elif cpu1 == "Paper" and cpu2 == "Rock":
            print("CPU 1 Wins!")
            scpu1 += 1
        elif cpu1 == "Paper" and cpu2 == "Paper":
            print("Draw")
        elif cpu2 == "Paper" and cpu2 == "Scissors":
            print("CPU 2 Wins!")
            scpu2 += 1

        # CPU 1 chosses scissors

        elif cpu1 == "Scissors" and cpu2 == "Rock":
            print("CPU 2 Wins!")
            scpu2 += 1
        elif cpu2 == "Scissors" and cpu2 == "Paper":
            print("CPU 1 Wins!")
            scpu1 += 1
        else:
            print("Draw")

    # Player vs Player

    elif gameMode == 2:
        player1_action = input("Player 1 Turn \nDigite a sua jogada: Pedra, Papel ou Tesoura: ")
        player2_action = input("Player 2 Turn \nDigite a sua jogada: Pedra, Papel ou Tesoura: ")
        print("-----------------------------------")
        print("JO \nKEN \nPO")
        print("-----------------------------------")
        print("O jogador 1 jogou: ", player1_action)
        print("O jogador 2 jogou: ", player2_action)

        # Jogador1 Pedra

        if jogada1 == "Pedra" and jogada2 == "Pedra":
            print("Empatou")
        elif jogada1 == "Papel" and jogada2 == "Pedra":
            print("Vitória do jogador 1!")
            pl1 += 1
        elif jogada1 == "Tesoura" and jogada2 == "Pedra":
            print("Vitória do jogador 2!")
            pl2 += 1

        # Jogador1 Papel

        if jogada1 == "Pedra" and jogada2 == "Papel":
            print("Vitória do jogador 2!")
            pl2 += 1
        elif jogada1 == "Papel" and jogada2 == "Papel":
            print("Empatou")
        elif jogada1 == "Tesoura" and jogada2 == "Papel":
            print("Vitória do jogador 1")
            pl1 += 1

        # Jogador1 Tesoura

        if jogada1 == "Pedra" and jogada2 == "Tesoura":
            print("Vitória do jogador 1!")
            pl1 += 1
        elif jogada1 == "Papel" and jogada2 == "Tesoura":
            print("Vitória do jogador 2!")
            pl2 += 1
        elif jogada1 == "Tesoura" and jogada2 == "Tesoura":
            print("Empatou")

    # Player vs PC

    else:
        computador = random.choice(lista1)
        jogada = input("Digite a sua jogada: Pedra, Papel e Tesoura: ")
        print("-----------------------------------")
        print("JO \nKEN \nPO")
        print("-----------------------------------")
        print("O computador jogou:", computador)
        print("Você jogou:", jogada)

        # Jogador Pedra

        if computador == "Pedra" and jogada == "Pedra":
            print("Empatou")
        elif computador == "Papel" and jogada == "Pedra":
            print("Você perdeu")
            pc3 += 1
        elif computador == "Tesoura" and jogada == "Pedra":
            print("Você ganhou!")
            pl3 += 1

        # Jogador Papel

        if computador == "Pedra" and jogada == "Papel":
            print("Você ganhou!")
            pl3 += 1
        elif computador == "Papel" and jogada == "Papel":
            print("Empatou")
        elif computador == "Tesoura" and jogada == "Papel":
            print("Você perdeu")
            pc3 += 1

        # Jogador Tesoura

        if computador == "Pedra" and jogada == "Tesoura":
            print("Você perdeu")
            pc3 += 1
        elif computador == "Papel" and jogada == "Tesoura":
            print("Você ganhou!")
            pl3 += 1
        elif computador == "Tesoura" and jogada == "Tesoura":
            print("Empatou")

    # Encerramento

    continuar = int(input("Deseja jogar novamente? Sim(1) Não(2): "))
    print1 = 0
    print2 = 0
    if continuar == 1:
        verificacao = True
    else:
        if modo == 1:
            print1 = pc1
            print2 = pc2
        elif modo == 2:
            print1 = pl1
            print2 = pl2
        else:
            print1 = pl3
            print2 = pc3
        print("-----------------------------------\nThanks for playing \nScoreboard: User 1: {0} / User 2: {1} ".format(print1, print2))
        verificacao = False