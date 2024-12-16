# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions

class Game:
    # Directions possibles 
    VALID_DIRECTIONS ={"N": "Nord", "S": "Sud", "E": "Est", "O": "Ouest", "U": "Haut","D":"Bas",}


    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None   
    
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = ""
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", Actions.go, 1)
        self.commands["go"] = go
        
        # Setup create 
        Forteresse = Room("Forteresse ", " Une forteresse ancienne perchée au sommet d'une montagne volcanique.")
        self.rooms.append( Forteresse )
        Forêt = Room("Forêt", " Une forêt dense regorgeant de ressources naturelles (bois, plantes médicinales)")        
        self.rooms.append(Forêt)
        Désert = Room("Désert ", "Une vaste étendue désertique où les ressources sont rares mais stratégiquement importante pour contrôler les routes commerciales.")
        self.rooms.append(Désert )
        Ruines= Room("Ruines", " Un lieu ancien avec des structures abandonnées, regorgeant de trésors et de connaissances oubliées.")
        self.rooms.append(Ruines)
        Port = Room("Port ", " Un port maritime crucial pour le commerce et le transport.")
        self.rooms.append(Port )
        Plaine = Room("Plaine", " Un territoire ouvert idéal pour les grandes batailles d'armées.")
        self.rooms.append(Plaine)
        Gorge  = Room("Gorge", " Un canyon étroit avec des chemins dangereux mais stratégiquement avantageux pour tendre des embuscades ou bloquer l'avancée des ennemis .")
        self.rooms.append(Gorge )
        Citadelle = Room("Citadelle", " Une région enneigée avec des mines de cristaux rares .")
        self.rooms.append(Citadelle )
        Tour= Room("Tour", " Une structure imposante située au sommet de la forteresse.")
        self.rooms.append(Tour )
        Cryptes= Room("Cryptes", " Un réseau souterrain mystérieux et sombre sous les ruines.")
        self.rooms.append(Cryptes )




        # Create exits for rooms

        Forteresse.exits = {"N" : Forêt , "E" : None, "S" : Ruines , "O" : None,"U" :Tour }
        Forêt.exits = {"N" :Plaine , "E" : Port  , "S" : None , "O" : None}
        Désert .exits = {"N" : None, "E" :Ruines , "S" :Forteresse , "O" : None}
        Ruines.exits = {"N" : None, "E" : None, "S" : Citadelle, "O" :Gorge ,"D" :Cryptes}
        Port.exits = {"N" : Plaine, "E" : None, "S" : None, "O" : Désert}    
        Plaine.exits = {"N" : Désert, "E" :Forêt , "S" : None, "O" : None}
        Gorge.exits = {"N" : None, "E" : None , "S" :Port, "O" :Forêt,"U" : Citadelle }
        Citadelle.exits = {"N" :Gorge, "E" : None, "S" : None, "O" :Forêt }    
        Tour.exits = {"D" :Forteresse }
        Cryptes.exits = {"U" :Ruines }     




        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = Forteresse 

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:
     

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print("")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
