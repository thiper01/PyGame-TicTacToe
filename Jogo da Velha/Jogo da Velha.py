import pygame
from pygame.locals import MOUSEBUTTONDOWN, Rect, QUIT
from sys import exit
import os

#Define o menu inicial do jogo


def introducao():
       
    intro = True

    while intro:
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if click[0] == 1 and mouse[0] >= 360 and mouse[0] <=599 and mouse[1] >= 463 and mouse[1] <=512: # inicia jogo
                intro = False
            if click[0] == 1 and mouse[0] >= 480 and mouse[0] <= 573 and mouse[1] >= 8 and mouse[1] <= 90: #inicia ranking
                print("epa")
                os.startfile("rankingOrd.txt")
            if click[0] == 1 and mouse[0] >= 28 and mouse[0] <= 185 and mouse[1] >= 523 and mouse[1] <= 572: #quita do game
                pygame.quit()
                quit()
                

            if event.type == pygame.QUIT:
                pygame.quit()
                quit() 
        img = pygame.image.load('Menu.png').convert_alpha()
        seta1 = pygame.image.load('Arrow pt5.png').convert_alpha()
        tela.blit(img, (0,0))
        tela.blit(seta1, (20,480))
        tela.blit(pygame.image.load('to be continued.png').convert_alpha(),(350,460))
        
        pygame.display.update()

def pontuador(vencedor):
    end = ""
    arquivo = open("ranking.txt", "r+")
    achou = False
    linha = 0
    naotinha = False
    
    while not achou:
        leitura = arquivo.readline()
        if leitura == end:
            arquivo.write(vencedor)
            arquivo.write(":1\n")
            achou = True
            naotinha = True
            break

        nome_ponto = leitura.rstrip().split(":")
        nome = nome_ponto[0]
    
        if nome == vencedor:
            achou = True
        else:
            linha += 1

    if naotinha is False:
        arquivo.seek(0)
        rank = arquivo.readlines()
        nome_ponto = rank[linha].rstrip().split(":")
        nome_ponto[1]= int(nome_ponto[1])+1
        nome_ponto[1] = str(nome_ponto[1])
        rank[linha] = "".join((":".join(nome_ponto), "\n"))
        arquivo.seek(0)
        print(rank)
        arquivo.writelines(rank)

def rankingordenado():
    vazio = ""
    ranking = []
    achou = False

    arquivo = open("ranking.txt")
    arquivo.seek(0)
    while not achou:
        leu = arquivo.readline()
        if leu == vazio:
            achou = True
        else:
            leu_ponto = leu.rstrip().split(":")
            transfer = "".join((leu_ponto[1], " ", leu_ponto[0]))
            ranking.append(transfer)
            ranking.sort(reverse=True, key=myFunc)

    return ranking

def escreveOrd(ranking):
    arquivo = open("rankingOrd.txt","w+")
    for i in range (len(ranking)):
        arquivo.write("{}\n".format(ranking[i]))

def myFunc(e):
    e = e.split(" ")
    return int(e[0])

def inputBox():
    global users
    users = []
    screen = pygame.display.set_mode((640, 600))
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(200, 300, 1000, 50)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = True
    arial = pygame.font.SysFont('mingliuextbpmingliuextbmingliuhkscsextb', 30)
    i = 0

    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        users.append(text)
                        print(users)
                        text = ''
                        
                        if len(users) == 2:
                            done = False     
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((0,0,0))
        a =arial.render("Digite o nome do jogador",True,(255,255,255))
        tela.blit(a,(150,200))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()
        clock.tick(30)

#Desenha o tabuleiro
def desenhar_tabu():
    pygame.draw.line(tela, (255, 255, 255), (200, 0), (200, 600), 10)
    pygame.draw.line(tela, (255, 255, 255), (400, 0), (400, 600), 10)
    pygame.draw.line(tela, (255, 255, 255), (0, 200), (600, 200), 10)
    pygame.draw.line(tela, (255, 255, 255), (0, 400), (600, 400), 10)

#Função para desenhar as peças do jogo
def desenhar_peca(pos):
    global VEZ
    x, y = pos
    if VEZ == 'JOGADOR2':
        img = pygame.image.load('Bola.png').convert_alpha()
        tela.blit(img,(x-50,y-50))
    else:
        img = pygame.image.load('X-JoJo.png').convert_alpha()
        img = pygame.transform.scale(img,(100,100))
        tela.blit(img, (x - 50, y - 50))

#Função que verifica a posição do mouse
def testa_pos():
    for p in rec:
        if e.type == MOUSEBUTTONDOWN and p.collidepoint(mouse_pos):
            if p == rect1:
                confimar(0, [100, 100])
            if p == rect2:
                confimar(1, [300, 100])
            if p == rect3:
                confimar(2, [500, 100])
            if p == rect4:
                confimar(3, [100, 300])
            if p == rect5:
                confimar(4, [300, 300])
            if p == rect6:
                confimar(5, [500, 300])
            if p == rect7:
                confimar(6, [100, 500])
            if p == rect8:
                confimar(7, [300, 500])
            if p == rect9:
                confimar(8, [500, 500])

