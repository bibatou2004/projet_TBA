# Description: Jeu d'aventure textuel

# Import des modules
from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from character import Character

#DEBUG = True


class Game:
    # Directions possibles
    VALID_DIRECTIONS = {"N": "Nord", "S": "Sud", "E": "Est", "O": "Ouest", "U": "Haut", "D": "Bas"}

    def __init__(self):
        """Initialise le jeu."""
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.character = {}

    def setup(self):
        """Configure les commandes, les salles, les items et le joueur."""

        # Ajouter les commandes
       

        help = Command("help", " : Afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : Quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", Actions.go, 1)
        self.commands["go"] = go
        back = Command("back", " : Revenir en arrière", Actions.back, 0)
        self.commands["back"] = back
        check = Command("check", " : vérifier les items dans votre inventaire", Actions.check, 0)
        self.commands["check"] = check
        look = Command("look" , " :  observer la pièce actuelle", Actions.look, 0)
        self.commands["look"] = look
        take = Command("take", " : prendre un item dans la pièce", Actions.take, 1)
        self.commands["take"] = take
        drop = Command("drop", " : déposer un item dans la pièce", Actions.drop, 1)
        self.commands["drop"] = drop
        talk = Command("talk", " : Parler à un PNJ", Actions.talk, 1)
        self.commands["talk"] = talk
        attack = Command("attack", " : attaque les forces ennemies dans la pièce actuelle", Actions.attack_enemy, 0)
        self.commands["attack"] = attack
        armi = Command("Voir", " : voir l'effectif", Actions.armies, 0)
        self.commands["Voir"] = armi

        




        forteresse = Room("Forteresse", "Une forteresse ancienne perchée au sommet d'une montagne volcanique.", enemy_army=10)
        foret = Room("Forêt", "Une forêt dense regorgeant de ressources naturelles.", enemy_army=5)
        desert = Room("Désert", "Une vaste étendue désertique avec peu de ressources.", enemy_army=8)
        ruines = Room("Ruines", "Un lieu ancien avec des structures abandonnées.", enemy_army=6)
        port = Room("Port", "Un port maritime crucial pour le commerce.", enemy_army=12)
        plaine = Room("Plaine", "Un territoire ouvert idéal pour des batailles.", enemy_army=5)
        gorge = Room("Gorge", "Un canyon étroit avec des chemins dangereux.", enemy_army=10)
        citadelle = Room("Citadelle", "Une région enneigée avec des mines rares.", enemy_army=20)
        tour = Room("Tour", "Une structure imposante située au sommet de la forteresse.", enemy_army=8)
        cryptes = Room("Cryptes", "Un réseau souterrain mystérieux sous les ruines.", enemy_army=5)
        chateau = Room("chateau", "Le grand chateau inaccessible", enemy_army=5)
     



        # Ajouter les salles à la liste
        self.rooms.extend([forteresse, foret, desert, ruines, port, plaine, gorge, citadelle, tour, cryptes,chateau])

        # Créer des items
        sword = Item("sword", "une épée au fil tranchant", 2)
        shield = Item("shield", "un bouclier robuste", 5)
        bow = Item("Arc Long", "Un arc qui permet de tirer sur des ennemis à distance.", 7)
        axe = Item("Hache de Guerre", "Une arme destructrice contre les boucliers ennemis.", 8)

        # Ajouter les items à l'inventaire des salles
        forteresse.inventory["sword"] = sword
        foret.inventory["shield"] = shield
        foret.inventory = {"bow": bow}
        plaine.inventory = {"axe": axe}

        # Définir les sorties des salles
        """forteresse.exits = {"N": foret, "E": None, "S": ruines, "O": None, "U": tour}
        foret.exits = {"N": plaine, "E": port, "S": None, "O": None}
        desert.exits = {"N": chateau, "E": ruines, "S": forteresse, "O": None}
        ruines.exits = {"N": None, "E": None, "S": citadelle, "O": gorge, "D": cryptes}
        port.exits = {"N": plaine, "E": None, "S": None, "O": desert}
        plaine.exits = {"N": desert, "E": foret, "S": None, "O": None}
        gorge.exits = {"N": None, "E": None, "S": port, "O": foret, "U": citadelle}
        citadelle.exits = {"N": gorge, "E": None, "S": None, "O": foret}
        tour.exits = {"D": forteresse}
        cryptes.exits = {"U": ruines}"""


        forteresse.exits = {"N": foret, "E": plaine, "S": ruines}
        foret.exits = {"N": gorge, "S": forteresse, "E": port}
        plaine.exits = {"E": desert, "W": forteresse}
        desert.exits = {"N": chateau, "W": plaine}
        ruines.exits = {"N": forteresse, "E": cryptes}
        port.exits = {"W": plaine}  # Correction ici : port doit mener à plaine, pas forêt
        gorge.exits = {"S": foret, "N": citadelle}
        citadelle.exits = {"S": gorge}
        cryptes.exits = {"W": ruines}
        tour.exits = {"D": forteresse}
        chateau.exits = {}  # Pas de sorties supplémentaires depuis le château

    


        

        # Configurer le joueur
        self.player = Player(input("\nEntrez votre nom : "))
        self.player.current_room = forteresse

        # Les PNJ 
        capitaine = Character("Capitaine des gardes","Un soldat imposant qui veille à la sécurité de la forteresse.",forteresse,["Restez sur vos gardes, des ennemis pourraient attaquer !", 
        "La forteresse est imprenable, grâce à notre vigilance."])

        forgeron = Character("Grimgor", "Un forgeron robuste et expérimenté.", forteresse, ["C'est en forgeant qu'on devient forgeron."])
        eclaireur = Character("Lyria", "Une éclaireuse agile prête à partager ses connaissances.", foret, ["Les ennemis de la plaine ont une faiblesse dans leur formation."])
        
        forteresse.character["Grimgor"] = forgeron
        foret.character["Lyria"] = eclaireur

        self.victory_room=chateau





    def play(self):
        """Démarre le jeu."""
        self.setup()
        self.print_welcome()
        while not self.finished:
            self.process_command(input("> "))

    def process_command(self, command_string):
        """Traite les commandes entrées par le joueur."""
        list_of_words = command_string.split()
        command_word = list_of_words[0]

        if command_word not in self.commands.keys():
            print("\nCommande inconnue. Tapez 'help' pour voir les commandes disponibles.\n")
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    def print_welcome(self):
        """Affiche un message de bienvenue."""
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        print(self.player.current_room.get_long_description())

# Point d'entrée du programme
def main():
    Game().play()

if __name__ == "__main__":
    main()
