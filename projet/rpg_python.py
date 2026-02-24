import random
import time


class Personnage:
    def __init__(self, nom, pv, attaque):
        self.nom = nom
        self.pv = pv
        self.pv_max = pv
        self.attaque = attaque

    def est_vivant(self):
        return self.pv > 0

    def attaquer(self, adversaire):
        variabilite = random.randint(-3, 3)
        degats = max(0, self.attaque + variabilite)
        adversaire.pv -= degats
        print(f"{self.nom} attaque {adversaire.nom} et inflige {degats} degats.")


class Joueur(Personnage):
    def __init__(self, nom):
        super().__init__(nom, pv=100, attaque=18)
        self.potions = 3

    def se_soigner(self):
        if self.potions > 0:
            soin = 40
            self.pv = min(self.pv_max, self.pv + soin)
            self.potions -= 1
            print(f"{self.nom} utilise une potion. PV : {self.pv}/{self.pv_max}.")
        else:
            print("Action impossible : plus de potions.")


def lancer_simulation():
    print("--- PROTOCOLE DE COMBAT ALPHA ---")
    nom_entree = input("Nom de l'unite : ")
    if not nom_entree: nom_entree = "Admin"

    joueur = Joueur(nom_entree)
    ennemis = [
        Personnage("Drone de securite", 40, 10),
        Personnage("Gardien Reseau", 65, 15),
        Personnage("Noyau Central", 95, 22)
    ]

    for ennemi in ennemis:
        print(f"\nCible identifiee : {ennemi.nom}")

        while ennemi.est_vivant() and joueur.est_vivant():
            print(f"\n{joueur.nom} : {joueur.pv} PV | {ennemi.nom} : {ennemi.pv} PV")
            choix = input("1: Attaque | 2: Potion | Choix : ")

            if choix == "1":
                joueur.attaquer(ennemi)
            elif choix == "2":
                joueur.se_soigner()

            if ennemi.est_vivant():
                time.sleep(0.6)
                ennemi.attaquer(joueur)

        if not joueur.est_vivant():
            print(f"\nSimulation interrompue. {joueur.nom} est hors service.")
            return

        print(f"Cible neutralisee.")
        time.sleep(1)

    print(f"\nSimulation terminee. {joueur.nom} a securise la zone.")


if __name__ == "__main__":
    lancer_simulation()