#Função que confirma a posição da peça
def confimar(indice, pos):
    global ESCOLHA, VEZ, espaco
    if marca_tabu[indice] == 'X':
        print('X')
    elif marca_tabu[indice] == 'O':
        print('O')
    else:
        marca_tabu[indice] = ESCOLHA
        desenhar_peca(pos)
        print(marca_tabu)
        if VEZ == 'JOGADOR1':
            VEZ = 'JOGADOR2'
        else:
            VEZ = 'JOGADOR1'
        espaco +=1

#testa se um jogador ganhou
def teste_vitoria(l):
    return ((marca_tabu[0] == l and marca_tabu[1] == l and marca_tabu[2] == l) or
        (marca_tabu[3] == l and marca_tabu[4] == l and marca_tabu[5] == l) or
        (marca_tabu[6] == l and marca_tabu[7] == l and marca_tabu[8] == l) or
        (marca_tabu[0] == l and marca_tabu[3] == l and marca_tabu[6] == l) or
        (marca_tabu[1] == l and marca_tabu[4] == l and marca_tabu[7] == l) or
        (marca_tabu[2] == l and marca_tabu[5] == l and marca_tabu[8] == l) or
        (marca_tabu[0] == l and marca_tabu[4] == l and marca_tabu[8] == l) or
        (marca_tabu[2] == l and marca_tabu[4] == l and marca_tabu[6] == l))

#Mostra o vencedor
def texto_vitoria(v):
    arial = pygame.font.SysFont('arial', 70)
    mensagem = 'JOGADOR {} VENCEU'.format(v)

    if v == 'EMPATE':
        mens_vitoria = arial.render('DEU VELHA', True, (0, 255, 0), 0)
        tela.blit(mens_vitoria, (115, 265))
    else:
        mens_vitoria = arial.render(mensagem, True, (0, 255, 0), 0)
        tela.blit(mens_vitoria, (0, 265))

#reinicia o jogo
def reset():
        global ESCOLHA, ESTADO, VEZ, marca_tabu, espaco
        ESTADO = 'JOGANDO'
        VEZ = 'JOGADOR1'
        ESCOLHA = 'X'
        espaco = 0
        marca_tabu = [
            0, 1, 2,
            3, 4, 5,
            6, 7, 8
        ]
        tela.fill(0)

def pontos(pontos1, pontos2):
    arial = pygame.font.SysFont('mingliuextbpmingliuextbmingliuhkscsextb', 30)
    jogador1 = '{} = {}'.format(users[0],pontos1) #mudar quando tiver vetor pronto
    jogador2 = '{} = {}'.format(users[1],pontos2)

    jd1 = arial.render(jogador1, True, (188, 186, 186))
    jd2 = arial.render(jogador2, True, (188, 186, 186))
    tela.blit(jd1, (0, 0))
    tela.blit(jd2, (420, 0))

pygame.init()

tela = pygame.display.set_mode((600, 600), 0, 32)
pygame.display.set_caption('Jogo da velha')
pygame.mixer.music.load('Giornos Theme.mp3')
pygame.mixer.music.set_volume(0.5)

ESTADO = 'JOGANDO'
VEZ = 'JOGADOR1'
ESCOLHA = 'X'
espaco = 0
marca_tabu = [
    0, 1, 2,
    3, 4, 5,
    6, 7, 8
]

rect1 = Rect((0, 0), (200, 200))
rect2 = Rect((200, 0), (200, 200))
rect3 = Rect((400, 0), (200, 200))
rect4 = Rect((0, 200), (200, 200))
rect5 = Rect((200, 200), (200, 200))
rect6 = Rect((400, 200), (200, 200))
rect7 = Rect((0, 400), (200, 200))
rect8 = Rect((200, 400), (200, 200))
rect9 = Rect((400, 400), (200, 200))

rec = [
    rect1,rect2,rect3,rect4,
    rect5,rect6,rect7,rect8,rect9,
]

pontos1, pontos2 = 0, 0

print(pygame.font.get_fonts())
pygame.mixer.music.play(-1, 0.0)

print(rankingordenado())
escreveOrd(rankingordenado())
introducao()
inputBox()
tela.fill((0,0,0))


while True:
    mouse_pos = pygame.mouse.get_pos()
    if ESTADO == 'JOGANDO':
        desenhar_tabu()
        pontos(pontos1, pontos2)

        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                exit()
            if e.type == MOUSEBUTTONDOWN:
                if VEZ == 'JOGADOR1':
                    ESCOLHA = 'X'
                    testa_pos()
                else:
                    ESCOLHA = 'O'
                    testa_pos()

        if teste_vitoria('X'):
            print('X VENCEU')
            texto_vitoria('X')
            vencedor = users[0]
            pontuador(vencedor)
            
            ESTADO = 'RESET'
            pontos1 += 1

        elif teste_vitoria('O'):
            print('O VENCEU')
            texto_vitoria('O')
            vencedor = users[1]
            pontuador(vencedor)
            
            ESTADO = 'RESET'
            pontos2 +=1

        elif espaco >= 9:
            print('EMPATE')
            texto_vitoria('EMPATE')
            ESTADO = 'RESET'

    else:
        for u in pygame.event.get():
            if u.type == QUIT:
                pygame.quit()
                exit()
            if u.type == MOUSEBUTTONDOWN:
                reset()
                desenhar_tabu()
    pygame.display.flip()