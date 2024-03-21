from tkinter import *


exemple_tableau = {"date":0, "heure":1, "id_capteur":2, "valeur":3, "type":4}

def nvligne(date, heure, id_capteur, valeur, type, tab ): #ajouter une ligne au tableau
   ligne = [date, heure, id_capteur, valeur, type]
   tab.append(ligne)
   return tab


def afficher(tab, dico):
   for i in range(len(tab)):
       print(f'Date : {tab[i][dico["date"]][2]}/{tab[i][dico["date"]][1]}/{tab[i][dico["date"]][0]} - Heure : {tab[i][dico["heure"]][0]}:{tab[i][dico["heure"]][1]}:{tab[i][dico["heure"]][2]} \t [Sequences : {tab[i][dico["id_capteur"]]}] -> Valeur : {tab[i][dico["valeur"]]} {tab[i][dico["type"]]}')

def filtrage(tab, filtre, id): #filtre en fonction d'un indice mis dans filtre
   temptab = []
   for i in range(len(tab)):
       if tab[i][id] == filtre:
           temptab.append(tab[i])
   return temptab


def add_filter(tab_a_filtre, filtre, id_filtre, tableau_deja_filtre): #fais le lien entre le filtre et le tableau
   tableau_deja_filtre = filtrage(tab_a_filtre, filtre, id_filtre)
   return tableau_deja_filtre


def tri_chrono(tab):
   for i in range(len(tab)-1):
       if tab[i][exemple_tableau["date"]] > tab[i + 1][exemple_tableau["date"]]:
           # On echange les deux elements
           tab[i], tab[i + 1] = tab[i + 1],tab[i]
       if tab[i][exemple_tableau["date"]] == tab[i + 1][exemple_tableau["date"]] and tab[i][exemple_tableau["heure"]] > tab[i + 1][exemple_tableau["heure"]]:
           tab[i], tab[i + 1] = tab[i + 1],tab[i]
   return tab



#----------------MAIN----------------#

def main(dico):
   
   exemple_tableau = dico

   print("start \n")

   tableau = []
   tableau_filtre = []


   nvligne((1185,1,3), (6,57,6), "TGH", 25,"humidite", tableau) #ligne1
   nvligne((1985,12,12), (10,5,1), "ABC", 10,"température", tableau)  #ligne2
   nvligne((1985,12,12), (1,50,1), "ABC", 5,"température", tableau) #ligne3
   nvligne((2000,12,12), (1,50,1), "KDK", 0,"température", tableau) #ligne3
   
   #Affiche tableau
   print("\tTableau de base")
   afficher(tableau, exemple_tableau)
   
   #Filtres pour avoir uniquement les tableau contenant le filtre
   print("\n\t Tableau 1 filtré avec 'id_capteur' et le Tableau 2 avec 'heure'")
   afficher(add_filter(tableau, "ABC", exemple_tableau["id_capteur"] ,tableau_filtre), exemple_tableau)
   afficher(add_filter(tableau, (1,50,1), exemple_tableau["heure"] ,tableau_filtre), exemple_tableau)
   
   #tri chronologique par date et heure
   print("\n\tTableau trié dans l'ordre chronoogique")
   afficher(tri_chrono(tableau), exemple_tableau) #tableau et dico
   
   print("\n stop")

main(exemple_tableau)

def menu(dico):
   
   exemple_tableau = dico
   
   tableau = []
   
   
   choice = str(input("A : Créer un ligne \nQ : Quitter\n"))
   while choice != "Q":
      if choice == "A":
         nbr_li = int(input("nombre de ligne à ajouter "))
         for i in range(nbr_li):
            print(f'\tLigne {i}')
            
            date = input("Année "), input("Mois "), input("Jour ")
            heure = input("Heure (HH) "), input("Minutes (MM) "), input("Secondes (SS) ")
            idcap = str(input("ID du Capteur "))
            valcap = input("Valeur du capteur ")
            type_cap = input("Type du capteur ")
            
            nvligne(date, heure, idcap, valcap, type_cap, tableau)
            
         afficher(tableau, exemple_tableau)
         choice = str(input("A : Créer un ligne \nB : Filtrer un tableau \nC : Trier un Tableau Chronologiquement \nQ : Quitter \n"))
      
      if choice == "B":
         tableau_filtre = []
         filtre = str(input("Quel champ filtrer :\n -date\n-heure\n-id_capteur\n-valeur\n-type\n"))
         val_filtre = input("Valeur du filtre ")
         
         if filtre == "date":
            date = input("Année "), input("Mois "), input("Jour ")
            afficher(add_filter(tableau, val_filtre, exemple_tableau[filtre] ,tableau_filtre), exemple_tableau)
            
         if filtre == "heure":
            heure = input("Heure (HH) "), input("Minutes (MM) "), input("Secondes (SS) ")
            afficher(add_filter(tableau, val_filtre, exemple_tableau[filtre] ,tableau_filtre), exemple_tableau)
            
         if filtre == "id_capteur" or "type":
            afficher(add_filter(tableau, str(val_filtre), exemple_tableau[filtre] ,tableau_filtre), exemple_tableau)
           
         if filtre == "valeur" :
            afficher(add_filter(tableau, int(val_filtre), exemple_tableau[filtre] ,tableau_filtre), exemple_tableau)
            
         else:
            print("\nERROR\n")
         choice = str(input("A : Créer un ligne \nB : Filtrer un tableau \nC : Trier un Tableau Chronologiquement \nQ : Quitter \n"))
      
      if choice == "C":
         afficher(tri_chrono(tableau), exemple_tableau)   
         choice = str(input("A : Créer un ligne \nB : Filtrer un tableau \nC : Trier un Tableau Chronologiquement \nQ : Quitter \n"))

      
   
   print("\nSTOP\n")  
      
   
def menu_tk(dico):
   
   affmenu = Tk()
   affmenu.geometry("600x250")
   
   def close(top):
      top.destroy()
   
   def popup():
      top = Toplevel(affmenu)
      top.geometry("750x250")
      
      val = Entry(top, width=25)
      val.pack()
      
      entry = Button(top, text="OK", command=lambda:close(top))
      entry.pack(pady=5, side=TOP)

   
   exemple_tableau = dico

   
   add_val = Button(affmenu, text="Ajouter une ligne", height=4, width=300, command=popup)
   add_val.pack()
   
   
   ##############################NOT FINISHED
   
   
   affmenu.mainloop()
   
menu_tk(exemple_tableau)
