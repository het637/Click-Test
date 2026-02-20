# 🖱️ Compteur de Clics par Seconde (CPS) - Projet Tkinter Débutant

![Python](https://img.shields.io/badge/Python-3.13.7-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Terminé-success?style=for-the-badge)
![Library](https://img.shields.io/badge/Lib-Tkinter%20|%20webbrowser-orange?style=for-the-badge)

## 📋 Description du Projet

Ce projet est un **compteur de clics par seconde (CPS)** réalisé en Python avec **Tkinter**.  

L'objectif principal est **pédagogique** : apprendre les bases de Tkinter (widgets, boutons, labels, Entry, menus, timers) et la gestion des événements, **sans se concentrer sur le design ou l'interface graphique**.

Le programme permet à l'utilisateur de définir une durée de test, de cliquer autant de fois que possible sur un bouton, et affiche le score final ainsi que les CPS (clics par seconde).

---

## ✨ Fonctionnalités Principales

* **Durée configurable :** l'utilisateur peut définir la durée du test via un champ de saisie (`Entry`).  
* **Compteur dynamique :** le nombre de clics s'affiche en temps réel.  
* **Timer :** compte à rebours avec affichage du temps restant.  
* **Résultat final :** pop-up affichant le score et le CPS.  
* **Menu Aide :** ouvre un lien GitHub dans le navigateur via `webbrowser`.  
* **Fermeture facile :** bouton pour quitter le programme.  

---

## 🛠️ Installation et Lancement

### Prérequis

* **Python 3** (>= 3.6 recommandé)  
* Librairies utilisées :  
  * `tkinter` (inclus par défaut dans Python)  
  * `webbrowser` (module standard Python)

### Lancer le programme

1. Clonez le dépôt ou téléchargez le fichier `cps_tkinter.py`.  
2. Exécutez le programme avec :

```bash
python cps_tkinter.py
