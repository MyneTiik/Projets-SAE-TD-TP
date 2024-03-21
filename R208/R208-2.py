def nvligne(nom, prenom, sexe, ddn, tab ): #ajouter une ligne au tableau
   ligne = [nom, prenom, sexe, ddn]
   tab.append(ligne)
   return tab

def ascendance(enfant, parent, tableau):
   tableau.append((enfant,parent))
   return tableau
   

def afficher(tab):
   for i in range(len(tab)):
       print(f'Date de naissance : {tab[i][3][2]}/{tab[i][3][1]}/{tab[i][3][0]} \tNom : {tab[i][0]} - Prenom : {tab[i][1]} (Sexe : {tab[i][2]})')
   print('\n')

def afficher_des_asc(tab):
   for i in range(len(tab)):
       print(tab[i])
   print('\n')


def cherche_id(tab):
   for i in range(len(tab)):
      print(i, f'|| Date de naissance : {tab[i][3][2]}/{tab[i][3][1]}/{tab[i][3][0]} \tNom : {tab[i][0]} - Prenom : {tab[i][1]} (Sexe : {tab[i][2]})')

################################################################################################################################################################

def parents(tab, lien, personne,vide,old=0):
   for i in lien:
      if i[0] == personne:
         if old == 0:
            vide.append(f'Parent : {tab[i[1]][0]} - {tab[i[1]][1]}')
         
         if old == 1:
            vide.append("Grand "+f'Parent : {tab[i[1]][0]} - {tab[i[1]][1]}')
         
         if old > 1:
            vide.append("Arrière "*(old-1)+f'Grand Parent : {tab[i[1]][0]} - {tab[i[1]][1]}')
            
         parents(tab, lien, i[1],vide, old+1)
   vide.sort()
   return vide

################################################################################################################################################################

def enfants(tab, lien, personne,vide,old=0):
   for i in lien:
      if i[1] == personne:
         if old == 0:
            vide.append(f'Fils/Fille : {tab[i[0]][0]} - {tab[i[0]][1]}')
         
         if old == 1:
            vide.append("-Petit "+f'Fils/Fille : {tab[i[0]][0]} - {tab[i[0]][1]}')
         
         if old > 1:
            vide.append("-Arrière "*(old-1)+f'Petit Fils : {tab[i[0]][0]} - {tab[i[0]][1]}')
            
         enfants(tab, lien, i[0],vide,old+1)
         
   vide.sort()
   return vide  


def fraternite(tab, lien, personne) :
   parents_l = []
   frat = []
   for i in lien:
      if i[0] == personne:
         parents_l.append(i[1])
   
   for j in parents_l:
      for k in lien:
         if k[1] == j and k[0] != personne:
            if tab[k[0]][2] == 'H':
               print(f'Frère : {tab[k[0]][1]} {tab[k[0]][0]}')
            if tab[k[0]][2] == 'F':
               print(f'Soeur : {tab[k[0]][1]} {tab[k[0]][0]}')
   return ("\n")
            
def tri_alph(tab):
   for i in range(len(tab)-1):
      bulle = 0
      for j in range(len(tab)-1):
         if tab[j][0] > tab[j+1][0]:
            tab[j], tab[j + 1] = tab[j + 1],tab[j]
            bulle = 1
            
         if tab[j][0] == tab[j+1][0] and tab[j][1] > tab[j+1][1]:
            tab[j], tab[j + 1] = tab[j + 1],tab[j]
            bulle = 1
            
      if bulle == 0:
         break
      
   return tab

def tri_age(tab):
   for i in range(len(tab)-1):
      bulle = 0
      for j in range(len(tab)-1):
         if tab[j][3] > tab[j+1][3]:
            tab[j], tab[j + 1] = tab[j + 1],tab[j]
            bulle = 1
            
      if bulle == 0:
         break
      
   return tab    
               
tableau = []
lien_parentee = []

nvligne('delaparnade', 'alexandre', 'H', (1995,12,12), tableau)
nvligne('dupont', 'martin', 'H', (1940,10,2), tableau)
nvligne('pasdupond', 'martine', 'F', (1941,4,6), tableau)
nvligne('demars', 'thibault', 'H', (2000,1,1), tableau)
nvligne('leonart', 'annie', 'F', (1950,7,7), tableau)
nvligne('eren', 'yaeger', 'H', (1999,11,9), tableau)
nvligne('akim', 'bo', 'H', (2000,1,1), tableau)
nvligne('tantine', 'bernadette', 'F', (2000,11,1), tableau)
nvligne('d Arc', 'Jeanne', 'F', (2056,6,6), tableau)

