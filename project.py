# Afonso Ponces de Carvalho / ist199046 / 1º Projeto de FP 2020/2021


def eh_tabuleiro(tab):  # Verifica se o tabuleiro introduzido e valido ou nao
    '''

    :param tab: tabuleiro do jogo do galo
    :return: True or False
    '''
    if type(tab) != tuple:
        return False
    if len(tab) != 3:
        return False
    for i in tab:
        if type(i) != tuple:
            return False
        if len(i) != 3:
            return False
        for e in i:
            if type(e) != int:
                return False
            if e != 1 and e != -1 and e != 0:
                return False
    return True


def eh_posicao(x):  # Verifica se o inteiro introduzido esta entre as posicoes possiveis do tabuleiro
    '''

    :param x: numero inteiro entre 1 e 9
    :return: True or False
    '''
    if type(x) != int:
        return False
    else:
        if x > 9 or x <= 0:
            return False
        else:
            return True


def obter_coluna(tab, c):  # Obter uma coluna do tabuleiro
    '''

    :param tab: tabuleiro do jogo do galo
    :param c: numero inteiro entre 1 e 3
    :return: tuplo que e uma coluna do tabuleiro
    '''
    if not eh_tabuleiro(tab) or c > 3 or c < 1 or type(c) != int:
        raise ValueError('obter_coluna: algum dos argumentos e invalido')
    res = ()
    for e in tab:
        for i in range(len(e)):
            if i + 1 == c:
                res = res + (e[i],)
    return res


def obter_linha(tab, l):  # Obter uma linha do tabuleiro
    '''

    :param tab: tabuleiro do jogo do galo
    :param l: numero inteiro entre 1 e 3
    :return: tuplo que e uma linha do tabuleiro
    '''
    if not eh_tabuleiro(tab) or l > 3 or l < 1 or type(l) != int:
        raise ValueError('obter_linha: algum dos argumentos e invalido')
    res = ()
    for e in range(len(tab)):
        if e + 1 == l:
            res = res + tab[e]
    return res


def obter_diagonal(tab, dg):  # Obter uma diagonal do tabuleiro
    '''

    :param tab: tabuleiro do jogo do galo
    :param dg: numero inteiro entre 1 e 2
    :return: tuplo que e uma diagonal (da esquerda para a direita) do tabuleiro
    '''
    if not eh_tabuleiro(tab) or dg not in (1, 2) or type(dg) != int:
        raise ValueError('obter_diagonal: algum dos argumentos e invalido')
    res = []
    if dg == 1:
        res = res + [tab[0][0]] + [tab[1][1]] + [tab[2][2]]
    if dg == 2:
        res = res + [tab[2][0]] + [tab[1][1]] + [tab[0][2]]
    return tuple(res)


def tabuleiro_str(tab):  # Representacao do tabuleiro recebido em string
    '''

    :param tab: tabuleiro do jogo do galo
    :return: string da constituicao do tabuleiro (usar print para representar o tabuleiro)
    '''
    if not eh_tabuleiro(tab):
        raise ValueError("tabuleiro_str: o argumento e invalido")
    res = ''
    r = ''
    for c in range(len(tab)):
        res += ' '
        for e in range(len(tab[c])):
            if tab[c][e] == 1:
                r = 'X'
            if tab[c][e] == -1:
                r = 'O'
            if tab[c][e] == 0:
                r = ' '
            res = res + r
            if e == 2:
                res = res + ''
            else:
                res = res + ' ' + '|' + ' '
        if c == 2:
            res = res + ' '
        else:
            res = res + ' \n-----------\n'
    return res


def eh_posicao_livre(tab, p):  # Confirma se a posicao escolhida se encontra entre as posicoes livres do tabuleiro
    '''

    :param tab: tabuleiro do jogo do galo
    :param p: numero inteiro entre 1 e 9
    :return: True or False
    '''
    if not eh_tabuleiro(tab) or not eh_posicao(p):
        raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')
    for e in range(len(tab[0])):
        if p == e + 1:
            if tab[0][e] == 0:
                return True
    for e in range(len(tab[1])):
        if p == e + 4:
            if tab[1][e] == 0:
                return True
    for e in range(len(tab[2])):
        if p == e + 7:
            if tab[2][e] == 0:
                return True
    return False


