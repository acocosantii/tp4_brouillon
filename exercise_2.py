import random


class NPC:
    """Classe de base pour tous les personnages non-joueurs"""

    def __init__(self, nom, race, espece, profession):
        # Génération des attributs avec 4d6 (garder les 3 meilleurs)
        self.force = self._rouler_attribut()
        self.agilite = self._rouler_attribut()
        self.constitution = self._rouler_attribut()
        self.intelligence = self._rouler_attribut()
        self.sagesse = self._rouler_attribut()
        self.charisme = self._rouler_attribut()

        # Autres attributs
        self.classe_armure = random.randint(1, 12)
        self.points_vie = random.randint(1, 20)

        self.nom = nom
        self.race = race
        self.espece = espece
        self.profession = profession

    def _rouler_attribut(self):
        """Roule 4d6 et garde les 3 meilleurs résultats"""
        des = [random.randint(1, 6) for _ in range(4)]
        des.sort(reverse=True)
        return sum(des[:3])

    def afficher_caracteristiques(self):
        """Affiche toutes les caractéristiques du personnage"""
        print(f"\n{'='*50}")
        print(f"nom: {self.nom}")
        print(f"race: {self.race}")
        print(f"espece: {self.espece}")
        print(f"profession: {self.profession}")
        print(f"{'='*50}")
        print(f"points de vie: {self.points_vie}")
        print(f"classe d'armure: {self.classe_armure}")
        print("\nattributs:")
        print(f"  force: {self.force}")
        print(f"  agilite: {self.agilite}")
        print(f"  constitution: {self.constitution}")
        print(f"  intelligence: {self.intelligence}")
        print(f"  sagesse: {self.sagesse}")
        print(f"  charisme: {self.charisme}")
        print(f"{'='*50}\n")


class Kobold(NPC):
    """Classe pour les monstres kobolds"""

    def __init__(self, nom):
        super().__init__(nom, "kobold", "creature", "monstre")

    def attaquer(self, cible):
        print(f"\n{self.nom} attaque {cible.nom}")

        jet_attaque = random.randint(1, 20)
        print(f"jet d'attaque: {jet_attaque}")

        if jet_attaque == 20:
            print("coup critique")
            dommage = random.randint(1, 8)
            cible.subir_dommage(dommage)
        elif jet_attaque == 1:
            print("attaque ratee")
        elif jet_attaque >= cible.classe_armure:
            print("l'attaque touche")
            dommage = random.randint(1, 6)
            cible.subir_dommage(dommage)
        else:
            print("l'attaque echoue")

    def subir_dommage(self, dommage):
        self.points_vie -= dommage
        print(f"{self.nom} subit {dommage} points de dommage")
        print(f"points de vie restants: {self.points_vie}")

        if self.points_vie <= 0:
            print(f"{self.nom} est vaincu")


class Heros(NPC):
    """Classe pour les héros joueurs"""

    def __init__(self, nom, race, profession):
        super().__init__(nom, race, "humanoide", profession)

    def attaquer(self, cible):
        print(f"\n{self.nom} attaque {cible.nom}")

        jet_attaque = random.randint(1, 20)
        print(f"jet d'attaque: {jet_attaque}")

        if jet_attaque == 20:
            print("coup critique")
            dommage = random.randint(1, 8)
            cible.subir_dommage(dommage)
        elif jet_attaque == 1:
            print("echec critique")
        elif jet_attaque >= cible.classe_armure:
            print("l'attaque touche")
            dommage = random.randint(1, 6)
            cible.subir_dommage(dommage)
        else:
            print("l'attaque echoue")

    def subir_dommage(self, dommage):
        self.points_vie -= dommage
        print(f"{self.nom} subit {dommage} points de dommage")
        print(f"points de vie restants: {self.points_vie}")

        if self.points_vie <= 0:
            print(f"{self.nom} est tombe au combat")


# =======================
# Exemple d'utilisation
# =======================

if __name__ == "__main__":
    heros = Heros("Aragorn", "humain", "guerrier")
    heros.afficher_caracteristiques()

    kobold = Kobold("Gribouille")
    kobold.afficher_caracteristiques()

    print("\n" + "="*50)
    print("debut du combat")
    print("="*50)

    round_num = 1
    while heros.points_vie > 0 and kobold.points_vie > 0:
        print(f"\n--- round {round_num} ---")

        heros.attaquer(kobold)

        if kobold.points_vie > 0:
            kobold.attaquer(heros)

        round_num += 1

        if round_num > 20:
            print("\nle combat s'eternise...")
            break

    print("\n" + "="*50)
    print("fin du combat")
    print("="*50)
