# 🔐 Générateur de mot de passe avec calcul d'entropie

## Description

Ce projet est une application réalisée en **Python** avec la bibliothèque **Tkinter**. Elle permet de générer un mot de passe aléatoire sécurisé selon plusieurs critères définis par l'utilisateur.

L'application offre également un calcul de l'**entropie** du mot de passe afin d'estimer son niveau de sécurité.

## Fonctionnalités

- Choix de la longueur du mot de passe.
- Ajout facultatif de :
  - lettres majuscules ;
  - chiffres ;
  - symboles.
- Génération d'un mot de passe aléatoire grâce au module `secrets`.
- Calcul automatique de l'entropie.
- Affichage d'un indicateur de sécurité :
  - 🔴 Rouge : faible
  - 🟠 Orange : moyen
  - 🟢 Vert : élevé
- Copie du mot de passe dans le presse-papiers en un clic.

## Bibliothèques utilisées

- `tkinter` : interface graphique.
- `secrets` : génération sécurisée de nombres aléatoires.
- `math` : calcul de l'entropie.
- `pyperclip` : copie dans le presse-papiers.

## Calcul de l'entropie

L'entropie mesure la difficulté à deviner un mot de passe.

La formule utilisée est :

\[
\text{Entropie} = L \times \log_2(N)
\]

où :

- **L** = longueur du mot de passe ;
- **N** = nombre de caractères possibles.

Par exemple :

- 12 caractères parmi 26 lettres minuscules :

\[
12 \times \log_2(26) \approx 56,4\ \text{bits}
\]

- 12 caractères parmi 26 minuscules + 26 majuscules + 10 chiffres + 20 symboles (82 caractères) :

\[
12 \times \log_2(82) \approx 76,3\ \text{bits}
\]

## Interprétation

| Entropie | Niveau |
|----------:|:-------|
| < 40 bits | Faible |
| 40 à 70 bits | Moyen |
| > 70 bits | Élevé |

Plus l'entropie est élevée, plus le mot de passe est difficile à casser par une attaque de force brute.

## Lancement

Installer la dépendance :

```bash
pip install pyperclip
```

Puis exécuter :

```bash
python main.py
```

## Auteur

Projet réalisé en Python dans le cadre d'un exercice sur la sécurité informatique et la génération de mots de passe.
