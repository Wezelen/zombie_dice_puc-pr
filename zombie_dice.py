#adicionando Bibliotecas
from random import choice
from time import sleep

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
for dados in range(13):
    while len(pote) < 6:
        pote.append(dado_verde)
    while len(pote) < 10:
        pote.append(dado_amarelo)
    while len(pote) < 13:
        pote.append(dado_vermelho)

#Inicianco jogo
print('Vamos jogar Zombie Dice!')

#criando Jogadores
jogadores = []
num_jogadores = 0

#quantidade de jogadores
while True:
    try:
        num_jogadores = int(input('digite a quantidade de jogadores:'))
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
    contador = [jogador, '']
    jogadores.append(contador)


#função para sortear dados
""" def sortear_dados(dado):
    pass """
pontos_rodada = ['', '', '']
while len(pontos_rodada[1]) <= 3:
    dados_no_pote = pote
    dados_na_mão = []
    cor_dados = [] #limpar antes do novo ciclo
    resultado = []
    passos = []
    
    if len(pontos_rodada[1]) >= 3:
        print('o jogador tomou pelo menos 3 tiros')
        break
    print('deseja continuar?')
    continuar = str(input('[S] [N]')).strip()
    if continuar in 'Ss':
        pass
    elif continuar in 'Nn':
        jogadores[0][1] += pontos_rodada[0] #########################
        break

    if len(dados_no_pote) + len(passos) > 3:
        for pegar_dados in range(0, 3 - len(passos)): #sorteia 3 dados do pote
            dados_na_mão.append(choice(dados_no_pote))
            #acumulando a cor dos 3 dados
            if dados_na_mão[pegar_dados] == dado_vermelho:
                cor_dados.append(vermelho)
            if dados_na_mão[pegar_dados] == dado_amarelo:
                cor_dados.append(amarelo)
            if dados_na_mão[pegar_dados] == dado_verde:
                cor_dados.append(verde)
            dados_no_pote.remove(dados_na_mão[pegar_dados])
        print(f'você pegou os dados: {cor_dados}')
        jogar = str(input('precione enter para rolar os dados'))
    else:
        print('não a mais dados suficientes para uma nova jogada')
        jogadores[0][1] += pontos_rodada[0]
        break

    
    for jogar_dados in range(0, 3 - len(passos)): #roda os 3 dados sorteados
        sorteado = choice(dados_na_mão)
        resultado.append(choice(sorteado[jogar_dados]))
        dados_na_mão.remove(sorteado)
        if len(passos) > 0:
            for r in range(0, len(passos)):
                passos.append(choice(passos[r]))
        if resultado[jogar_dados] == c:
            pontos_rodada[0] += c
        elif resultado[jogar_dados] == t:
            pontos_rodada[1] += t
        else:
            pontos_rodada[2] += p
            passos.append(sorteado)
    print(resultado)
    resultado = []
    print(pontos_rodada)
    
print(f'{jogadores[0][0]} comeu "{len(jogadores[0][1])}"') #####################