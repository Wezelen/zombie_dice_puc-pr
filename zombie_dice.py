#iniciando jogo
print('JOGO ZOMBIE DICE')
menu = str(input('''digite "iniciar" para começar o jogo ou "regras" para ler as regras. ''')).lower().strip()
if menu == 'regras': #editar as regras
    print('*-*-' * 28)
    #regras:
    print('''13 dados:
6 dados verdes: 3 cerebros, 2 fuga, 1 tiro
4 dados amarelos: 2 cerebros 2 fuga 2 tiro
3 dados vermelhos: 1 cerebros 2 fuga 3 tiro

objetivo: comer 13 cerebros
perde ao levar 3 tiros na mesma rodada

na rodada o jogador pega 3 dados aleatorios o os joga
cada cérebro acumula 1 ponto
tiros acumulam somente na rodada
fuga: a vitima conseguiu escapar
após jogar os 3 dados pode parar e acumular os pontos ou continuar
continuar:
sempre jogara 3 dados
jogara novamente os dados onde a vitima escapou juntamente com o numero de novos dados aleatorios para completar 3
os dados de cérebro e tiro não são jogados novamente mas ficam acumulando os seus valores na rodada
após a rodada acabar os pontos são somados na pontuação do jogador
caso o jogador leve 3 tiros perde a partida
o jogo finaliza quando 1 jogador tiver comido 13 cérebros ou os demais tenham morrido''')
    print('*-*-' * 28)
    menu = str(input('digite "iniciar" para começar o jogo. ')).lower().strip()
    print('são necessários pelo menso 2 jogadores')
elif menu == 'iniciar':
    print('são necessários pelo menso 2 jogadores')
else:
    print('comendo invalido tente novamente!')

#adicionando jogadores
jogadores = []
if menu == 'iniciar':
    nun_jogadores = int(input('digite a quantidade de jogadores: '))
    if nun_jogadores > 1:
        for nomes in range(0, nun_jogadores):
            jogador = ''.join(str(input(f'digite o nome do jogador {nomes + 1}: ')))
            jogadores += [jogador]
    else:
        print('tente novamente')



#criando dados
'''6 dados verdes: 3 cerebros, 2 fuga, 1 tiro
   4 dados amarelos: 2 cerebros 2 fuga 2 tiro
   3 dados vermelhos: 1 cerebros 2 fuga 3 tiro'''