ascendance(5, 1, lien_parentee)
ascendance(5, 2, lien_parentee)
ascendance(3, 5, lien_parentee)
ascendance(3, 4, lien_parentee)
ascendance(0, 3, lien_parentee)
ascendance(6, 3, lien_parentee)
ascendance(0, 7, lien_parentee)
ascendance(8, 3, lien_parentee)

#afficher(tableau)
#cherche_id(tableau)

#print(parents(tableau, lien_parentee, 0))
#print(enfants(tableau, lien_parentee, 2))

#print(fraternite(tableau,lien_parentee, 0))

#afficher(tri_alph(tableau))

#afficher(tri_age(tableau))

def menu():
   
   print("\nSTART\n")
   
   tableau = []
   lien_parentee = []

   nvligne('delaparnade', 'alexandre', 'H', (1995,12,12), tableau)
   nvligne('dupont', 'martin', 'H', (1940,10,2), tableau)
   nvligne('pasdupond', 'martine', 'F', (1941,4,6), tableau)
   nvligne('demars', 'thibault', 'H', (2000,1,1), tableau)
   nvligne('leonart', 'annie', 'F', (1950,7,7), tableau)
   nvligne('eren', 'yaeger', 'H', (1999,11,9), tableau)
   nvligne('akim', 'bo', 'H', (2000,1,1), tableau)
   nvligne('tantine', 'bernadette', 'F', (2000,11,1), tableau)
   nvligne('d Arc', 'Jeanne', 'F', (2056,6,6), tableau)

   ascendance(5, 1, lien_parentee)
   ascendance(5, 2, lien_parentee)
   ascendance(3, 5, lien_parentee)
   ascendance(3, 4, lien_parentee)
   ascendance(0, 3, lien_parentee)
   ascendance(6, 3, lien_parentee)
   ascendance(0, 7, lien_parentee)
   ascendance(8, 3, lien_parentee)
   
   afficher(tableau)
   choice = str(input("\nA : Trouver l'ascendance \nB : Trouver la Déscendance \nC : Trouver la Fraterie \nD : Tri de tableau (ALPHABETIQUE) \nE : Tri de tableau (CHRONOLOGIQUE) \nQ : Quitter \n"))
   while choice != "Q":
      if choice == "A": 
         
         cherche_id(tableau)
         
         idenf = int(input("De qui voulez vous l'ascendance ? (id) "))
         print("\n")
         form = []
         afficher_des_asc(parents(tableau, lien_parentee, idenf, form))
         
         choice = str(input("\nA : Trouver l'ascendance \nB : Trouver la Déscendance \nC : Trouver la Fraterie \nD : Tri de tableau (ALPHABETIQUE) \nE : Tri de tableau (CHRONOLOGIQUE) \nQ : Quitter \n"))
          
      if choice == "B":
         
         cherche_id(tableau)
         
         idpar = int(input("\nDe qui voulez vous la descendance ? (id) "))
         print("\n")
         form = []
         afficher_des_asc(enfants(tableau, lien_parentee, idpar, form))
         
         choice = str(input("\nA : Trouver l'ascendance \nB : Trouver la Déscendance \nC : Trouver la Fraterie \nD : Tri de tableau (ALPHABETIQUE) \nE : Tri de tableau (CHRONOLOGIQUE) \nQ : Quitter \n"))
      
      if choice == "C":
         
         cherche_id(tableau)
         
         idfr = int(input("\nDe qui voulez vous la fraterie ? (id) "))
         print(fraternite(tableau,lien_parentee, idfr))

         choice = str(input("\nA : Trouver l'ascendance \nB : Trouver la Déscendance \nC : Trouver la Fraterie \nD : Tri de tableau (ALPHABETIQUE) \nE : Tri de tableau (CHRONOLOGIQUE) \nQ : Quitter \n"))

      if choice == "D":
         
         afficher(tri_alph(tableau))   
         choice = str(input("\nA : Trouver l'ascendance \nB : Trouver la Déscendance \nC : Trouver la Fraterie \nD : Tri de tableau (ALPHABETIQUE) \nE : Tri de tableau (CHRONOLOGIQUE) \nQ : Quitter \n"))

      if choice == "E":
         
         afficher(tri_age(tableau))   
         choice = str(input("\nA : Trouver l'ascendance \nB : Trouver la Déscendance \nC : Trouver la Fraterie \nD : Tri de tableau (ALPHABETIQUE) \nE : Tri de tableau (CHRONOLOGIQUE) \nQ : Quitter \n"))

      
   
   print("\nSTOP\n")        

menu()