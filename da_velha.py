import os 
#os: operating system
#vai verificar se o nome de usuário já existe nos arquivos
#____________________________________________________________________

#OBSERVAÇÕES GERAIS DO CÓDIGO

#preciso criar algumas funções principais, 4 serão as opções do menu
#criar player, apagar player, histórico player e começar partida
# e uma será a main, que é o menu em si

#dentro da função comecarPartida, usaremos as funções printjogo(), rodadasjogo(),
# vitoriaplayer() e derrotaplayer()


def criarPlayer(): #função p criar um jogador
    nome = input("Digite o nome do jogador: ")

    #caso o jogador já exista
    if os.path.isfile("./players/"+nome +".txt"):
        print("Esse nome de jogador já existe")

    else:
        arquivo = open("./players/"+nome +".txt", "w")
        arquivo.write("0\n")
        arquivo.write("0")
        arquivo.close()
        print("Jogador %s criado!"%nome)
        print("")

#_________________________________________________________________________
def apagarPlayer(): #função p excluir um jogador dos arquivos
    nome = input("Digite o nome do jogador a ser excluído: ")
    if os.path.isfile("./players/"+nome+".txt"):
        print("exluindo o jogador:", nome )
        os.remove("./players/"+nome+".txt")
        main() 
    else:
        print("esse jogador não existe")
        main()
#_________________________________________________________________________
def historicoPlayer(): #função p mostrar vitórias e derrotas do jogador
    nome = input("Nome do jogador: ")

    if os.path.isfile("./players/"+nome+".txt"):

        arquivo = open("./players/"+nome+".txt") #abrir
        historico = arquivo.readlines() #ler
        arquivo.close() #fechar
        vitorias = historico[0] #lendo pelo índice
        derrotas = historico[1]
        print("Vitórias: %s"%vitorias)
        print("Derrotas: %s"%derrotas)

    else:
        print("Jogador não existente!")

#_________________________________________________________________________

#VITÓRIA E DERROTA
#adicionando vitória ao histórico do jogador
def vitoriaPlayer(jogador):
                            
    arq = open("./players/"+jogador+".txt")
    hist = arq.readlines()
    win = int(hist[0])+1
    lose = int(hist[1])
    arq.close()

    arq = open("./players/"+jogador+".txt", "w")
    arq.write("%d\n%d "%(win,lose))
    arq.close()
    return arq

#adicionando derrota ao historico do jogador
def derrotaPlayer(jogador):
    arq = open("./players/"+jogador+".txt")
    hist = arq.readlines()
    lose = int(hist[0])+1
    win = int(hist[1])
    arq.close()

    arq = open("./players/"+jogador+".txt", "w")
    arq.write("%d\n%d "%(win,lose))
    arq.close()
    return arq

#_________________________________________________________________________

def printjogo(matriz):
        #criando o tabuleiro e conectando eles com os índices da matriz pelo {} e .format
    tabuleiro = """
 {} | {} | {} | {} | {}
---+---+---+---+---
 {} | {} | {} | {} | {}
---+---+---+---+---
 {} | {} | {} | {} | {}
---+---+---+---+---
 {} | {} | {} | {} | {}
---+---+---+---+---
 {} | {} | {} | {} | {}

    """.format(matriz[0][0],matriz[0][1],matriz[0][2],
    matriz[0][3],matriz[0][4],matriz[1][0],
    matriz[1][1],matriz[1][2],matriz[1][3],
    matriz[1][4],matriz[2][0],matriz[2][1],
    matriz[2][2],matriz[2][3],matriz[2][4],
    matriz[3][0],matriz[3][1],matriz[3][2],
    matriz[3][3],matriz[3][4],matriz[4][0],
    matriz[4][1],matriz[4][2],matriz[4][3],
    matriz[4][4])
    print(tabuleiro)

#__________________________________________________________________________________