def obter_posicoes_livres(tab):  # Obter posicoes livres do tabuleiro
    '''

    :param tab: tabuleiro do jogo do galo
    :return: tuplo que representa as posicoes livres do tabuleiro (inteiros de 1 a 9)
    '''
    if not eh_tabuleiro(tab):
        raise ValueError('obter_posicoes_livres: o argumento e invalido')
    i = 1
    res = ()
    while i < 10:
        if eh_posicao_livre(tab, i):
            res = res + (i,)
        i = i + 1
    return res


def jogador_ganhador(tab):  # Mostra , dependendo do tabuleiro quem ganhou (1 ou -1 em linha ) ou se nao ha ganhador
    '''

    :param tab: tabuleiro de jogo
    :return: 1 or -1 or 0 . dependendo se ha ganhador (1 para o X)(-1 para a O)(0 se ninguem ganha)
    '''
    if not eh_tabuleiro(tab):
        raise ValueError('jogador_ganhador: o argumento e invalido')
    for i in range(1, 9):
        if i < 4:
            res = avaliar_tuplo(obter_coluna(tab, i))
        elif i < 7:
            res = avaliar_tuplo(obter_linha(tab, i - 3))
        else:
            res = avaliar_tuplo(obter_diagonal(tab, i - 6))
        if res in (1, -1):
            return res
    return 0


def avaliar_tuplo(tpl):  # Funcao auxiliar - Avalia o tuplo auxiliando a funcao jogador ganhador
    '''

    :param tpl: tuplo (linha, coluna ou diagonal)
    :return: -1 (tupulo = (1,1,1) or 1 (tupulo = (1,1,1) or 0
    '''
    return tpl[0] if (tpl[0] == tpl[1] == tpl[2] and tpl[0] in (1, -1)) else 0


def marcar_posicao(tab, i, pos):  # Marca a posicao escolhida com 1 ou -1
    '''

    :param tab: tabuleiro do jogo do galo
    :param i: 1 or -1 or 0
    :param pos: posicao do tabuleiro do jogo do galo
    :return: tuplo que e um tabuleiro modificado pela posicao marcada pela funcao
    '''
    if not eh_tabuleiro(tab) or i not in (1,-1) or type(i) != int or pos not in obter_posicoes_livres(tab):
        raise ValueError('marcar_posicao: algum dos argumentos e invalido')
    tab_list = [list(c) for c in tab]
    linha = (pos - 1) // 3
    coluna = pos - (linha * 3 + 1)
    tab_list[linha][coluna] = i
    return tuple([tuple(c) for c in tab_list])


def escolher_posicao_manual(tab):  # Posicao escolhida manualmente pelo jogador
    '''

    :param tab: tabuleiro do jogo do galo
    :return: x (se x entre as posicoes livres do tabuleiro)
    '''
    if not eh_tabuleiro(tab):
        raise ValueError('escolher_posicao_manual: o argumento e invalido')
    x = int(input('Turno do jogador. Escolha uma posicao livre: '))
    if x not in obter_posicoes_livres(tab):
        raise ValueError('escolher_posicao_manual: a posicao introduzida e invalida')
    else:
        return x


def basico(tab):  # Funcao auxiliar - Modo de jogo Basico
    '''

    :param tab: tabuleiro do jogo do galo
    :return: inteiro entre 1 e 9 (apos analisar o tabuleiro com as estrategias), onde o computador vai jogar
    '''
    if  5 in obter_posicoes_livres(tab):
        return 5
    else :
        return estrategia_canto_vazio_e_lateral_vazio_7_e_8(tab)


