from tkinter import*
# import the module tkinter's features


def window1():
    mywindow = Tk()
    # use of a tkinter's class to create an instance (object) named "mywindow"
    mytext = Label(mywindow, text = "Bonjour à tous les élèves du groupe NSI !", fg="red")
    # "" "" label defines a label to show messages in "mywindow"
    mytext.pack()
    # .pack is a method that adjusts the size of the master window to the slaves widgets
    mybutton = Button(mywindow, text = "Quitter", command=mywindow.destroy)
    # like mytext and label but this time, creation of a button that closes the window
    mybutton.pack()
    # "" ""
    mywindow.mainloop()
    # allows the start of the events intercepter


def centrecible():
# Dessine, dans le canevas can, deux lignes, une horizontale et une verticale,
# dont l'intersection définit le centre de la cible.
# On utilise la methode create_line qui permet, en passant x1, y1,x2, y2 en arguments
# de tracer le segment d'extrémités (x1,y1) et (x2,y2) .
    can.create_line(250,0,250,500)
    can.create_line(0,250,500,250)


def carre(x,y,r):
# Dessine un carre de centre (x,y), de côtés parallèles a ceux du canevas
# de demi-cote r, de couleur rouge dans le canevas can.
    can.create_rectangle(x-r,y-r,x+r,y+r,outline='red')
    # On utilise la methode create_rectangle qui permet de dessiner un rectangle de cotes paralleles a
    # ceux du canevas. En passant x1,y1,x2,y2 en arguments, on obtient le rectangle dont les
    # extremites de la diagonale qui relie le sommet en haut a gauche au sommet en bas a droite
    # sont (x1,y1) et (x2,y2).


def cercle(x,y,r):
# Dessine un cercle de centre (x,y), de rayon r, de couleur bleue dans le canevas can.
    can.create_oval(x-r,y-r,x+r,y+r,outline='blue')
    # On utilise la methode create_oval qui permet de dessiner une ellipse d'axes paralleles
    # aux cotes du canevas. En passant x1,y1,x2,y2 en arguments, on obtient l'ellipse contenue
    # dans la boite rectangulaire dont les extremites de la diagonale qui relie le sommet
    # en haut a gauche au sommet en bas a droite sont (x1,y1) et (x2,y2).
    # Ici, la boite est un carre, l'ellipse est un cercle.

def losange(
def dessin1():
    can.delete(ALL)
    # efface tout dessin preexistant.
    centrecible()
    # trace les deux lignes, horizontale et verticale.
    rayon=30
    while rayon<250:
        cercle(250,250,rayon)
        rayon+=30
        # trace des cercles concentriques.


def dessin2():
    can.delete(ALL)
    centrecible()
    r=30
    while r<250:
        carre(250,250,r)
        r+=30
        # trace des carres emboites.


### Programme principal ###
def cibles():
    fen=Tk()
    can=Canvas(fen,width=500,height=500,bg='ivory')
    can.pack(side=TOP,padx=4,pady=4)
    bou1=Button(fen, text='cible 1', command=dessin1)
    bou1.pack(side=LEFT,padx=4,pady=4)
    bou2=Button(fen, text='cible 2', command=dessin2)
    bou2.pack(side=RIGHT,padx=4,pady=4)
    fen.mainloop()
    """Par instanciation de la classe Tk() on crée un objet fenêtre désigné par fen.
    Par instanciation de la classe Canvas() on crée un objet canevas esclave de fen,
    désigné par can, de largeur 500, de hauteur 500 et dont la couleur de fond est ivoire. L'origine du repère est place en haut a gauche.
    Dans la méthode pack(), l'option side, qui peut recevoir les valeurs TOP,BOTTOM,LEFT,RIGHT ,
    permet de pousser le widget du cote correspondant dans la fenetre, les options padx et pady permettent de réserver un petit espace autour du widget;
    cet espace est exprimé en nombre de pixels, padx réserve un espace à gauche et à droite du widget, pady réserve un espace au-dessus et au-dessous du widget.
    Les deux boutons, bou1 et bou2, objets esclaves de fen, commandent l'affichage des deux dessins, en appelant les fonctions dessin1() et dessin2().
    Enfin, l'instruction fen.mainloop(), permet le démarrage du réceptionnaire d'événements associé à la fenêtre,
    en cliquant sur un bouton, la commande qui lui est associée sera exécutée."""
