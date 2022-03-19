'''Nome: Wezelen Gomes dos Santos Junior
   curso: Analise e desenvolvimento de sistemas'''


#adicionando Bibliotecas
from random import choice

#criando os dados
p = '👟'
c = '🧠'
t = '💥'
verde = '🟩'
amarelo = '🟨'
vermelho = '🟥'
dado_verde = [c, p, c, p, c, t]
dado_amarelo = [c, t, p, c, t, p]
dado_vermelho = [t, c, t, p, t, p]
pote = []

#adicionando os 13 dados
def add_dado(pote):
    for dados in range(13):
        while len(pote) < 6:
            pote.append(dado_verde)
        while len(pote) < 10:
            pote.append(dado_amarelo)
        while len(pote) < 13:
            pote.append(dado_vermelho)
    return pote

#Inicianco jogo
print('Vamos jogar Zombie Dice!')

#criando Jogadores
jogadores = []
num_jogadores = 0

#quantidade de jogadores
while True:
    try:
        num_jogadores = int(input('digite a quantidade de jogadores: '))
        if num_jogadores > 1:
            print(f'A quantidade de jogadores sera de {num_jogadores}')
            break
        else:
            print('É necessario pelo menos 2 jogadores')
    except:
        print('Valor invalido')

#nomeando jogadores
for nomes in range(0, num_jogadores):
    jogador = str(input('Digite o nome do {}° jogador: '.format(nomes + 1)))
    contador = [jogador, ''] #para adicionar os pontos do jogador
    jogadores.append(contador)


pontuacao = 0
while pontuacao < 13:
    print('ninguem ganhou')
    for player in range(0, len(jogadores)):
        print(jogadores[player])
        #função para sortear dados
        pontos_rodada = ['', '', '']
        dados_na_mão = []
        dados_no_pote = add_dado(pote)
        passos = []
        while len(pontos_rodada[1]) <= 3:
            resultado = []
            cor_dados = []
            

            if len(pontos_rodada[1]) >= 3: #checa se o jogador ja levou 3 tiros na rodada
                print('o jogador tomou pelo menos 3 tiros')
                break
            print('deseja pegar os dados?')
            continuar = str(input('[S] [N]  ')).strip()
            

            if continuar in 'Ss':
                pass
            elif continuar in 'Nn':
                jogadores[player][1] += pontos_rodada[0] #ainda preciso configurar para mais jogadores   ########
                break


            if len(dados_no_pote) + len(passos) > 3: #checa se ainda é possivel ter 3 dados para jogar
                #sorteia dados até completar 3 na mão
                for pegar_dados in range(0, 3):
                    if len(passos) > 0:
                        for r in range(0, len(passos)):
                            dados_na_mão.append(passos[0])
                            passos.remove(passos[0])
                    else:
                        dados_na_mão.append(choice(dados_no_pote))
                    #acumulando a cor dos 3 dados
                    if dados_na_mão[pegar_dados] == dado_vermelho:
                        cor_dados.append(vermelho)
                    elif dados_na_mão[pegar_dados] == dado_amarelo:
                        cor_dados.append(amarelo)
                    elif dados_na_mão[pegar_dados] == dado_verde:
                        cor_dados.append(verde)
                    try:
                        dados_no_pote.remove(dados_na_mão[pegar_dados])
                    except:
                        pass
                print(f'você pegou os dados: {cor_dados[0]} {cor_dados[1]} {cor_dados[2]}')        
            else: #quando a quantidade de dasos não soma 3 dados, interrompe o ciclo e soma os pontos ao jogador
                print('não a mais dados suficientes para uma nova jogada')
                jogadores[player][1] += pontos_rodada[0] #ainda preciso configurar para mais jogadores   ########
                break


            jogar = str(input('precione enter para rolar os dados'))
            for jogar_dados in range(0, 3): #roda os 3 dados sorteados e adiciona soma os resultados nos pontos da rodada
                resultado.append(choice(dados_na_mão[0]))    
                if resultado[jogar_dados] == c:
                    pontos_rodada[0] += c
                elif resultado[jogar_dados] == t:
                    pontos_rodada[1] += t
                else:
                    pontos_rodada[2] += p
                    passos.append(dados_na_mão[0])
                dados_na_mão.remove(dados_na_mão[0])


            print(f'{cor_dados[0]} → {resultado[0]}\n{cor_dados[1]} → {resultado[1]}\n{cor_dados[2]} → {resultado[2]}')
            print(pontos_rodada)
        

        print(f'{jogadores[player][0]} comeu "{len(jogadores[player][1])}"') #ainda preciso configurar para mais jogadores   ########

    if pontuacao < len(jogadores[player][1]):
        pontuacao = len(jogadores[player][1])

print('resultado')
for jogador in jogadores:
    print(f'{jogador[0]} conseguiu {jogador[1]}')
    if len(jogador[1]) == pontuacao:
        print('vencedor')
