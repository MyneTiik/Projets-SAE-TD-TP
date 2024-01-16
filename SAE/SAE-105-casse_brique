from tkinter import *

def deplacement():
    global dx, dy
    if canvas.coords(balle1)[3]>400: #collision_bas
        label = Label( tk, text="PERDU !")  #Ecran de défaite
        label.pack()    #fait apparaitre le texte
        canvas.delete(balle1) #supprime la balle (évite les problèmes)
    if canvas.coords(balle1)[3]<20: #collision_haut
        dy = -1*dy
    if canvas.coords(balle1)[2]>500: #collision_droit
        dx = -1*dx
    if canvas.coords(balle1)[0]< 0: #collision_gauche
        dx = -1*dx

    #Test de la collision avec la raquette par coordonnees:
    if (canvas.coords(balle1)[3]>canvas.coords(raquette)[1]) and (canvas.coords(balle1)[0]<canvas.coords(raquette)[2]) and (canvas.coords(balle1)[2]>canvas.coords(raquette)[0]):
        dy=-1*dy
    #Test de la collision avec la raquette à gauche et à droite
    if canvas.coords(raquette)[2]>500: #collision_droit
        canvas.move(raquette,-10,0)
    if canvas.coords(raquette)[0]< 0: #collision_gauche   
        canvas.move(raquette,10,0)

    #Collistion + destricution des briques
    coll = canvas.find_overlapping(canvas.coords(balle1)[0],canvas.coords(balle1)[1],canvas.coords(balle1)[2],canvas.coords(balle1)[3])
    print(coll)
    if len(coll)>=2 : #c'est une collision
        if coll[1]>=3 : #c'est une brique
            canvas.delete(coll[1])
            dy = -1 * dy #balle part en sens inverse quand elle touche une brique

    #On deplace la balle :
    canvas.move(1,dx,dy)
    #On repete cette fonction
    tk.after(20,deplacement)

def droite(event):
    canvas.move(raquette,15,0)
def gauche(event):
    canvas.move(raquette,-15,0)

Pos_X=150
Pos_Y=150
dx=4
dy=4

#On cree une fenetre et un canevas:
tk = Tk()
canvas = Canvas(tk,width = 500, height = 400 , bd=0, bg="white")
canvas.pack(padx=10,pady=10)

#Creation  d'un bouton "Quitter":
Bouton_Quitter=Button(tk, text ='Quitter', command = tk.destroy)
#On ajoute l'affichage du bouton dans la fenêtre tk:
Bouton_Quitter.pack()

#On cree une balle:
balle1 = canvas.create_oval(Pos_X,Pos_Y,Pos_X+20,Pos_Y+20,fill='red')

#On cree une raquette:
raquette = canvas.create_rectangle(200,380,300,390,fill='red')
#On associe la touche droite du clavier a la fonction droite():
canvas.bind_all('<Right>', droite)
#On associe la touche gauche du clavier a la fonction gauche():
canvas.bind_all('<Left>', gauche)
#creation d'une fonction briques

def briques():
    for yb in range(0, 100, 20):
        for xb in range(0, 500, 50):
            if (xb // 50) % 2 == (yb // 20) % 2: #colonne paires et lignes pair donc une case sur deux
                brique = canvas.create_rectangle(xb, yb, xb + 50, yb + 20, fill='yellow')
            else:
                brique = canvas.create_rectangle(xb, yb, xb + 50, yb + 20, fill='red')

deplacement()

briques()


canvas.move(balle1,dx,dy)


#On lance la boucle principale:
tk.mainloop()