def normal(tab,i):  # Funcao auxiliar - Modo de jogo Normal
    '''

    :param tab: tabuleiro do jogo do galo
    :param i: 1 or -1(dependendo da peca do computador)
    :return: inteiro entre 1 e 9 (apos analisar o tabuleiro com as estrategias), onde o computador vai jogar
    '''
    x = estrategia_vitoria1(tab,i)
    if x != -1 :
        return estrategia_vitoria1(tab,i)
    x = estrategia_bloqueio2(tab,i)
    if x != -1 :
        return estrategia_bloqueio2(tab,i)
    if  5 in obter_posicoes_livres(tab):
        return 5
    x = estrategia_canto_oposto6(tab,i)
    if x != -1 :
        return estrategia_canto_oposto6(tab,i)
    x = estrategia_canto_vazio_e_lateral_vazio_7_e_8(tab)
    if x != -1 :
        return estrategia_canto_vazio_e_lateral_vazio_7_e_8(tab)


def perfeito(tab,i):  # Funcao auxiliar - Modo de jogo Perfeito
    '''

    :param tab: tabuleiro do jogo do galo
    :param i: 1 or -1(dependendo da peca do computador)
    :return: inteiro entre 1 e 9 (apos analisar o tabuleiro com as estrategias), onde o computador vai jogar
    '''
    x = estrategia_vitoria1(tab, i)
    if x != -1:
        return estrategia_vitoria1(tab, i)
    x = estrategia_bloqueio2(tab, i)
    if x != -1:
        return estrategia_bloqueio2(tab, i)
    if 5 in obter_posicoes_livres(tab):
        return 5
    x = estrategia_canto_oposto6(tab, i)
    if x != -1:
        return estrategia_canto_oposto6(tab, i)
    x = estrategia_canto_vazio_e_lateral_vazio_7_e_8(tab)
    if x != -1:
        return estrategia_canto_vazio_e_lateral_vazio_7_e_8(tab)


def estrategia_canto_vazio_e_lateral_vazio_7_e_8(tab):  # Funcao auxiliar - estrategia canto vazio e estrategia lateral vazia
    '''

    :param tab: tabuleiro do jogo do galo
    :return: se houver possibildidade de jogo devolve c, se nao devolve -1
    '''
    x = (1,3,7,9,2,4,6,8)
    for c in x :
        if c in obter_posicoes_livres(tab):
            return c
    return -1


def estrategia_vitoria1(tab,i):  # Funcao auxiliar - estrategia vitoria
    '''

    :param tab: tabuleiro do jogo do galo
    :param i: 1 or -1(dependendo da peca do computador)
    :return: posicao a jogar pelo computador se houver uma vitoria iminente de modo a ganhar o jogo
    '''
    return possibilidade_de_vitoria(tab,i)


def possibilidade_de_vitoria(tab,i):  # Funcao auxiliar - verifica se ha possibildade de vitoria ou bloqueio
    '''

    :param tab: tabuleiro do jogo do galo
    :param i: 1 or -1(dependendo da peca do computador)
    :return: -1 (se nao houver jogo possivel) c (melhor posicao para defender ou ganhar dependendo do que e preciso)
    '''
    x = ((i, i, 0), (i, 0, i), (0, i, i))
    for c in range(1, 9):
        if 0 < c < 4:
            res = obter_coluna(tab, c)
            if res in x:
                return res.index(0) * 3 + c
        elif 3 < c < 7:
            res = obter_linha(tab, c - 3)
            if res in x:
                return (c - 4) * 3 + res.index(0) + 1
        elif 6 < c < 9:
            res = obter_diagonal(tab, c - 6)
            if res in x:
                if c - 6 == 1:
                    return 4 * res.index(0) + 1
                if c - 6 == 2:
                    return 7 - 2 * res.index(0)
    return -1


def estrategia_bloqueio2(tab,i):  # Funcao auxiliar - Estrategia de bloqueio
    '''

    :param tab: tabuleiro do jogo do galo
    :param i: 1 or -1(dependendo da peca do computador)
    :return: melhor posicao a jogar de modo a prevenir uma derrota iminente
    '''
    return possibilidade_de_vitoria(tab,-i)


