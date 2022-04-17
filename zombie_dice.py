'''Nome: Wezelen Gomes dos Santos Junior
   curso: Analise e desenvolvimento de sistemas'''


#adicionando Bibliotecas
from time import sleep
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
print('><<' * 15)
print('        Vamos jogar Zombie Dice!')
print('><<' * 15)
while True:
    menu = int(input('''MENU:
Iniciar    |1|
Regras     |2|
Sair       |3|
'''))
    if menu == 1:
        break
    elif menu == 2:
        print('_' * 100)
        print('''neste jogo cada dado representa uma vítima, e seu objetivo é comer os cérebros delas.
os dados possuem 3 símbolos:
🧠 cérebro - você devorou sua vítima com sucesso
💥 tiro    - sua vítima atirou em você
👟 pegadas - sua vítima correu
existem 3 tipos de dados:
🟩 o dado verde é uma vítima mais fraca.    - 3 🧠, 2 👟 e 1 💥
🟨 o dado amarelo é uma vítima normal.      - 2 🧠, 2 👟 e 2 💥
🟥 o dado vermelho é uma vítima mais forte. - 1 🧠, 2 👟 e 3 💥 
- O jogador pega 3 dados aleatórios e os joga (cada jogada é necessário jogar 3 dados)
- Após cada jogada o jogador pode decidir se deseja continuar jogando
- Os dados que forem pegadas(👟) serão jogados novamente, juntamente com mais dados aleatórios,
completando os 3 dados necessário para a jogada
- Se o jogador tomar 3 tiros durante sua rodada ele perde todos os cérebros acumulados na rodada e
passa sua vez para o próximo jogador
o jogo acaba quando algum jogador comer 13 cérebros.
''')
        print('_'*100)
        input('para voltar ao menu precione |enter|')
    elif menu == 3:
        exit()
    else:
        print('comando invalido')


#criando Jogadores
jogadores = []
num_jogadores = 0

while True:#quantidade de jogadores
    try:
        print('_' * 45)
        num_jogadores = int(input('digite a quantidade de jogadores: '))
        if num_jogadores > 1:
            break
        else:
            print('É necessario pelo menos 2 jogadores')
    except:
        print('Valor invalido')

for nomes in range(0, num_jogadores):#nomeando jogadores
    jogador = str(input('Digite o nome do {}° jogador: '.format(nomes + 1)))
    contador = [jogador, ''] #para adicionar os pontos do jogador
    jogadores.append(contador)


pontuacao = 0
while pontuacao < 12:    
    for player in range(0, len(jogadores)):
        
        #sortear dados
        pontos_rodada = ['', '', '']
        dados_na_mão = []
        dados_no_pote = add_dado(pote)[:]
        passos = []
        jogada = 0
        if pontuacao >= 13: #cortar o ciclo quando alguem fizer 13 pontos
            break
        print('=' * 45)
        print('jogadores       pontuação') #placar
        for placar in range(0, len(jogadores)):
            print(f'\033[0;33m{jogadores[placar][0]:-<15}-({len(jogadores[placar][1]):^3})-{jogadores[placar][1]:<13} \033[m')
        print('=' * 45) 
        input('para continuar precione |enter|')
        
        while True:
            resultado = []
            cor_dados = []
            if len(pontos_rodada[1]) >= 3: #checa se o jogador ja levou 3 tiros na rodada
                print('=' * 45)
                print(f'\033[0;31m{jogadores[player][0]} tomou pelo menos 3 tiros\033[m')                
                print('=' * 45)
                print('para continuar precione |enter|')
                input()
                break

            if jogada != 0: #para mostrar a mensagem de continue somente a partir da segunda jogada do jogador
                print('deseja continuar?')                
                continuar = str(input('[S] [N]  ')).strip()
                if continuar in 'Ss':
                    pass
                elif continuar in 'Nn':
                    jogadores[player][1] += pontos_rodada[0]
                    if pontuacao < len(jogadores[player][1]):
                        pontuacao = len(jogadores[player][1])
                    break                     
            jogada += 1

            if len(dados_no_pote) + len(passos) > 3: #checa se ainda é possivel ter 3 dados para jogar                
                for pegar_dados in range(0, 3): #sorteia dados até completar 3 na mão,verificando se ja teve algum passo na jogada para jogar esse dado novamente
                    if len(passos) > 0:
                        for r in range(0, len(passos)):
                            dados_na_mão.append(passos[0])
                            passos.remove(passos[0])
                    else:
                        dados_na_mão.append(choice(dados_no_pote))                   
                    if dados_na_mão[pegar_dados] == dado_vermelho: #acumulando a cor dos 3 dados para mostrar para o jogador
                        cor_dados.append(vermelho)
                    elif dados_na_mão[pegar_dados] == dado_amarelo:
                        cor_dados.append(amarelo)
                    elif dados_na_mão[pegar_dados] == dado_verde:
                        cor_dados.append(verde)
                    try: #remove as cores para a proxima jogada
                        dados_no_pote.remove(dados_na_mão[pegar_dados])
                    except:
                        pass
                print('=' * 45)
                sleep(0.5)
                print(f'\033[43m {jogadores[player][0]} \033[m pegou os dados:\n\n{cor_dados[0]} {cor_dados[1]} {cor_dados[2]}') #mostra ao jogador quais dados ele pegou                
            else: #quando a quantidade de dasos não soma 3 dados, interrompe o ciclo e soma os pontos ao jogador
                print('=' * 45)
                print('não a mais dados suficientes para uma nova jogada')                
                jogadores[player][1] += pontos_rodada[0]
                break
                        
            for jogar_dados in range(0, 3):#roda os 3 dados sorteados e adiciona soma os resultados nos pontos da rodada
                resultado.append(choice(dados_na_mão[0]))    
                if resultado[jogar_dados] == c:
                    pontos_rodada[0] += c
                elif resultado[jogar_dados] == t:
                    pontos_rodada[1] += t
                else:
                    pontos_rodada[2] += p
                    passos.append(dados_na_mão[0])
                dados_na_mão.remove(dados_na_mão[0]) #remove os dados para proxima jogada            
            
            print('=' * 45) #mostra os dados e os resultados ao jogador
            sleep(0.5)
            print(f'{cor_dados[0]} → {resultado[0]}')
            sleep(0.5)
            print(f'{cor_dados[1]} → {resultado[1]}')
            sleep(0.5)
            print(f'{cor_dados[2]} → {resultado[2]}')
            sleep(0.5)
            print('=' * 45)
            print(f'Pontuação de {jogadores[player][0]} na rodada')
            print('=' * 45)
            sleep(0.5)
            print(f'{pontos_rodada[0]} | {pontos_rodada[1]} | {pontos_rodada[2]}')            

print('=' * 45)
print('jogadores       pontuação') #placar
for placar in range(0, len(jogadores)):
    print(f'\033[0;33m{jogadores[placar][0]:-<15}-({len(jogadores[placar][1]):^3})-{jogadores[placar][1]:<13} \033[m')

print('+==' * 15, '\nresultado')
for jogador in jogadores:
    if len(jogador[1]) == pontuacao:
        print('vencedor')
        print(f'\033[42m {jogador[0]} \033[m\nconseguiu comer {jogador[1]}')

