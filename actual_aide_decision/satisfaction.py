import math
import statistics
import numpy as np 
import matplotlib.pyplot as plt 
from mariage_stable import *

#entier pour voeux_ponderes, =1 lineaire, =2 quadratique et =3 binaire (satisfaction totale ou nulle) 
def satisfaction_perso (final_affectation, pref_etudiants, pref_ecoles, voeux_ponderes):

    satisfaction_etudiants = []
    satisfaction_ecoles = []
    nb = len(pref_etudiants)

    #pour l'option 3 on fixe un seuil pour la satisfaction totale 
    mean = int(nb/2)
    #l'index commence à 0 
    if nb%2 == 0:
        mean-=1

    for i in range(nb):
        
        pref_etu = pref_etudiants[i]
        pref_eco = pref_ecoles[i]

        clef = [c for c, v in final_affectation.items() if v == i+1]
        affectation_etu = clef[0]
        affectation_eco = final_affectation[i+1]

        if voeux_ponderes == 1 :
            s_etu = voeux_ponderes_lineaire(nb, pref_etu, affectation_etu)
            s_eco = voeux_ponderes_lineaire(nb, pref_eco, affectation_eco)
        elif voeux_ponderes == 2 : 
            s_etu = voeux_ponderes_quadratique(nb, pref_etu, affectation_etu)
            s_eco = voeux_ponderes_quadratique(nb, pref_eco, affectation_eco)
        elif voeux_ponderes == 3 :
            if pref_etu.index(affectation_etu) < mean :
                s_etu = 100
            else :
                s_etu = 0
            if pref_eco.index(affectation_eco) < mean : 
                s_eco = 100
            else : 
                s_eco = 0

        #satisfaction en pourcentage 
        satisfaction_etudiants.append(s_etu)
        satisfaction_ecoles.append(s_eco)
    
    return satisfaction_etudiants, satisfaction_ecoles

def satisfaction_partielle(final_affectation, pref_etudiants, pref_ecoles, voeux_ponderes):

    satisfaction_etudiants, satisfaction_ecoles = satisfaction_perso (final_affectation, pref_etudiants, pref_ecoles, voeux_ponderes)

    #on réalise les moyennes des satisfactions pour la classe des étudiants puis celle des écoles 
    return statistics.mean(satisfaction_etudiants), statistics.mean(satisfaction_ecoles)


#voeux pondérés : premier voeux vaut nb, deuxieme vaut nb-1, et dernier vaut 1 
def voeux_ponderes_lineaire(nb_tt, pref, affect):
    p = nb_tt - pref.index(affect)

    return  p*100/nb_tt

def voeux_ponderes_quadratique(nb_tt, pref, affect):
    x = nb_tt - pref.index(affect) 
    p = math.pow(x, 2)

    return p*100/math.pow(nb_tt,2)
#Etude du nombre de participants dans le mariage stable 

#satif_mode entier entre 1, 2 et 3 pour satisfaction_partiel 
#max_nbchoix nombre de choix maximum
def etude_nb_choix(satif_mode, max_nbchoix):

    #pour avoir le max_nbchoix compris 
    max_nbchoix += 1 

    #pour nb_choix=1 on sait que la satisfaction est à 100% 
    mean_satif_etu_list = [100]
    mean_satif_eco_list = [100]

    for i in range(2, max_nbchoix):

        #on va faire la moyenne des 5 mariages stables pour un i ATTENTION SI ON VEUT L AUGMENTER IL FAUT SANS DOUTE ENLEVER I=2 
        mean_satif_etu = 0
        mean_satif_eco = 0

        for j in range(5):
            etu,eco = generateurPref(i,i)
            f_affectation = mariageStable(etu, eco)
            #on obtient une moyenne pour chaque classe 
            satif_etu, satif_eco = satisfaction_partielle(f_affectation, etu, eco, satif_mode)
            mean_satif_etu += satif_etu
            mean_satif_eco += satif_eco
        #division par le nombre de generateurs etudiés, ici 5 
        mean_satif_etu_list.append(mean_satif_etu/5)
        mean_satif_eco_list.append(mean_satif_eco/5)
    
    #on a donc trois listes pour le plot, une pour pour les abscisses et deux pour les ordonnées (une pour étudiants et une pour écoles)
    nbchoix_evolution = range(1, max_nbchoix)

    #
    plt.figure(figsize=(15,5))
    plt.axes().set(facecolor=("#f8ffff"))
    plt.plot(nbchoix_evolution, mean_satif_eco_list, color=(.6,.9,.7,1.),label='Ecoles')
    plt.plot(nbchoix_evolution, mean_satif_eco_list,'o', color=(.6,.9,.7,1.))

    #on garde ca pour d'autre plot 
    #plt.plot(nbchoix_evolution, mean_satif_etu_list, color=(.6,.9,.9,1.),label='batch_size = 64')
    #plt.plot(nbchoix_evolution, mean_satif_etu_list,'o', color=(.6,.9,.9,1.))

    plt.plot(nbchoix_evolution, mean_satif_etu_list, color=(1.,0.8,.6,1.),label='Etudiants')
    plt.plot(nbchoix_evolution, mean_satif_etu_list,'o', color=(1.,0.8,.6,1.))

    plt.legend()
    plt.xlabel("Nombre de choix")
    plt.ylabel("Satisfaction")
    #plt.ylim(0,110)
    plt.grid(axis="both", linewidth=1, color=("#e4eaea"))
    title = "Evolution de la satisfaction selon le nombre de choix"
    plt.title(title)
    
    plt.show()


