import random
pc1 = 0
pc2 = 0
pc3 = 0
pl1 = 0
pl2 = 0
pl3 = 0
verificacao = True
lista1 = ["Pedra", "Papel", "Tesoura"]

# Menu
modo = int(input("Escolha o modo de jogo: PC X PC(1), Player x Player(2), Player x PC(3): "))
while verificacao:

    # PC vs PC
    if modo == 1:
        computador1 = random.choice(lista1)
        computador2 = random.choice(lista1)
        print("-----------------------------------")
        print("JO \nKEN \nPO")
        print("-----------------------------------")
        print("O computador 1 jogou:", computador1)
        print("O computador 2 jogou:", computador2)

        # PC Jogando Pedra

        if computador1 == "Pedra" and computador2 == "Pedra":
            print("Empatou")
        elif computador1 == "Pedra" and computador2 == "Papel":
            print("Vitória do computador 2")
            pc2 += 1
        elif computador1 == "Pedra" and computador2 == "Tesoura":
            print("Vitória do computador 1")
            pc1 += 1

        # PC Jogando Papel
    
        elif computador1 == "Papel" and computador2 == "Pedra":
            print("Vitória do computador 1")
            pc1 += 1
        elif computador1 == "Papel" and computador2 == "Papel":
            print("Empatou")
        elif computador1 == "Papel" and computador2 == "Tesoura":
            print("Vitória do computador 2")
            pc2 += 1

        # PC Jogando Tesoura

        elif computador1 == "Tesoura" and computador2 == "Pedra":
            print("Vitória do computador 2")
            pc2 += 1
        elif computador1 == "Tesoura" and computador2 == "Papel":
            print("Vitória do computador 1")
            pc1 += 1
        else:
            print("Empatou")

    # Player vs Player

    elif modo == 2:
        jogada1 = input("Turno do Jogador 1 \nDigite a sua jogada: Pedra, Papel ou Tesoura: ")
        jogada2 = input("Turno do Jogador 2 \nDigite a sua jogada: Pedra, Papel ou Tesoura: ")
        print("-----------------------------------")
        print("JO \nKEN \nPO")
        print("-----------------------------------")
        print("O jogador 1 jogou: ", jogada1)
        print("O jogador 2 jogou: ", jogada2)

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
        print("-----------------------------------\nObrigado por jogar \nPlacar Final: Usuário 1: {0} / Usuário 2: {1} ".format(print1, print2))
        verificacao = False