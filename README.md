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

L'application calcule l'entropie du mot de passe afin d'estimer son niveau de sécurité.

La formule utilisée est :

```
Entropie = Longueur × log2(nombre de caractères possibles)
```

- **Longueur** : nombre de caractères du mot de passe.
- **Nombre de caractères possibles** : taille de l'ensemble de caractères utilisé (minuscules, majuscules, chiffres et/ou symboles).

Exemple :

- Mot de passe de 12 caractères utilisant uniquement les lettres minuscules :

```
Entropie = 12 × log2(26) ≈ 56,4 bits
```

- Mot de passe de 12 caractères utilisant minuscules, majuscules, chiffres et symboles (82 caractères possibles) :

```
Entropie = 12 × log2(82) ≈ 76,3 bits
```

### Important

L'entropie est **une estimation théorique** de la résistance d'un mot de passe face à une attaque par force brute. Elle ne garantit pas à elle seule qu'un mot de passe est réellement sécurisé.

En pratique, la sécurité dépend également de plusieurs facteurs :

- la qualité de l'algorithme de génération ;
- l'absence de mots du dictionnaire ou de motifs prévisibles ;
- le stockage sécurisé du mot de passe (hachage, salage, etc.) ;
- les techniques d'attaque utilisées par un attaquant.

L'entropie constitue donc un **indicateur de robustesse**, mais elle ne représente pas à elle seule le niveau réel de sécurité d'un mot de passe.

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
