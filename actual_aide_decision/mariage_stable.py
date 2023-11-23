
import random

#généralement nb_etu=nb_eco
def generateurPref(nb_etu,nb_eco):

  etudiants = [random.sample(range(1, nb_etu+1), nb_etu) for i in range(nb_etu)]
  ecole = [random.sample(range(1, nb_eco+1), nb_eco) for i in range(nb_eco)]

  return etudiants,ecole

def generateurPrefAllDiff(nb_pers): 
  etu,eco = generateurPref(nb_pers,nb_pers)

  #AllDiff seulement pour le premier voeu des Etudiants
  not_available = []
  for i in range(nb_pers):
      
      if etu[i][0] in not_available: 
          #alors on va changer le premier voeu avec le voeu suivant 
          searching = True
          j=1
          while searching : 
              if etu[i][j] in not_available : 
                  j+=1
              else :
                  #on echange 
                  buffer = etu[i][0]
                  etu[i][0] = etu[i][j]
                  etu[i][j] = buffer
                  not_available.append(etu[i][j])
                  searching = False

      else : 
          not_available.append(etu[i][0])
  return etu, eco

#en entrée les listes qu'on peut obtenir en sortie de generateurPref
def mariageStable(pref_etudiants, pref_ecole):

  #on copie les listes pour garder les informations à l'extérieur
  etu_copy = [x[:] for x in pref_etudiants]
  eco_copy = [x[:] for x in pref_ecole]

  nb = len(etu_copy)
  #liste d'attribution (index correspond à une ecole/eleve et valeur : 0 pas d'attribution, 1 : attribué)
  etudiant_attribution = [0]*nb
  ecole_attribution = [0]*nb

  #affectation finale : les clefs sont les etudiants et les valeurs les ecoles
  final_affectation = {}

  #Tant que l'affectation est disponible
  while 0 in etudiant_attribution:

    #premier etudiant
    i = 0
    #on cherche un etudiant sans attribution
    while etudiant_attribution[i] != 0:
      i+=1
    #on enlève son premier choix de la liste pour le traiter
    w = etu_copy[i].pop(0)

    #on vérifie que ce choix soit disponible pour affecter l'etudiant
    if ecole_attribution[w-1] == 0:
      final_affectation[w] = i+1
      etudiant_attribution[i] = 1 # etudiant affecté
      ecole_attribution[w-1] = 1 #ecole affecté
      print("Etudiant",i+1,"affecté à l'école:",w)
    else:
      #si l'école avait déjà un étudiant attribué alors on les compare
      print("Etudiant en attente:",i+1,"école :",w)
      etudiant_attribue = final_affectation[w]
      print("Etudiant actuel :",etudiant_attribue)

      # On doit regarder les préférences de l'école
      #Si l'ecole w préfère l'étudiant actuel à l'étudiant attribué
      #Sinon l'étudiant attribué et l'école garde leur affectation
      if (eco_copy[w-1].index(etudiant_attribue)>eco_copy[w-1].index(i+1)):

        #on affecte et précise qu'ils ne sont pas disponibles
        final_affectation[w] = i+1
        etudiant_attribution[i] = 1
        ecole_attribution[w-1] = 1

        #l'étudiant qui était attribué devient disponible
        etudiant_attribution[etudiant_attribue-1] = 0
        print("Etudiant",i+1,"affecté à l'école:",w)

  print("Les écoles ont toutes un élève : ",ecole_attribution) #[1,1,1]
  print("Les élèves ont tous une école : ",etudiant_attribution) #[1,1,1]
  return final_affectation

def printAffectation(affectation, nb):
  
  stringaffectation = ""
  for k in list(range(1, nb+1)):
    buffer_affectation = "\nEleve "+str(k)+" a été admis dans l'école "+str(affectation.get(k))+"."
    stringaffectation += buffer_affectation
    
  return stringaffectation


