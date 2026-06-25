# ------------- imports -------------
import tkinter
import secrets
import math
import pyperclip

# ------------- les fonctions -------------
    # fonction generer ( qui sert à générer le mot de passe )
def generer():
    caracteres = "abcdefghijklmnopqrstuvwxyz"

    if var_maj.get() == 1:
        caracteres += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if var_chiffre.get() == 1:
        caracteres += "0123456789"

    if var_signes.get() == 1:
        caracteres += "!@#$%^&*µ=(){<>+§/~"

    longueur = int(champ_longueur.get())
    global mot_de_passe
    mot_de_passe = "".join(secrets.choice(caracteres) for _ in range(longueur))

    entropie = round(longueur * math.log2(len(caracteres)), 2)
    affiche_entropie.config(text=entropie)

    if entropie < 40:
        affiche_entropie.config(fg="red")
    elif entropie < 70:
        affiche_entropie.config(fg="orange")
    else:
        affiche_entropie.config(fg="green")
    affiche.config(text=mot_de_passe)

    # fonction copier ( qui sert à copier le mot de passe en 1 clic )
def copier():
    pyperclip.copy(mot_de_passe)

# ------------- fenêtre principale -------------

    # ___ base de la page ___
page = tkinter.Tk()
page.title("Créer son mot de passe + calcul d'entropie")
page.geometry("500x300")
page.configure(bg="#5C5C5C")
    # configuration
page.columnconfigure(0, weight=1)
page.columnconfigure(1, weight=1)
page.columnconfigure(2, weight=1)
page.rowconfigure(10, weight=1)

# ------------- widgets -------------
    # ___ longueur + saisie ___
mon_label = tkinter.Label(page, text="Longueur :")
mon_label.grid(row=0, column=0, columnspan=3)

champ_longueur = tkinter.Entry(page)
champ_longueur.grid(row=1, column=0, columnspan=3, padx=5, pady=0)


    # ___ les 3 options ___
var_maj = tkinter.IntVar()
maj = tkinter.Checkbutton(page, text="Majuscule :", variable=var_maj)
maj.grid(row=2, column=0, pady=(20,0))

var_chiffre = tkinter.IntVar()
chiffre = tkinter.Checkbutton(page, text="Chiffres", variable=var_chiffre)
chiffre.grid(row=2, column=1, pady=(20,0))

var_signes = tkinter.IntVar()
signes = tkinter.Checkbutton(page, text="Symboles", variable=var_signes)
signes.grid(row=2, column=2, pady=(20,0))

 # ___ generer ___
btn_generer = tkinter.Button(page, text="Générer", bg="#1a73e8", fg="white", padx=20, pady=8, command=generer)
btn_generer.grid(row=6, column=0, columnspan=3, pady=15)

    # ___ mot de passe ___
label_mdp = tkinter.Label(page, text="MDP :")
label_mdp.grid(row=4, column=0, columnspan=4, pady=(15,0))

affiche = tkinter.Label(page, text="")
affiche.grid(row=4, column=1, columnspan=3, pady=(15,0))

    # ___ entropie ___
label_entropie = tkinter.Label(page, text="Entropie :")
label_entropie.grid(row=5, column=0, columnspan=3, pady=(10,0))

affiche_entropie = tkinter.Label(page, text="")
affiche_entropie.grid(row=5, column=1, columnspan=4, pady=(10,0))

    # ___ copie ___
btn_copier = tkinter.Button(page, text="Copier", command=copier)
btn_copier.grid(row=10, column=2, sticky="se", padx=10, pady=10)









# ------------- boucle principale -------------
page.mainloop()