def estrategia_canto_oposto6(tab,i):  # Funcao auxiliar - Estrategia Canto Oposto
    '''

    :param tab: tabuleiro do jogo do galo
    :param i: 1 or -1(dependendo da peca do computador)
    :return: posicao do tabuleiro apos analise de qual a melhor posicao a escolher dependendo d
    '''
    if 1 not in obter_posicoes_livres(tab) and tab[0][0] == (-i):
        if 9 in obter_posicoes_livres(tab):
            return 9
    if 3 not in obter_posicoes_livres(tab) and tab[0][2] == (-i):
        if 7 in obter_posicoes_livres(tab):
            return 7
    if 7 not in obter_posicoes_livres(tab) and tab[2][0] == (-i):
        if 3 in obter_posicoes_livres(tab):
            return 3
    if 9 not in obter_posicoes_livres(tab) and tab[2][2] == (-i):
        if 1 in obter_posicoes_livres(tab):
            return 1
    return -1


def escolher_posicao_auto(tab,i,cad):  # Posicao escolhida automaticamente pelo computador
    '''

    :param tab: tabuleiro do jogo do galo
    :param i: 1 or -1(dependendo da peca do computador)
    :param cad: 'basico','normal' ou 'perfeito' dependendo do modo de jogo que se quer jogar
    :return: posicao a jogar pelo computador tendo em conta o tabuleiro e a estrategia pedida
    '''
    if not eh_tabuleiro(tab) or i not in (1,-1) or type(i) != int or cad not in ('basico','normal','perfeito'):
        raise ValueError('escolher_posicao_auto: algum dos argumentos e invalido')
    if cad == 'basico':
        return basico(tab)
    if cad == 'normal':
        return normal(tab,i)
    if cad == 'perfeito':
        return perfeito(tab,i)


def jogo_do_galo(cad1,cad2):  # Jogo do Galo Completo (jogador vs computador)
    '''

    :param cad1: 'X' or 'O' (peca do jogador)('X' joga primeiro)
    :param cad2: 'basico','normal' ou 'perfeito' dependendo do modo de jogo que se quer jogar
    :return: jogo do galo completo contra o computador (primeiro a por 3 em linha ganha)(Empate se nao houver mais espacos)
    '''
    if cad1 not in ('O','X') or cad2 not in ('basico','normal','perfeito'):
        raise ValueError('jogo_do_galo: algum dos argumentos e invalido')
    print("Bem-vindo ao JOGO DO GALO.\nO jogador joga com '"+cad1+"'.")
    tab = ((0,0,0),(0,0,0),(0,0,0))
    while obter_posicoes_livres(tab) != () :
        if cad1 == 'X':  # se o jogador escolher X joga primeiro
            jogador,computador = 1,-1
            x = escolher_posicao_manual(tab)
            tab = marcar_posicao(tab,jogador,x)
            print(tabuleiro_str(tab))
            if jogador_ganhador(tab) == 1 :  # verificar se alguem ganhou antes de continuar o jogo
                return 'X'
            if obter_posicoes_livres(tab) == ():  # verificar se o tabuleiro esta cheio antes de comtinuar o jogo
                return 'EMPATE'
            print('Turno do computador ('+cad2+'):')
            tab = marcar_posicao(tab, computador, (escolher_posicao_auto(tab, computador, cad2)))
            print(tabuleiro_str(tab))
            if jogador_ganhador(tab) == -1 :
                return 'O'
        elif cad1 == 'O' :  # se o jogador escolher O, o computador joga primeiro
            jogador,computador = -1,1
            print('Turno do computador ('+cad2+'):')
            tab = marcar_posicao(tab, computador, (escolher_posicao_auto(tab, computador, cad2)))
            print(tabuleiro_str(tab))
            if jogador_ganhador(tab) == 1 :
                return 'X'
            if obter_posicoes_livres(tab) == ():
                return 'EMPATE'
            x = escolher_posicao_manual(tab)
            tab = marcar_posicao(tab, jogador, x)
            print(tabuleiro_str(tab))
            if jogador_ganhador(tab) == -1 :
                return 'O'


jogo_do_galo('X','basico')