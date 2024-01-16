'''

ATTENTION LES FONCTIONCS MARCHENT CHACUNES, MAIS PAS LE CODE ENTIER

'''

import requests
import json
import os
import time
import urllib.request
import folium
import matplotlib.pyplot as plt
import numpy as np


os.environ["HTTP_PROXY"]="http://cache.univ-pau.fr:3128"
os.environ["HTTPS_PROXY"]="https://cache.univ-pau.fr:3128"




with open(r"/home/supervisor/Documents/controltower_reduit", "r") as fichier:
   lines = len(fichier.readlines())


f = open("/home/supervisor/Documents/controltower_reduit", "r")




################################## RECUPERATION d'IP


def prendip(ligne): #Récupère les ips des différentes lignes
   ip=""
   for elt in str(ligne):
       if  elt != " ":
           ip+=elt
       else:
           return ip
      
def listeip(longueur):
   ip_total = []
   ligne = f.readline()
   for i in range(longueur):
       ip_total.append(prendip(ligne))
       ligne = f.readline()
   return ip_total


################################## RECUPERATION DE DATES


def prend_date():
   e = open("/home/supervisor/Documents/controltower_reduit", "r")
   listedate = []
   for elt in e :
       b = elt.split(" ")
       listedate.append(b[3])
   return listedate




def date_uniquement(liste):
   tabdate = []
   x = ""
   for elt in liste:
       x = ""
       for i in range(1,12):
           x += elt[i]
       tabdate.append(x)
   return tabdate


################################## CREATION DE GRAPHES EN BAR (POUR LES CONNEXIONS/IP)


def diagramme(liste_a_traiter):
   tabdiag = []
   for elt in ip_sans_occ:
       x = liste_a_traiter.count(elt)
       tabdiag.append(x)
   return tabdiag




################################## CREATION DE GRAPHES basique (POUR LES CONNEXIONS/DATES)


def jours_connexion(liste_a_traiter):
   tabdiag = []
   for elt in list(set(liste_dates)):
       x = liste_a_traiter.count(elt)
       tabdiag.append(x)
   return tabdiag


def sans_doublon(liste):
   tab=[]
   for i in liste:
       if i not in tab:
           tab.append(i)
   return tab
      
print(sans_doublon(liste_dates))


################################## PARTIE SUR FOLIUM


def lireip(liste):
   URL = "http://ip-api.com/json/"
   tab = []
   for elt in liste:
       time.sleep(0.5)
       x = urllib.request.urlopen(URL + elt)
       rx = x.read()
       jx = json.loads(rx)
       long = jx["lon"]
       lat = jx["lat"]
       tab.append([elt,lat,long])
   return tab
absc = np.array(ip_sans_occ)
print(absc)


ordo = np.array(diagramme(ip_avec_occ))
print(ordo)


plt.bar(absc,ordo)
plt.title("Diagramme des connexions / IP")
plt.show()cc = list(set(IP_finales))


longlat = lireip(ip_sans_occ)


m = folium.Map(location=(53.0,9.0))


def placepoints(tab):
   for pts in tab:
       folium.Marker([pts[1],pts[2]],tooltip="cliquez pour ip", popup=pts, icon=folium.Icon(color="red"),).add_to(m)
      
placepoints(longlat)


################################## MAIN CODE

liste_dates = date_uniquement(prend_date())
IP_finales = listeip(lines-1)


################################## AFFICHAGE DES GRAPHES

################# GRAPHES EN PLOT


jours = np.array(sans_doublon(liste_dates))
nbr_connexion = np.array(jours_connexion(liste_dates))


plt.plot(jours, nbr_connexion)
plt.title("Diagramme des connexions / jours")
plt.show()


################# GRAPHES EN BAR


absc = np.array(ip_sans_occ)
print(absc)


ordo = np.array(diagramme(ip_avec_occ))
print(ordo)


plt.bar(absc,ordo)
plt.title("Diagramme des connexions / IP")
plt.show()



m.save("/home/supervisor/Documents/map.html")
