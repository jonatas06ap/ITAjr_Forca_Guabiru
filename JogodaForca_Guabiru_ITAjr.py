import random
#Lendo o arquivo de palavras
with open ("Palavras.txt","r") as arquivo:
    palavras_disponiveis = arquivo.read()
    palavras_disponiveis = palavras_disponiveis.lower()
    palavras_disponiveis = palavras_disponiveis.replace(","," ")
    palavras_disponiveis = palavras_disponiveis.split()
    for palavra in palavras_disponiveis:
        if len(palavra) != 5:
            palavras_disponiveis.pop(palavras_disponiveis.index(palavra))
#Estatisticas Padrao
vitorias=0
derrotas=0
lances_em_vitorias=0
lances_em_derrotas=0
vidas_em_vitorias=0
palavras_usadas=[]

#Lendo o arquivo de estatisticas
with open("Estatisticas.txt", "r") as status:
    dados = status.read()
    dados = dados.split()
    if len(dados) >= 6:
        vitorias = int(dados[0])
        derrotas = int(dados[1])
        lances_em_vitorias = int(dados[2])
        lances_em_derrotas = int(dados[3])
        vidas_em_vitorias = int(dados[4])
        for palv in dados[5:]:
            palavras_usadas.append(palv)
vidas_padrao = 7
menu = "I"
while menu != "S":
    print ("Jogo da Forca - ITA jr - Guabiru")
    print(" Novo Jogo: 'J'\n Estatisticas: 'E'\n Opcoes: 'O'\n Sair: 'S'")
    menu = input()
    #Menu de Jogo
    if menu=="J":

        #Inicializacao
        print("-------------------------x-------------------------")
        print("\nNOVO JOGO\n")
        palavra_atual = random.choice(palavras_disponiveis)
        #print(palavra_atual)
        palavras_disponiveis.pop(palavras_disponiveis.index(palavra_atual))
        palavras_usadas.append(palavra_atual)
        palavras_usadas.sort()
        letras_disponiveis = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        letras_usadas=[]
        chutes = 0
        vidas = vidas_padrao

        #Chutes

        estado_do_jogo = 'em andamento'
        palavra_apresentada = "_____"
        while estado_do_jogo != 'finalizado':
            #Apresentacao
            print("-------------------------x-------------------------")
            print("Vidas: ", vidas)
            print("\n", palavra_apresentada, "\n")
            letras_usadas.sort()
            print("Letras chutadas: ", letras_usadas)
            chutes += 1
            #Escolha
            print("Escolha uma letra")
            letra = input()
            #Coerencia
            if letra in letras_disponiveis:
                #Catalogo
                letras_disponiveis.pop(letras_disponiveis.index(letra))
                letras_usadas.append(letra)
                #Analise
                if letra in palavra_atual:
                    print("\nChute correto\n")
                    #Indices Corretos
                    indices_corretos = []
                    lista_letras = list(palavra_atual)
                    while letra in lista_letras:
                        i = lista_letras.index(letra)
                        indices_corretos.append(i)
                        lista_letras[i] = 0
                    #Posicionamento da letra nos indices
                    lista_palavra_apresentado = list(palavra_apresentada)
                    for ind in indices_corretos:
                        lista_palavra_apresentado[ind] = letra
                    palavra_apresentada = "".join(lista_palavra_apresentado)
                else:
                    print("\nChute incorreto\n")
                    vidas -= 1
            else:
                print("\nLetra ja analisada\n")

            #Testes
            if palavra_atual==palavra_apresentada:
                print("-------------------------x-------------------------\n")
                print("PARABENS: A palavra é: ", palavra_atual, "\n")
                print("-------------------------x-------------------------\n")
                vitorias +=1
                lances_em_vitorias += chutes
                vidas_em_vitorias += vidas
                estado_do_jogo = 'finalizado'
            elif vidas == 0:
                print("-------------------------x-------------------------\n")
                print("Suas vidas acabaram :(, a palavra era: ,", palavra_atual, "\n")
                print("-------------------------x-------------------------\n")
                derrotas += 1
                lances_em_derrotas += chutes
                estado_do_jogo = 'finalizado'

    #Menu de Estatisticas

    elif menu=="E":
        #Estatisticas
        print("-------------------------x-------------------------")
        print("\nEstatisticas\n")
        print("-------------------------x-------------------------\n")
        print("Vitorias: ", vitorias)
        print("Derrotas: ", derrotas)
        if vitorias + derrotas != 0:
            print("Taxa de vitorias:", vitorias*100/(vitorias+derrotas), "%")
        else:
            print("Taxa de vitorias: Sem histórico")
        if vitorias != 0:
            print("Lances por vitoria: ", lances_em_vitorias/vitorias)
            print("Vidas por vitoria: ", vidas_em_vitorias / vitorias)
        else:
            print("Lances por vitoria: Sem historico")
            print("Vidas por vitoria: Sem historico")
        if derrotas != 0:
            print("Lances por derrota: ", lances_em_derrotas / derrotas)
        else:
            print("Lances por derrota: Sem historico")
        print('Palavras já jogadas: ')
        print(palavras_usadas)
        print("\n-------------------------x-------------------------\n")

    #Menu de Opcoes
    elif menu == "O":
        #Exibicao
        menu_de_opcoes="I"
        while menu_de_opcoes != "S":
            print("\n-------------------------x-------------------------\n")
            print("Dificuldade: 'D'\nPalavras Nao Jogadas: 'N'\nPalavras Jogadas: J\nAdicionar Palavra: A\nVoltar ao menu: 'S'")
            menu_de_opcoes = input()
            if menu_de_opcoes == "D":
                print("\n-------------------------x-------------------------\n")
                print("Vidas Iniciais: ", vidas_padrao,"\n")
                print("Selecione a dificuldade:")
                print("Trivial: 15 vidas, digite '1'")
                print("Facil: 10 vidas, digite '2'")
                print("Medio: 7 vidas, digite '3'")
                print("Dificil: 5 vidas, digite '4'")
                print("Impossivel: 3 vidas, digite '5'")
                print("Outra quantidade de vidas: digite '0'")
                modo = input()
                print("\n-------------------------x-------------------------\n")
                if modo == '1':
                    vidas_padrao = 15
                    print("Modo Trivial")
                elif modo == '2':
                    vidas_padrao = 10
                    print("Modo Facil")
                elif modo == '3':
                    vidas_padrao = 7
                    print("Modo Medio")
                elif modo == '4':
                    vidas_padrao = '5'
                    print("Modo Dificil")
                elif modo == '5':
                    vidas_padrao = 3
                    print("Modo Impossivel")
                elif modo == '0':
                    print("Digite o numero de vidas:")
                    vidas_padrao = input()
                    print("Agora o jogo comeca com ", vidas_padrao, " vidas")
            elif menu_de_opcoes == "N":
                print("\n-------------------------x-------------------------\n")
                print("Palavras nao jogadas:")
                print(palavras_disponiveis)
            elif menu_de_opcoes == "J":
                print("\n-------------------------x-------------------------\n")
                print("Palavras jogadas:")
                print(palavras_usadas)

            elif menu_de_opcoes == "A":
                print("\n-------------------------x-------------------------\n")
                print("Adicione uma nova palavra para joga-la futuramente: ")
                print("(Ela deve ter 5 letras e nao possuir acentos nem letras maiusculas)")
                nova = input()
                if len(nova) == 5:
                    print("\n-------------------------x-------------------------\n")
                    palavras_disponiveis.append(nova)
                    palavras_disponiveis.sort()
                    print("Palavra adicionada")
                else:
                    print("\n-------------------------x-------------------------\n")
                    print("(A palavra nao possui 5 digitos)")
            elif menu_de_opcoes == "S":
                print("\n-------------------------x-------------------------\n")
                print("Voltando ao menu")
                print("\n-------------------------x-------------------------\n")


    #Menu de Saida

    elif menu=="S":
        #Mensagem
        print("\n-------------------------x-------------------------\n")
        print("Obrigado por jogar")
        print("\n-------------------------x-------------------------\n")
        #Armazenando estatisticas
        with open("Estatisticas.txt","w") as status:
            status.write("{} {} {} {} {} ".format(vitorias,derrotas,lances_em_vitorias,lances_em_derrotas,vidas_em_vitorias))
            for palavra in palavras_usadas:
                status.write("{} ".format(palavra))
        with open("Palavras.txt","w") as arquivo:
            for palavra in palavras_disponiveis:
                arquivo.write("{} ".format(palavra))
