from tkinter import *
from tkinter.messagebox import showinfo
import webbrowser

compteur = 0
jeu_en_cours = False
duree_jeu = 5  


def clique(): 
    """
    Cette fonction est la structure même du programme, elle permet de compter le nombre de clics
    """
    global compteur, jeu_en_cours
    if jeu_en_cours:
        compteur += 1
        compteur_label.config(text=f"Clics : {compteur}")


def countdown(valeur):
    """
    Cette fonction sert de compteur, en effet, tant que la valeur du compteur est supérieur à 0
    le compteur continue de décroitre et quand il arrive à 0, cela nous affiche le résultat du test
    """
    global jeu_en_cours
    if valeur > 0:
        timer_label.config(text=f"Temps restant : {valeur}s")
        fenetre.after(1000, countdown, valeur - 1) # Programme l'exécution d'une fct après x temps
    else:                                          # after(délai,fonction,arguments)
        jeu_en_cours = False
        timer_label.config(text="Temps écoulé !")
        cps = compteur / duree_jeu  
        showinfo("Résultat", f"Votre score : {compteur} clics\nCPS : {cps:.2f}") # Retourne notre score
        start_button.config(state=NORMAL) # Re-autorise l'utilisateur à appuyer sur le bouton "commencer"


def start_game():
    """
    Fonction motrice du programme, là où tout est rassemblé, s'execute lorsque le bouton 
    "commencer le test" est appuyé.
    """
    global compteur, jeu_en_cours, duree_jeu
    try:
        duree_jeu = int(entree.get())
        if duree_jeu <= 0:
            raise ValueError
    except ValueError:
        showinfo("Erreur", "Veuillez entrer un nombre entier positif pour la durée.")
        return

    compteur = 0
    compteur_label.config(text=f"Clics : {compteur}") # Met à jour en temps réel le nombre de clics
    jeu_en_cours = True
    start_button.config(state=DISABLED) # Empêche l'utilisateur de commencer plusieurs fois le jeu 
    countdown(duree_jeu)


fenetre = Tk()
fenetre.title("Compteur de CPS")
fenetre.state('zoomed') # Force la fenetre à se mettre en plein écran ( avec bordures )


value = StringVar() 
value.set("5")  # Ces 2 premières lignes permettent de définir la valeur par défaut 
entree = Entry(fenetre, textvariable=value, width=10)
entree.pack()
bouton_valider = Button(fenetre, text="Valider la durée", command=lambda: showinfo("Durée", f"Durée définie : {entree.get()}s"))
bouton_valider.pack(pady=5)

label = Label(fenetre, text="Bienvenue sur le compteur de clics par seconde ! (CPS)")
label.pack(pady=10)

bouton_sortie = Button(fenetre, text="Fermer le programme", command=fenetre.quit)
bouton_sortie.pack(pady=5)


tst = LabelFrame(fenetre, text='Compteur', padx=30, pady=30)
tst.pack(pady=10)

aff = Button(tst, text="Cliquez !", width=20, height=5, command=clique)
aff.pack()

compteur_label = Label(tst, text="Clics : 0", font=("Arial", 14))
compteur_label.pack(pady=5)

timer_label = Label(fenetre, text=f"Temps restant : {duree_jeu}s", font=("Arial", 12))
timer_label.pack(pady=5)

start_button = Button(fenetre, text="Commencer le test", command=start_game)
start_button.pack(pady=10)


def alert():
    """
    Cette fonction permet de renvoyer vers un lien github lorsque l'utilisateur ouvre le menu Aide 
    et sélectionne "Explications du programme".
    """
    showinfo("Info", "Vous allez être redirigé vers le readme associé à ce projet")
    webbrowser.open("https://github.com/het637/Click-Test/blob/main/README.md")



menubar = Menu(fenetre)
menu_aide = Menu(menubar, tearoff=0) # tearoff=0 force le menu a rester dans la même fenêtre
menubar.add_cascade(label="Aide", menu=menu_aide) # Menu 
menu_aide.add_command(label="Explications du programme", command=alert) # Option du menu
fenetre.config(menu=menubar)

fenetre.mainloop()