#Essa função contém tudo que acontecerá durante a partida
def rodadasJogo(player1,player2):
    matriz = [] #chamar a matriz que está conectada ao tabuleiro da função acima
    for linha in range(5):
        linha = []
        for coluna in range(5):
            linha.append(" ")
        matriz.append(linha)

    #a variável que vai definir qual símbolo cada um vai usar (var símbolo)      
    símbolo = input("Por favor, %s, digite 1 para usar o X e 2 para usar a bolinha: "%player1)

    x = 0
    #1 pq é a opção do X, ou seja, se o player 1 desejar usar o x
    if símbolo == "1":
        printjogo(matriz)
        print("")
        print("Certo, então %s usará o X e %s usará a bolinha!"%(player1,player2))
        
        #o máximo que teremos são 25 jogadas (tamanho do tabuleiro)
        while x<=25:
            #se o número da jogada for par, é vez do jogador 1
            if x%2 ==0:
                print("")    
                print("Vez de %s"%player1)
                linha = int(input("Digite o índice da linha: "))
                coluna = int(input("Digite o índice da coluna: "))
                
                #caso as cordenadas digitadas não sejam válidas, alertar o user e repetir o loop
                if linha<0 or linha>4 or coluna<0 or linha>4:
                    print("")
                    print("Posição inexistente. Tente novamente com valores de 0 a 4")
                    x=x

                #confirmar se o slot está vazio. se estiver, preencher c/ X e continuar o while
                elif matriz[linha][coluna] == " ":
                    matriz[linha][coluna] = "X"
                    printjogo(matriz)
                    x+=1
                
                    #todas as possibilidades de vitória na horizontal
                    if (matriz[0][0]== "X" and matriz[0][1]== "X" and matriz[0][2]== "X" and matriz[0][3]== "X"
                    ) or (matriz[0][1]== "X" and matriz[0][2]== "X" and matriz[0][3]== "X" and matriz[0][4]== "X"
                    ) or (matriz[1][0]== "X" and matriz[1][1]== "X" and matriz[1][2]== "X" and matriz[1][3]== "X"
                    ) or (matriz[1][1]== "X" and matriz[1][2]== "X" and matriz[1][3]== "X" and matriz[1][4]== "X"
                    ) or (matriz[2][0]== "X" and matriz[2][1]== "X" and matriz[2][2]== "X" and matriz[2][3]== "X"
                    ) or (matriz[2][1]== "X" and matriz[2][2]== "X" and matriz[2][3]== "X" and matriz[2][4]== "X"
                    ) or (matriz[3][0]== "X" and matriz[3][1]== "X" and matriz[3][2]== "X" and matriz[3][3]== "X"
                    ) or (matriz[3][1]== "X" and matriz[3][2]== "X" and matriz[3][3]== "X" and matriz[3][4]== "X"
                    ) or (matriz[4][0]== "X" and matriz[4][1]== "X" and matriz[4][2]== "X" and matriz[4][3]== "X"
                    ) or (matriz[4][1]== "X" and matriz[4][2]== "X" and matriz[4][3]== "X" and matriz[4][4]== "X"):

                        print("")
                        print("%s ganhou!"%player1)
                        print("Adicionando vitória a %s e adicionando derrota a %s!"%(player1,player2))
                        print("")
                        
                        vitoriaPlayer(player1)
                        derrotaPlayer(player2)

                        break;
                    #todas as possibilidades de vitória na vertical
                    if(matriz[0][0]== "X" and matriz[1][0]== "X" and matriz[2][0]== "X" and matriz[3][0]== "X"
                    ) or (matriz[1][0]== "X" and matriz[2][0]== "X" and matriz[3][0]== "X" and matriz[4][0]== "X"
                    ) or (matriz[0][1]== "X" and matriz[1][1]== "X" and matriz[2][1]== "X" and matriz[3][1]== "X"
                    ) or (matriz[1][1]== "X" and matriz[2][1]== "X" and matriz[3][1]== "X" and matriz[4][1]== "X"
                    ) or (matriz[0][2]== "X" and matriz[1][2]== "X" and matriz[2][2]== "X" and matriz[3][2]== "X"
                    ) or (matriz[1][2]== "X" and matriz[2][2]== "X" and matriz[3][2]== "X" and matriz[4][2]== "X"
                    ) or (matriz[0][3]== "X" and matriz[1][3]== "X" and matriz[2][3]== "X" and matriz[3][3]== "X"
                    ) or (matriz[1][3]== "X" and matriz[2][3]== "X" and matriz[3][3]== "X" and matriz[4][3]== "X"
                    ) or (matriz[0][4]== "X" and matriz[1][4]== "X" and matriz[2][4]== "X" and matriz[3][4]== "X"
                    ) or (matriz[1][4]== "X" and matriz[2][4]== "X" and matriz[3][4]== "X" and matriz[4][4]== "X"):
                        
                        print("")
                        print("%s ganhou!"%player1)
                        print("Adicionando vitória a %s e adicionando derrota a %s!"%(player1,player2))
                        print("")

                        vitoriaPlayer(player1)
                        derrotaPlayer(player2)

                        break;

                    #todas as possibilidades de vitória na diagonal
                    if(matriz[0][0]== "X" and matriz[1][1]== "X" and matriz[2][2]== "X" and matriz[3][3]== "X"
                    ) or (matriz[1][1]== "X" and matriz[2][2]== "X" and matriz[3][3]== "X" and matriz[4][4]== "X"
                    ) or (matriz[1][0]== "X" and matriz[2][1]== "X" and matriz[3][2]== "X" and matriz[4][3]== "X"
                    ) or (matriz[0][1]== "X" and matriz[1][2]== "X" and matriz[2][3]== "X" and matriz[3][4]== "X"
                    ) or (matriz[0][4]== "X" and matriz[1][3]== "X" and matriz[2][2]== "X" and matriz[3][1]== "X"
                    ) or (matriz[1][3]== "X" and matriz[2][2]== "X" and matriz[3][1]== "X" and matriz[4][0]== "X"
                    ) or (matriz[1][4]== "X" and matriz[2][3]== "X" and matriz[3][2]== "X" and matriz[4][1]== "X"
                    ) or (matriz[0][3]== "X" and matriz[1][2]== "X" and matriz[2][1]== "X" and matriz[3][0]== "X"):
                        
                        print("")
                        print("%s ganhou!"%player1)
                        print("Adicionando vitória a %s e adicionando derrota a %s!"%(player1,player2))
                        print("")

                        vitoriaPlayer(player1)
                        derrotaPlayer(player2)

                        break;
                        
                        

                #caso o slot já tenha sido usado, alertar o player e repetir essa etapa do while
                
                else:
                    print("")
                    print("Posição Ocupada!")
                    x=x

                    
            #se for ímpar, vez do outro player (player2)
            elif x%2 !=0:
                print("")
                print("Vez de %s"%player2)
                linha = int(input("Digite o índice da linha: "))
                coluna = int(input("Digite o índice da coluna: "))

                #caso as cordenadas digitadas não sejam válidas, alertar o user e repetir o loop
                if linha<0 or linha>4 or coluna<0 or linha>4:
                    print("")
                    print("Posição inexistente. Tente novamente com valores de 0 a 4!")
                    x=x

                #conferir se está vazia para poder preencher com a bolinha
                elif matriz[linha][coluna] == " ":
                    matriz[linha][coluna] = "O"
                    printjogo(matriz)
                    x+=1

                    #todas as possibilidades de vitória na horizontal
                    if (matriz[0][0]== "O" and matriz[0][1]== "O" and matriz[0][2]== "O" and matriz[0][3]== "O"
                    ) or (matriz[0][1]== "O" and matriz[0][2]== "O" and matriz[0][3]== "O" and matriz[0][4]== "O"
                    ) or (matriz[1][0]== "O" and matriz[1][1]== "O" and matriz[1][2]== "O" and matriz[1][3]== "O"
                    ) or (matriz[1][1]== "O" and matriz[1][2]== "O" and matriz[1][3]== "O" and matriz[1][4]== "O"
                    ) or (matriz[2][0]== "O" and matriz[2][1]== "O" and matriz[2][2]== "O" and matriz[2][3]== "O"
                    ) or (matriz[2][1]== "O" and matriz[2][2]== "O" and matriz[2][3]== "O" and matriz[2][4]== "O"
                    ) or (matriz[3][0]== "O" and matriz[3][1]== "O" and matriz[3][2]== "O" and matriz[3][3]== "O"
                    ) or (matriz[3][1]== "O" and matriz[3][2]== "O" and matriz[3][3]== "O" and matriz[3][4]== "O"
                    ) or (matriz[4][0]== "O" and matriz[4][1]== "O" and matriz[4][2]== "O" and matriz[4][3]== "O"
                    ) or (matriz[4][1]== "O" and matriz[4][2]== "O" and matriz[4][3]== "O" and matriz[4][4]== "O"):
                        
                        print("")
                        print("%s ganhou!"%player2)
                        print("Adicionando vitória a %s e adicionando derrota a %s!"%(player2,player1))
                        print("")

                        vitoriaPlayer(player2)
                        derrotaPlayer(player1)

                        break;

                    #todas as possibilidades de vitória na vertical
                    if(matriz[0][0]== "O" and matriz[1][0]== "O" and matriz[2][0]== "O" and matriz[3][0]== "O"
                    ) or (matriz[1][0]== "O" and matriz[2][0]== "O" and matriz[3][0]== "O" and matriz[4][0]== "O"
                    ) or (matriz[0][1]== "O" and matriz[1][1]== "O" and matriz[2][1]== "O" and matriz[3][1]== "O"
                    ) or (matriz[1][1]== "O" and matriz[2][1]== "O" and matriz[3][1]== "O" and matriz[4][1]== "O"
                    ) or (matriz[0][2]== "O" and matriz[1][2]== "O" and matriz[2][2]== "O" and matriz[3][2]== "O"
                    ) or (matriz[1][2]== "O" and matriz[2][2]== "O" and matriz[3][2]== "O" and matriz[4][2]== "O"
                    ) or (matriz[0][3]== "O" and matriz[1][3]== "O" and matriz[2][3]== "O" and matriz[3][3]== "O"
                    ) or (matriz[1][3]== "O" and matriz[2][3]== "O" and matriz[3][3]== "O" and matriz[4][3]== "O"
                    ) or (matriz[0][4]== "O" and matriz[1][4]== "O" and matriz[2][4]== "O" and matriz[3][4]== "O"
                    ) or (matriz[1][4]== "O" and matriz[2][4]== "O" and matriz[3][4]== "O" and matriz[4][4]== "O"):
                        print("")
                        print("%s ganhou!"%player2)
                        print("Adicionando vitória a %s e adicionando derrota a %s!"%(player2,player1))
                        print("")

                        vitoriaPlayer(player2)
                        derrotaPlayer(player1)
                        break;

                    #todas as possibilidades de vitória na diagonal
                    if(matriz[0][0]== "O" and matriz[1][1]== "O" and matriz[2][2]== "O" and matriz[3][3]== "O"
                    ) or (matriz[1][1]== "O" and matriz[2][2]== "O" and matriz[3][3]== "O" and matriz[4][4]== "O"
                    ) or (matriz[1][0]== "O" and matriz[2][1]== "O" and matriz[3][2]== "O" and matriz[4][3]== "O"
                    ) or (matriz[0][1]== "O" and matriz[1][2]== "O" and matriz[2][3]== "O" and matriz[3][4]== "O"
                    ) or (matriz[0][4]== "O" and matriz[1][3]== "O" and matriz[2][2]== "O" and matriz[3][1]== "O"
                    ) or (matriz[1][3]== "O" and matriz[2][2]== "O" and matriz[3][1]== "O" and matriz[4][0]== "O"
                    ) or (matriz[1][4]== "O" and matriz[2][3]== "O" and matriz[3][2]== "O" and matriz[4][1]== "O"
                    ) or (matriz[0][3]== "O" and matriz[1][2]== "O" and matriz[2][1]== "O" and matriz[3][0]== "O"):
                        print("")
                        print("%s ganhou!"%player2)
                        print("Adicionando vitória a %s e adicionando derrota a %s!"%(player2,player1))
                        print("")
                        vitoriaPlayer(player2)
                        derrotaPlayer(player1)

                        break;

                    #se ninguém ganhar durante as 25, decretar empate
                    elif x==25:
                            print("")
                            print("Empatou!")
                            break; 
                    
                
                #se estiver cheia, manter o while "aqui" e alertar o user    
                else:
                    print("")
                    print("Posição Ocupada!")
                    x=x


    #mesma lógica aplicada no if acima
    #mas para o caso do jogador 1 decidir usar a bolinha
    #2 pq é a opção da bolinha
    elif símbolo == "2": 
        printjogo(matriz)
        print("")
        print("Certo, então %s usará o X e %s usará a bolinha!"%(player2,player1))


        #relembrando: 25 pq é o máximo de jogadas
        while x<=25:
            #vez do player 1 de jogar
            if x%2 ==0:
                print("")
                print("Vez de %s"%player1)
                linha = int(input("Digite o índice da linha: "))
                coluna = int(input("Digite o índice da coluna: "))

                #caso as cordenadas digitadas não sejam válidas, alertar o user e repetir o loop
                if linha<0 or linha>4 or coluna<0 or linha>4:
                    print("")
                    print("Posição inexistente. Tente novamente com valores de 0 a 4")
                    x=x

                #se o slot estiver vazio, preencher com a bolinha
                elif matriz[linha][coluna] == " ":
                    matriz[linha][coluna] = "O"
                    printjogo(matriz)
                    x+=1

                    #todas as possibilidades de vitória na horizontal
                    if (matriz[0][0]== "O" and matriz[0][1]== "O" and matriz[0][2]== "O" and matriz[0][3]== "O"
                    ) or (matriz[0][1]== "O" and matriz[0][2]== "O" and matriz[0][3]== "O" and matriz[0][4]== "O"
                    ) or (matriz[1][0]== "O" and matriz[1][1]== "O" and matriz[1][2]== "O" and matriz[1][3]== "O"
                    ) or (matriz[1][1]== "O" and matriz[1][2]== "O" and matriz[1][3]== "O" and matriz[1][4]== "O"
                    ) or (matriz[2][0]== "O" and matriz[2][1]== "O" and matriz[2][2]== "O" and matriz[2][3]== "O"
                    ) or (matriz[2][1]== "O" and matriz[2][2]== "O" and matriz[2][3]== "O" and matriz[2][4]== "O"
                    ) or (matriz[3][0]== "O" and matriz[3][1]== "O" and matriz[3][2]== "O" and matriz[3][3]== "O"
                    ) or (matriz[3][1]== "O" and matriz[3][2]== "O" and matriz[3][3]== "O" and matriz[3][4]== "O"
                    ) or (matriz[4][0]== "O" and matriz[4][1]== "O" and matriz[4][2]== "O" and matriz[4][3]== "O"
                    ) or (matriz[4][1]== "O" and matriz[4][2]== "O" and matriz[4][3]== "O" and matriz[4][4]== "O"):
                        
                        print("")
                        print("%s ganhou!"%player1)
                        print("Adicionando vitória a %s e adicionando derrota a %s!"%(player1,player2))
                        print("")

                        vitoriaPlayer(player1)
                        derrotaPlayer(player2)

                        break;

                    #todas as possibilidades de vitória na vertical
                    if(matriz[0][0]== "O" and matriz[1][0]== "O" and matriz[2][0]== "O" and matriz[3][0]== "O"
                    ) or (matriz[1][0]== "O" and matriz[2][0]== "O" and matriz[3][0]== "O" and matriz[4][0]== "O"
                    ) or (matriz[0][1]== "O" and matriz[1][1]== "O" and matriz[2][1]== "O" and matriz[3][1]== "O"
                    ) or (matriz[1][1]== "O" and matriz[2][1]== "O" and matriz[3][1]== "O" and matriz[4][1]== "O"
                    ) or (matriz[0][2]== "O" and matriz[1][2]== "O" and matriz[2][2]== "O" and matriz[3][2]== "O"
                    ) or (matriz[1][2]== "O" and matriz[2][2]== "O" and matriz[3][2]== "O" and matriz[4][2]== "O"
                    ) or (matriz[0][3]== "O" and matriz[1][3]== "O" and matriz[2][3]== "O" and matriz[3][3]== "O"
                    ) or (matriz[1][3]== "O" and matriz[2][3]== "O" and matriz[3][3]== "O" and matriz[4][3]== "O"
                    ) or (matriz[0][4]== "O" and matriz[1][4]== "O" and matriz[2][4]== "O" and matriz[3][4]== "O"
                    ) or (matriz[1][4]== "O" and matriz[2][4]== "O" and matriz[3][4]== "O" and matriz[4][4]== "O"):
                        
                        print("")
                        print("%s ganhou!"%player1)
                        print("Adicionando vitória a %s e adicionando derrota a %s!"%(player1,player2))
                        print("")

                        vitoriaPlayer(player1)
                        derrotaPlayer(player2)

                        break;

                    #todas as possibilidades de vitória na diagonal
                    if(matriz[0][0]== "O" and matriz[1][1]== "O" and matriz[2][2]== "O" and matriz[3][3]== "O"
                    ) or (matriz[1][1]== "O" and matriz[2][2]== "O" and matriz[3][3]== "O" and matriz[4][4]== "O"
                    ) or (matriz[1][0]== "O" and matriz[2][1]== "O" and matriz[3][2]== "O" and matriz[4][3]== "O"
                    ) or (matriz[0][1]== "O" and matriz[1][2]== "O" and matriz[2][3]== "O" and matriz[3][4]== "O"
                    ) or (matriz[0][4]== "O" and matriz[1][3]== "O" and matriz[2][2]== "O" and matriz[3][1]== "O"
                    ) or (matriz[1][3]== "O" and matriz[2][2]== "O" and matriz[3][1]== "O" and matriz[4][0]== "O"
                    ) or (matriz[1][4]== "O" and matriz[2][3]== "O" and matriz[3][2]== "O" and matriz[4][1]== "O"
                    ) or (matriz[0][3]== "O" and matriz[1][2]== "O" and matriz[2][1]== "O" and matriz[3][0]== "O"):
                        
                        print("")
                        print("%s ganhou!"%player1)
                        print("Adicionando vitória a %s e adicionando derrota a %s!"%(player1,player2))
                        print("")

                        vitoriaPlayer(player1)
                        derrotaPlayer(player2)

                        break;
                    elif x==25:
                        print("")
                        print("Empatou!")
                        break;   
                
                #se estiver ocupado, repetir essa etapa do while e alertar o usuário
                else:
                    print("")
                    print("Posição Ocupada!")
                    x=x

            #vez do player 2   
            elif x%2 !=0:
                print("")
                print("Vez de %s"%player2)
                linha = int(input("Digite o índice da linha: "))
                coluna = int(input("Digite o índice da coluna: "))

                #caso as cordenadas digitadas não sejam válidas, alertar o user e repetir o loop
                if linha<0 or linha>4 or coluna<0 or linha>4:
                    print("")
                    print("Posição inexistente. Tente novamente com valores de 0 a 4!")
                    x=x

                #relembrando: se tá vazio, preencher e avançar o x
                elif matriz[linha][coluna] == " ":
                    matriz[linha][coluna] ="X"
                    printjogo(matriz)
                    x+=1

                    #todas as possibilidades de vitória na horizontal
                    if (matriz[0][0]== "X" and matriz[0][1]== "X" and matriz[0][2]== "X" and matriz[0][3]== "X"
                    ) or (matriz[0][1]== "X" and matriz[0][2]== "X" and matriz[0][3]== "X" and matriz[0][4]== "X"
                    ) or (matriz[1][0]== "X" and matriz[1][1]== "X" and matriz[1][2]== "X" and matriz[1][3]== "X"
                    ) or (matriz[1][1]== "X" and matriz[1][2]== "X" and matriz[1][3]== "X" and matriz[1][4]== "X"
                    ) or (matriz[2][0]== "X" and matriz[2][1]== "X" and matriz[2][2]== "X" and matriz[2][3]== "X"
                    ) or (matriz[2][1]== "X" and matriz[2][2]== "X" and matriz[2][3]== "X" and matriz[2][4]== "X"
                    ) or (matriz[3][0]== "X" and matriz[3][1]== "X" and matriz[3][2]== "X" and matriz[3][3]== "X"
                    ) or (matriz[3][1]== "X" and matriz[3][2]== "X" and matriz[3][3]== "X" and matriz[3][4]== "X"
                    ) or (matriz[4][0]== "X" and matriz[4][1]== "X" and matriz[4][2]== "X" and matriz[4][3]== "X"
                    ) or (matriz[4][1]== "X" and matriz[4][2]== "X" and matriz[4][3]== "X" and matriz[4][4]== "X"):
                        
                        print("")
                        print("%s ganhou!"%player2)
                        print("Adicionando vitória a %s e adicionando derrota a %s!"%(player2,player1))
                        print("")

                        vitoriaPlayer(player2)
                        derrotaPlayer(player1)
                        break;

                    #todas as possibilidades de vitória na vertical
                    if(matriz[0][0]== "X" and matriz[1][0]== "X" and matriz[2][0]== "X" and matriz[3][0]== "X"
                    ) or (matriz[1][0]== "X" and matriz[2][0]== "X" and matriz[3][0]== "X" and matriz[4][0]== "X"
                    ) or (matriz[0][1]== "X" and matriz[1][1]== "X" and matriz[2][1]== "X" and matriz[3][1]== "X"
                    ) or (matriz[1][1]== "X" and matriz[2][1]== "X" and matriz[3][1]== "X" and matriz[4][1]== "X"
                    ) or (matriz[0][2]== "X" and matriz[1][2]== "X" and matriz[2][2]== "X" and matriz[3][2]== "X"
                    ) or (matriz[1][2]== "X" and matriz[2][2]== "X" and matriz[3][2]== "X" and matriz[4][2]== "X"
                    ) or (matriz[0][3]== "X" and matriz[1][3]== "X" and matriz[2][3]== "X" and matriz[3][3]== "X"
                    ) or (matriz[1][3]== "X" and matriz[2][3]== "X" and matriz[3][3]== "X" and matriz[4][3]== "X"
                    ) or (matriz[0][4]== "X" and matriz[1][4]== "X" and matriz[2][4]== "X" and matriz[3][4]== "X"
                    ) or (matriz[1][4]== "X" and matriz[2][4]== "X" and matriz[3][4]== "X" and matriz[4][4]== "X"):
                        print("")
                        print("%s ganhou!"%player2)
                        print("Adicionando vitória a %s e adicionando derrota a %s!"%(player2,player1))
                        print("")

                        vitoriaPlayer(player2)
                        derrotaPlayer(player1)
                        break;

                    #todas as possibilidades de vitória na diagonal
                    if(matriz[0][0]== "X" and matriz[1][1]== "X" and matriz[2][2]== "X" and matriz[3][3]== "X"
                    ) or (matriz[1][1]== "X" and matriz[2][2]== "X" and matriz[3][3]== "X" and matriz[4][4]== "X"
                    ) or (matriz[1][0]== "X" and matriz[2][1]== "X" and matriz[3][2]== "X" and matriz[4][3]== "X"
                    ) or (matriz[0][1]== "X" and matriz[1][2]== "X" and matriz[2][3]== "X" and matriz[3][4]== "X"
                    ) or (matriz[0][4]== "X" and matriz[1][3]== "X" and matriz[2][2]== "X" and matriz[3][1]== "X"
                    ) or (matriz[1][3]== "X" and matriz[2][2]== "X" and matriz[3][1]== "X" and matriz[4][0]== "X"
                    ) or (matriz[1][4]== "X" and matriz[2][3]== "X" and matriz[3][2]== "X" and matriz[4][1]== "X"
                    ) or (matriz[0][3]== "X" and matriz[1][2]== "X" and matriz[2][1]== "X" and matriz[3][0]== "X"):
                        
                        print("")
                        print("%s ganhou!"%player2)
                        print("Adicionando vitória a %s e adicionando derrota a %s!"%(player2,player1))
                        print("")

                        vitoriaPlayer(player2)
                        derrotaPlayer(player1)
                        break;

                    #se ninguém ganhar durante as 25, decretar empate
                elif x==25:
                    print("")
                    print("Empatou!")
                    break;                        

            #completando o if da ocupação de slot
            #se o espaço tá ocupado, não avançar o x e alertar o user
            else:
                print("")
                print("Posição Ocupada!")
                x=x

    #caso o player 1 digite qualquer coisa que não seja 1 (pro x) ou 2 ( pra bolinha):
    else:
        print("")
        print("Opção inválida!")