#Etude de voeux identiques entre des etudiants pour avantager certains voeux 
def etude_popularite_alldiff(satif_mode, nb_personne):

    #pour avoir le nb_personne compris 
    nb_personne += 1 

    #pour nb_choix=1 on sait que la satisfaction est à 100% 
    satif_etu_list = []
    satif_eco_list = []
    list_id = list(range(1, nb_personne))

    for k in range(3):

        etu,eco = generateurPrefAllDiff(nb_personne-1)

        f_affectation = mariageStable(etu, eco)
        #on obtient une moyenne pour chaque classe 
        satisfaction_etudiants, satisfaction_ecoles = satisfaction_perso (f_affectation, etu, eco, satif_mode)
        satif_etu_list.append(satisfaction_etudiants)
        satif_eco_list.append(satisfaction_ecoles)
    
    plt.hist(satif_etu_list, color = ['yellow', 'green', 'red'], label=['Jeu de données 1', 'Jeu de données 2', 'Jeu de données 3'], histtype='bar')

    plt.legend()
    plt.ylabel("Etudiants")
    plt.xlabel("Satisfaction")
    plt.grid(axis="both", linewidth=1, color=("#e4eaea"))
    title = "Satisfaction des étudiants ayant un premier voeu différent"
    plt.title(title)
    
    plt.show()

    plt.hist(satif_eco_list, color = ['yellow', 'green', 'red'], label=['Jeu de données 1', 'Jeu de données 2', 'Jeu de données 3'], histtype='bar')

    plt.legend()
    plt.ylabel("Ecoles")
    plt.xlabel("Satisfaction")
    plt.grid(axis="both", linewidth=1, color=("#e4eaea"))
    title = "Satisfaction des écoles ayant un premier voeu différent"
    plt.title(title)
    
    plt.show()


#Etude de voeux identiques entre des etudiants pour avantager certains voeux 
#sans la moyenne sur 5 jeux de données
#satif_mode entier entre 1, 2 et 3 pour satisfaction_partielle 
#nb_personne nombre de personnes ayant le même choix 
def etude_popularite_sans_moyenne(satif_mode, nb_personne):

    #pour avoir le nb_personne compris 
    nb_personne += 1 

    #pour nb_choix=1 on sait que la satisfaction est à 100% 
    satif_etu_list = []
    satif_eco_list = []
    nb_personne_identique = range(2, nb_personne)

    for j in nb_personne_identique:

        

        etu,eco = generateurPref(nb_personne-1,nb_personne-1)
        
        #ICI le modifs
        # premiere boucle voeux identiques entre 2 pers 
        # deuxieme boucle voeux identiques entre 3 pers 
        # ...

        etu_identique = etu[0]
        for i in range(1, j):
            #on fait les memes voeux juste pour la classe etudiant 
            etu[i]= etu_identique

        print(etu)
        print(eco)
        f_affectation = mariageStable(etu, eco)
        print(f_affectation)
        #on obtient une moyenne pour chaque classe 
        satisfaction_etudiants, satisfaction_ecoles = satisfaction_perso (f_affectation, etu, eco, satif_mode)
        satif_etu, satif_eco = satisfaction_partielle(f_affectation, etu, eco, satif_mode)
        satif_etu_list.append(satif_etu)
        satif_eco_list.append(satif_eco)

    
    #on a donc trois listes pour le plot, une pour pour les abscisses et deux pour les ordonnées (une pour étudiants et une pour écoles)
    
    print("Satif etu : ",satisfaction_etudiants)
    print("Satif eco : ",satisfaction_ecoles)
    
    plt.figure(figsize=(15,5))
    plt.axes().set(facecolor=("#f8ffff"))
    plt.plot(nb_personne_identique, satif_eco_list, color=(.6,.9,.7,1.),label='Ecoles')
    plt.plot(nb_personne_identique, satif_eco_list,'o', color=(.6,.9,.7,1.))

    #on garde ca pour d'autre plot 
    #plt.plot(nbchoix_evolution, mean_satif_etu_list, color=(.6,.9,.9,1.),label='batch_size = 64')
    #plt.plot(nbchoix_evolution, mean_satif_etu_list,'o', color=(.6,.9,.9,1.))

    plt.plot(nb_personne_identique, satif_etu_list, color=(1.,0.8,.6,1.),label='Etudiants')
    plt.plot(nb_personne_identique, satif_etu_list,'o', color=(1.,0.8,.6,1.))

    plt.legend()
    plt.xlabel("Nombre de personnes ayant des voeux identiques")
    plt.ylabel("Satisfaction")
    plt.grid(axis="both", linewidth=1, color=("#e4eaea"))
    title = "Evolution de la satisfaction selon le nombre de voeux identiques"
    plt.title(title)
    
    plt.show()

    return printAffectation(f_affectation, len(f_affectation))

    
