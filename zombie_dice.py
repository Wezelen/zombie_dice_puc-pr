#adicionando Bibliotecas
from random import choice
from time import sleep

#criando os dados
p = '👟'
c = '🧠'
t = '💥'
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
for nomes in range(num_jogadores):
    jogador = str(input('Digite o nome do {}° jogador: ' .format(nomes + 1)))
    jogadores.append(jogador)
    

#função para sortear dados
""" def sortear_dados(dado):
    pass """

""" dados_para_sortear = pote
dados_sorteados = []
resultado = []
contador_tiros = 

for pegar_dados in range(0, 3): #sorteia 3 dados do pote
    dados_sorteados.append(choice(dados_para_sortear))
    dados_para_sortear.remove(dados_sorteados[pegar_dados])

for jogar_dados in range(0, 3): #roda os 3 dados sorteados
    sorteado = choice(dados_sorteados)
    print(sorteado)
    resultado.append(choice(sorteado[jogar_dados]))
    dados_sorteados.remove(sorteado)
    if resultado[jogar_dados] == c:
        pass
    elif resultado[jogar_dados] == t:
        pass
    else: #funcionando
        dados_para_sortear.append(sorteado)
    
     """