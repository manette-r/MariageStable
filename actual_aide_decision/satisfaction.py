import math
import statistics

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
            satisfaction_etudiants.append(100) if pref_etu.index(affectation_etu) < mean else satisfaction_etudiants.append(0)
            satisfaction_ecoles.append(100) if pref_eco.index(affectation_eco) < mean else satisfaction_ecoles.append(0)

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


dico = {1:2, 2:3, 3:1}
p_etu = [[1,2,3], [2,3,1], [1,3,2]]
p_eco = [[3,2,1], [2,3,1], [1,3,2]]
s_etu,s_eco = satisfaction_perso(dico, p_etu, p_eco, 2)
print(s_etu, s_eco)