#Etude de voeux identiques entre des etudiants pour avantager certains voeux 
#satif_mode entier entre 1, 2 et 3 pour satisfaction_partielle 
#nb_personne nombre de personnes ayant le même choix 
def etude_popularite(satif_mode, nb_personne):

    #pour avoir le nb_personne compris 
    nb_personne += 1 

    #pour nb_choix=1 on sait que la satisfaction est à 100% 
    mean_satif_etu_list = []
    mean_satif_eco_list = []
    nb_personne_identique = range(2, nb_personne)

    for j in nb_personne_identique:

        #on va faire la moyenne des 5 mariages stables pour un i ATTENTION SI ON VEUT L AUGMENTER IL FAUT SANS DOUTE ENLEVER I=2 
        mean_satif_etu = 0
        mean_satif_eco = 0

        for a in range(3):

            etu,eco = generateurPref(nb_personne-1,nb_personne-1)
            
            #ICI le modifs
            # premiere boucle voeux identiques entre 2 pers 
            # deuxieme boucle voeux identiques entre 3 pers 
            # ...

            etu_identique = etu[0]
            for i in range(1, j):
                #on fait les memes voeux juste pour la classe etudiant 
                etu[i]= etu_identique

            print(etu)
            print(eco)
            f_affectation = mariageStable(etu, eco)
            print(f_affectation)
            #on obtient une moyenne pour chaque classe 
            satif_etu, satif_eco = satisfaction_partielle(f_affectation, etu, eco, satif_mode)
            mean_satif_etu += satif_etu
            mean_satif_eco += satif_eco
        #division par le nombre de generateurs etudiés, ici 5 
        mean_satif_etu_list.append(mean_satif_etu/5)
        mean_satif_eco_list.append(mean_satif_eco/5)


    
    #on a donc trois listes pour le plot, une pour pour les abscisses et deux pour les ordonnées (une pour étudiants et une pour écoles)
    
    plt.figure(figsize=(15,5))
    plt.axes().set(facecolor=("#f8ffff"))
    plt.plot(nb_personne_identique, mean_satif_eco_list, color=(.6,.9,.7,1.),label='Ecoles')
    plt.plot(nb_personne_identique, mean_satif_eco_list,'o', color=(.6,.9,.7,1.))

    #on garde ca pour d'autre plot 
    #plt.plot(nbchoix_evolution, mean_satif_etu_list, color=(.6,.9,.9,1.),label='batch_size = 64')
    #plt.plot(nbchoix_evolution, mean_satif_etu_list,'o', color=(.6,.9,.9,1.))

    plt.plot(nb_personne_identique, mean_satif_etu_list, color=(1.,0.8,.6,1.),label='Etudiants')
    plt.plot(nb_personne_identique, mean_satif_etu_list,'o', color=(1.,0.8,.6,1.))

    plt.legend()
    plt.xlabel("Nombre de personnes ayant des voeux identiques")
    plt.ylabel("Satisfaction")
    plt.grid(axis="both", linewidth=1, color=("#e4eaea"))
    title = "Evolution de la satisfaction selon le nombre de voeux identiques"
    plt.title(title)
    
    plt.show()


dico = {1:2, 2:3, 3:1}
p_etu = [[1,2,3], [2,3,1], [1,3,2]]
p_eco = [[3,2,1], [2,3,1], [1,3,2]]
s_etu,s_eco = satisfaction_perso(dico, p_etu, p_eco, 2)
print(s_etu, s_eco)


