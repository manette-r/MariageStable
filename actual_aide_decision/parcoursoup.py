import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox, Tk, Canvas, Entry, Text, Button, PhotoImage
from PIL import Image, ImageTk  # install pillow with pip: pip install pillow
import random
from mariage_stable import *;
from satisfaction import * ; 
import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

class FirstPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        #chargment de la photo
        load = Image.open("photo4.jpg")
        photo = ImageTk.PhotoImage(load,master=self)
       # Afficher l'image dans un label
        label_image = tk.Label(self, image=photo)
        label_image.image = photo
        label_image.place(x=0, y=0, relwidth=1, relheight=1)
        
        color2 = '#FC9F5B'
        color3 = '#65e7ff'
        color4 = 'WHITE'
        
        
        #Titre
        label = tk.Label(self,
                         text="ParcourSoup", 
                         font=("Aria Bold",50),
                         bg = color4)
       # label.place(relx=0.5, rely=0.1, anchor='n')
        label.pack(side = "top")
        
        
        #texte 
        texte_label = tk.Label(self, 
                               text="L'application ou l'avenir se dessine",
                               font=("Aria ",35),
                               bg = color4)
        #texte_label.place(relx=0.5, rely=0.5, anchor='center')
        texte_label.pack(side = "top")
        
        #bouton direction page 2
        Button = tk.Button(self, 
                           text= "Entrez votre préférence",
                           font=("Arial", 15,'bold'), 
                           command= lambda: controller.show_frame(SecondPage),
                           background = color4,
                           foreground=color2,
                           activebackground=color2,
                           activeforeground=color4,
                           highlightbackground= color3,
                           highlightthickness= 10,
                           highlightcolor= color4,
                           border= 1,
                           cursor='hand1'
                )
        Button.place(relx=0.1, rely=0.8, anchor='sw')
        
        #bouton direction page 3
        Button2 = tk.Button(self,
                            font=("Arial", 15), 
                            text= "Lancer la simulation", 
                            command= lambda: controller.show_frame(ThirdPage),
                            background = color4,
                            foreground=color2,
                            activebackground=color4,
                            activeforeground=color4,
                            highlightbackground= color3,
                            highlightthickness= 10,
                            highlightcolor= color4,
                            border= 1,
                            cursor='hand1')
        
        Button2.place(relx=0.9, rely=0.8, anchor='se')
        
 
class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
 
        color1 = '#FFA6A6'
        color2 = 'WHITE'
        
        #chargment de la photo
        load = Image.open("photo6.jpg")
        photo = ImageTk.PhotoImage(load,master=self)
        # Afficher l'image dans un label
        label_image = tk.Label(self, image=photo)
        label_image.image = photo
        label_image.place(x=0, y=0, relwidth=1, relheight=1)
        
        
        
        
        #Titre 
        label = tk.Label(self,text="Faites vos voeux", 
                         font=("Aria Bold",40),
                         bg = color2)
        #label.place(relx=0.5, rely=0.1, anchor='n')
        label.pack(side = 'top')
        
       
        label1 = tk.Label(self,text="Voeux 1 :", 
                          font=("Aria Bold",20),
                          bg = color1)
        label1.place(x=250, y=230)
        #Liste avec barre de défilement
        o = ttk.Combobox(self, values=["Université de Lyon", "Université de Montpellier", "Université de Toulouse"])
        o.place(x=450, y=230)
        
        
       
        label2 = tk.Label(self, text="Voeux 1 :",
                          font=("Aria ",20),
                          bg = color1)
        label2.place(x=250, y=280)
        o1 = ttk.Combobox(self, values=["Université de Lyon", "Université de Montpellier", "Université de Toulouse"])
        o1.place(x=450, y=280)
       
        
        
       
        label3 = tk.Label(self, text="Voeux 3 :",
                          font=("Aria ",20),
                          bg = color1)
        label3.place(x=250, y=330)
        o3 = ttk.Combobox(self, values=["Université de Lyon", "Université de Montpellier", "Université de Toulouse"])
        o3.place(x=450, y=330)
        
        
        
       
       
        #Bouton  redirection page 1
        Button = tk.Button(self, 
                           text="Valider", 
                           font=("Arial", 15),
                           command=lambda: controller.show_frame(FirstPage),
                           bg = 'WHITE')
        Button.place(x=450, y=500)
 
    
        #Bouton  redirection page 1
        Button = tk.Button(self, 
                           text="Retour à la page principale", 
                           font=("Arial", 15), 
                           command=lambda: controller.show_frame(FirstPage),
                           bg = 'WHITE')
        Button.place(relx=0.15, rely=0.9, anchor='s')
        
        def print_file () :                     # voir le chapitre sur les événements
            print(o.get())
 
class ThirdPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller 
        
        
       
        
        color2 = 'WHITE'
        
        #affichage de la photo
        load = Image.open("photo5.jpg")
        photo = ImageTk.PhotoImage(load,master=self)
       # Afficher l'image dans un label
        label_image = tk.Label(self, image=photo)
        label_image.image = photo
        label_image.place(x=0, y=0, relwidth=1, relheight=1)

        label = tk.Label(self,
                         text="A VOUS ", 
                         font=("Aria Bold",40),
                         bg = "WHITE")
        #label.place(relx=0.5, rely=0.1, anchor='n')
        label.pack(side='top')
        
        label1 = tk.Label(self,
                         text="DE JOUEZ !", 
                         font=("Aria Bold",40),
                         bg = "WHITE")
        #label.place(relx=0.5, rely=0.1, anchor='n')
        label1.pack(side='top')
        
        
         
        # Champs d'entrée
        self.label1 = tk.Label(self, 
                               text="Entrez le nombre d'étudiants : ",
                               font=("Aria Bold",15),
                               bg= color2                               )
        self.label1.place(relx=0.3, rely=0.3, anchor='n')
        
        #Initialisation des strings pour les afficher 
        self.nb_pref = tk.StringVar()
        self.result_etudiants = tk.StringVar()
        self.result_ecoles = tk.StringVar()
        
        self.var_entry = tk.Entry(self,
                                  textvariable=self.nb_pref,
                                  bg = color2)
        self.var_entry.place(relx=0.5, rely=0.3, anchor='n')
          
        generateur_button = tk.Button(self,
                                      text="Générer les préférences",
                                      command=self.generateurPrefContainer,
                                      font=("Arial", 15,'bold'),
                            
                                      background = "WHITE")
        generateur_button.place(relx=0.65, rely=0.4, anchor='n')


        #ici
        label_etudiants = tk.Label(self,
                                   text="Listes de voeux pour chaque étudiants : ",
                                   font=("Aria Bold",15),
                                   bg = color2) 
        
        label_etudiants.place(relx=0.3, rely=0.5, anchor='center')
        result_label_etudiants = tk.Label(self,
                                          textvariable=self.result_etudiants,
                                          bg = color2) 
        result_label_etudiants.place(relx=0.5, rely=0.5, anchor='center')


         #ici
        label_ecoles = tk.Label(self,
                                text="Listes de voeux pour chaque établissements : ",
                                font=("Aria Bold",15),
                                bg = color2) 
        
        
        label_ecoles.place(relx=0.3, rely=0.6, anchor='center')
        result_label_ecoles = tk.Label(self,
                                       textvariable=self.result_ecoles,
                                       bg = color2
                                       ) 
        result_label_ecoles.place(relx=0.5, rely=0.6, anchor='center')

        Button2 = tk.Button(self,
                            font=("Arial", 15), 
                            text= "Lancer la simulation", 
                            command= lambda: self.valider(self.result_etudiants, self.result_ecoles),
                            background = 'WHITE')
        Button2.place(relx=0.9, rely=0.85, anchor='se')
     
        Button = tk.Button(self, 
                           text="Retour à la page principale", 
                           font=("Arial", 10), 
                           command=lambda: controller.show_frame(FirstPage),
                           background= 'WHITE')
        Button.place(relx=0.15, rely=0.85, anchor='s')

    def generateurPrefContainer(self):
            
            if(self.nb_pref.get().isnumeric()):
                
                self.var_entry.select_clear()
                self.label1.config(fg='black')

                # Longueur 
                nb_etu = int(self.nb_pref.get())
                nb_eco = int(self.nb_pref.get())
                # Générer
                etudiants, ecole = generateurPref(nb_etu, nb_eco)

                self.result_etudiants.set(etudiants)
                self.result_ecoles.set(ecole)  
            else : 
                self.var_entry.select_clear()
                self.label1.config(fg='red')

    def valider(self,entry1,entry2):
        # Récupérer les valeurs des champs d'entrée
        valeur_entree1 = entry1.get()
        valeur_entree2 = entry2.get()
   
        # Afficher les valeurs récupérées
        print("Valeur 1:", valeur_entree1, ", type : ", type(valeur_entree1))
        print("Valeur 2:", valeur_entree2)

        #On nettoie 
        self.result_etudiants.set("")
        self.result_ecoles.set("")

        # On vérifie que la génération de Voeux est bien été lancée 
        if( valeur_entree1 == None or valeur_entree1 == "" ): 
            self.var_entry.select_clear()
            self.label1.config(fg='red')
        else : 
            self.var_entry.select_clear()
            self.label1.config(fg='black')

            self.controller.etudiants_choix = valeur_entree1
            self.controller.ecoles_choix = valeur_entree2
            self.controller.frames[ResultPage].correct_label()
            self.controller.show_frame(ResultPage)
  
class ResultPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller 
        load = Image.open("TEST.png")
        photo = ImageTk.PhotoImage(load,master=self)
       
       
       
        # Afficher l'image dans un label
        label_image = tk.Label(self, image=photo)
        label_image.image = photo
        label_image.place(x=0, y=0, relwidth=1, relheight=1)
        
        color2 = '#FFA6A6'
        color = 'WHITE'
        
        label1 = tk.Label(self,text="LES", 
                          font=("Aria Bold",20),
                          bg = color2
                          )
        #label.place(relx=0.5, rely=0.1, anchor='n')
        label1.pack(side = 'top')

        label = tk.Label(self,
                         text="RESULTAT", 
                         font=("Aria Bold",60),
                         bg = color2)
        #label.place(relx=0.5, rely=0.1, anchor='n')
        label.pack(side = 'top')
        
        label2 = tk.Label(self,
                          text="D'ADMISSION !", 
                          font=("Aria Bold",40),
                          bg = color2)
        #label.place(relx=0.5, rely=0.1, anchor='n')
        label2.pack(side = 'top')
        # Champs d'entrée
         
        label_choix_etudiants = tk.Label(self, 
                                         text="Choix des étudiants : ",
                                         font=("Arial", 20),
                                         bg = color)
        label_choix_etudiants.place(relx=0.3, rely=0.3, anchor='center')

        self.choix_etudiants = tk.Label(self, 
                                        text=" choix ",
                                        font=("Arial", 20),
                                        bg = color)
        self.choix_etudiants.place(relx=0.6, rely=0.3, anchor='center')     

        label_choix_ecoles = tk.Label(self, 
                                      text="Choix des écoles : ",
                                      font=("Arial", 20),
                                      bg = color)
        label_choix_ecoles.place(relx=0.3, rely=0.35, anchor='center')

        self.choix_ecoles = tk.Label(self, 
                                     text=" choix ",
                                     font=("Arial", 20),
                                     bg = color)
        self.choix_ecoles.place(relx=0.6, rely=0.35, anchor='center')    

        self.result_affectation = tk.Label(self, 
                                           text=" résultats ",
                                           font=("Arial", 20),
                                           bg = color)
        self.result_affectation.place(relx=0.3, rely=0.5, anchor='center')  

        Button = tk.Button(self, 
                           text="Retour à la page principale", 
                           font=("Arial", 15),
                           command=lambda: controller.show_frame(FirstPage),
                           background= color)
        Button.place(relx=0.15, rely=0.85, anchor='s')

    def correct_label(self):
        etudiants_choix_string = self.controller.etudiants_choix
        ecoles_choix_string = self.controller.ecoles_choix

        #on les affiche 
        self.choix_etudiants.config(text=etudiants_choix_string)  
        self.choix_ecoles.config(text=ecoles_choix_string)  

        #on transforme les chaînes de caractères en liste de listes d'entiers 
        etudiants_choix = self.stringIntoList(etudiants_choix_string)
        ecoles_choix = self.stringIntoList(ecoles_choix_string)
        self.nb_choix = len(ecoles_choix)
        final_affectation = mariageStable(etudiants_choix, ecoles_choix)
        string_affectation = printAffectation(final_affectation, self.nb_choix)
        self.result_affectation.config(text=string_affectation) 

        #satisfaction et ses tableaux 
        satisfaction_etudiant, satisfaction_ecole = satisfaction_perso(final_affectation, etudiants_choix, ecoles_choix, 1)
        self.plotSatisfaction(satisfaction_etudiant, satisfaction_ecole)


    def stringIntoList(self, str_ecole):

        #on enleve la premiere et derniere parenthese 
        str_ecole = str_ecole[1:len(str_ecole)-1]
        liste_choix_tt = []
        list_choix = []

        for carac in str_ecole:
            if (carac == ")") : 
                liste_choix_tt.append(list_choix)
                list_choix = []
            elif (carac.isnumeric()) :
                list_choix.append(int(carac))

        return liste_choix_tt
    
    
    def plotSatisfaction(self, satisfaction_etu, satisfaction_eco):

        fig = plt.figure(figsize=(4, 4))
        nb = len(satisfaction_eco)
        ax = fig.add_subplot(111)
        ax.set_xlabel('Participants')
        ax.set_ylabel('Satisfaction')
        ax.plot(list(range(1,nb+1)), satisfaction_etu, 'bo', label='étudiants')
        ax.plot(list(range(nb+1,nb*2+1)), satisfaction_eco, 'ro', label='écoles')
        ax.set_ylim([0,110])
        ax.legend()
        fig.subplots_adjust(bottom=0.3 , left=0.3)
        
        canvas = FigureCanvasTkAgg(fig, self)
        canvas._tkcanvas.place(relx=0.5, rely=0.4)
        
        
class Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
 
        # creating a window
        window = tk.Frame(self)
        window.pack()
        window.grid_rowconfigure(0, minsize=window.winfo_screenheight())
        window.grid_columnconfigure(0, minsize=window.winfo_screenwidth())
 
        self.frames = {}
        for F in (FirstPage, SecondPage,ThirdPage,ResultPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
 
        self.show_frame(FirstPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("ParcourpSoup")

   
 
app = Application()
app.maxsize(1700, 900)
app.mainloop()