#__________________________________________________________________________________

#a função abaixo vai identificar os dois players, para depois executar o game
def comecarPartida():

    #digitar o player 1. verificar se existe nos arquivos. se existir, digitar o 2
    # em ambos, receber mensagem de erro caso o jogador não esteja nos arquivos

    player1 = input("Digite o nome do jogador 1: ")

    #verificar abaixo, se o "player1".txt existe no sistema operacional

    if os.path.isfile("./players/"+player1+".txt"):
        player2 = input("Digite o nome do jogador 2: ")
    
        #NO CENÁRIO IDEAL (2 PLAYERS EXISTENTES) O JOGO COMEÇA AQUI
        if os.path.isfile("./players/"+player2+".txt"):
            rodadasJogo(player1,player2)
  
        else:
            print("Jogador",player2 ,"não reconhecido.")

    #else que completa o if da verificação dos players
    #caso o player 1 não exista nos arquivos
    else:
        print("Jogador",player1 ,"não reconhecido.")
    

#_________________________________________________________________________
#menu
def main():
    while True:
         print(" _______________________________")
         print("|________|JOGO DA VELHA|________|")
         print("|_______________________________|")
         print("|_____________MENU______________|")
         print("| 1: Criar jogador              |")
         print("| 2: Exibir histórico do jogador|")
         print("| 3: Apagar jogador             |")
         print("| 4: Começar partida            |")
         print("|_______________________________|")

         #variável q vai armazenar a escolha do usuário no menu
         #de acordo com os números apresentados por mim no menu,
         #acontecerá aquilo que o usuário desejar

         um_a_quatro = input("Escolha uma das opções: ")

         if um_a_quatro =="1":
             criarPlayer()
        
         elif um_a_quatro =="2":
             historicoPlayer()
        
         elif um_a_quatro =="3":
             apagarPlayer()
        
         elif um_a_quatro =="4":
             comecarPartida()

main()
   