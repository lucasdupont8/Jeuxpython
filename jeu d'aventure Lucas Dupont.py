"""
Programme réalisé par Dupont, Lucas, 1G7
"""
import random
import time
import pygame
#touche Nord= n or t  Sud= s or g  Est= e or h ouest= o or f

#lieucle=random.randint(2, 11) #autre méthode aléatoire
list=[2,3,4,5,7,8,9,10]
lieucle=random.choice(list)
print(lieucle)
cle=0


#initialisation graphique
pygame.init()
fenetre = pygame.display.set_mode((640,360))
pygame.display.set_caption("jeu d'aventure")
font = pygame.font.Font('freesansbold.ttf', 20)

#images des pieces
image1=pygame.image.load("entrée.png")
image2=pygame.image.load("toilette.png")
image3=pygame.image.load("vuebaignoir.png")
image4=pygame.image.load("lit1.png")
image5=pygame.image.load("extérieur1.png")
image6=pygame.image.load("cuisine.png")
image7=pygame.image.load("salon.png")
image8=pygame.image.load("extérieuresalon.png")
image9=pygame.image.load("tableamanger.png")
image10=pygame.image.load("tableamangerexterieur.png")
image11=pygame.image.load("escalier.png")
image12=pygame.image.load("escaliertemp.png")
image13=pygame.image.load("desenteescalier.png")
image14=pygame.image.load("porte1fermer.png")
image15=pygame.image.load("porte1ouverte.png")



#texte sur les images
text1 = font.render("Vous vous trouvez dans l'entrée", True, (0, 0, 0))
text2 = font.render("Vous vous trouvez dans les toilette", True, (0, 0, 0))
text3 = font.render("Vous vous trouvez dans la suite parentale", True, (0, 0, 0))
text4 = font.render("Vous vous trouvez dans la suite parentale", True, (0, 0, 0))
text5 = font.render("Vous vous trouvez a l'extérieur", True, (0, 0, 0))
text6 = font.render("Vous vous trouvez dans la cuisine", True, (0, 0, 0))
text7 = font.render("Vous vous trouvez dans le salon ", True, (0, 0, 0))
text8 = font.render("Vous vous trouvez a l'extérieur ", True, (0, 0, 0))
text9 = font.render("Vous vous trouvez a coté de la table a manger", True, (0, 0, 0))
text10 = font.render("Vous vous trouvez a coté de la table extérieur ", True, (0, 0, 0))
text11 = font.render("Vous vous trouvez dans l'escalier ", True, (0, 0, 0))
text13 = font.render("Vous vous trouvez dans l'escalier ", True, (0, 0, 0))
text14 = font.render("Vous vous trouvez devant une porte fermer ", True, (0, 0, 0))
text15 = font.render("Vous vous trouvez dans la pièce qui était fermer", True, (0, 0, 0))
text16 = font.render("Vous avez trouvé la clé", True, (51, 222, 73))
text17 = font.render("Vous n'avez pas la clé", True, (218, 28, 28))

dansQuellePierceEstLePersonnage=1


def decrireLaPiece(piece):
    global cle
    if piece==1:
        fenetre.blit(image1,(0,0))      #afficher l'image à la prochaine actualisation
        fenetre.blit(text1,(30,300))
        if lieucle==piece:
            fenetre.blit(text16,(200,180))       #afficher le texte à la prochaine actualisation
            cle=1
    elif piece==2:
        fenetre.blit(image2,(0,0))
        fenetre.blit(text2,(30,300))
        if lieucle==piece:
            fenetre.blit(text16,(200,180))
            cle=1
    elif piece==3:
        fenetre.blit(image3,(0,0))
        fenetre.blit(text3,(30,300))
        if lieucle==piece:
            fenetre.blit(text16,(200,180))
            cle=1
    elif piece==4:
        fenetre.blit(image4,(0,0))
        fenetre.blit(text4,(30,300))
        if lieucle==piece:
            fenetre.blit(text16,(200,180))
            cle=1
    elif piece==5:
        fenetre.blit(image5,(0,0))
        fenetre.blit(text5,(30,300))
        if lieucle==piece:
            fenetre.blit(text16,(200,180))
            cle=1
    elif piece==6:
        fenetre.blit(image6,(0,0))
        fenetre.blit(text6,(30,300))
        if lieucle==piece:
            fenetre.blit(text16,(200,180))
            cle=1
    elif piece==7:
        fenetre.blit(image7,(0,0))
        fenetre.blit(text7,(30,300))
        if lieucle==piece:
            fenetre.blit(text16,(200,180))
            cle=1
    elif piece==8:
        fenetre.blit(image8,(0,0))
        fenetre.blit(text8,(30,300))
        if lieucle==piece:
            fenetre.blit(text16,(200,180))
            cle=1
    elif piece==9:
        fenetre.blit(image9,(0,0))
        fenetre.blit(text9,(30,300))
        if lieucle==piece:
            fenetre.blit(text16,(200,180))
            cle=1
    elif piece==10:
        fenetre.blit(image10,(0,0))
        fenetre.blit(text10,(30,300))
        if lieucle==piece:
            fenetre.blit(text16,(200,180))
            cle=1
    elif piece==11:                  #escalier
        fenetre.blit(image11,(0,0))
        fenetre.blit(text11,(30,300))
        if lieucle==piece:
            fenetre.blit(text16,(200,180))
            cle=1
    elif piece==15:
        if cle==1:
            fenetre.blit(image15,(0,0))        #piece bloquer
            fenetre.blit(text15,(30,300))
        elif cle==0:
            fenetre.blit(image14,(0,0))       #piece débloquer
            fenetre.blit(text14,(30,300))
            fenetre.blit(text17,(200,180))
"""elif piece==14:
        fenetre.blit(image14,(0,0))        #piece bloquer (test)
        fenetre.blit(text14,(30,300))
        if cle==1:
            fenetre.blit(text16,(200,180))"""


def decision(direction,piece):
    if lieucle==piece:
        fenetre.blit(text16,(0,50))
        pygame.display.flip()

    print("Vous désirez allez au",direction)
    memorisePiece=piece

    #N : le personnage désire aller au nord
    if direction=='n'or direction=="t":
        if piece==1:
            piece=6
        elif piece==6:
            piece=9
        elif piece==9:
            piece=10
        elif piece==4:
            piece=3
        elif piece==7:
            piece=8
        elif piece==11:
            piece=15
        """elif piece==11 and cle==0:
            piece=14                     #test
        elif piece==11 and cle==1:
            piece=15"""
    #S : le personnage désire aller au sud
    elif direction=='s'or direction=="g":
        if piece==6:
            piece=1
        elif piece==9:
            piece=6
        elif piece==10:
            piece=9
        elif piece==3:
            piece=4
        elif piece==8:
            piece=7
        elif piece==14:
            piece=11
        elif piece==15:
            piece=11
    #E : le personnage désire aller à l'est
    elif direction=='e'or direction=="h":
        if piece==7:
            piece=6
        elif piece==6:
            piece=11
            fenetre.blit(image12,(0,0))
            pygame.display.flip()
            time.sleep(0.5)
        elif piece==5:
            piece=3
        elif piece==3:
            piece=1
        elif piece==1:
            piece=2

    #O : le personnage désire aller à l'ouest
    elif direction=='o'or direction=="f":
        if piece==6:
            piece=7
        elif piece==11:
            piece=6      #possible retour escalier
            fenetre.blit(image13,(0,0))
            pygame.display.flip()
            time.sleep(0.5)
        elif piece==3:
            piece=5
        elif piece==1:
            piece=3
        elif piece==2:
            piece=1

    #deplacement imposible
    if memorisePiece==piece:
        print("Déplacement impossible")
    else:
        print("C'est possible")
    return piece


loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenetre (croix rouge)
        elif event.type == pygame.KEYDOWN:  #lecture du clavier
            dansQuellePierceEstLePersonnage=decision(event.unicode,dansQuellePierceEstLePersonnage)
            if event.key == pygame.K_ESCAPE or event.unicode == 'q': #touche q pour quitter
                loop = False
    decrireLaPiece(dansQuellePierceEstLePersonnage)
    # Actualisation de l'affichage
    pygame.display.flip()
pygame.quit()

