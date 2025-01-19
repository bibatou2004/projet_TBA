# Define the Player class.
class Player():

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = []  # Initialize the history attribute as an empty list.
        self.inventory = {}
        self.army = 15
    # Define the move method.
    def move(self, direction):
    # Vérifier si la direction est valide dans la pièce actuelle
        if direction not in self.current_room.exits:
           print("\nIl n'y a pas de sortie dans cette direction !\n")
           return False

        # Obtenir la pièce suivante
        next_room = self.current_room.exits[direction]

        # Ajouter la pièce actuelle à l'historique avant de changer de pièce
        self.history.append(self.current_room)

        # Mettre à jour la pièce actuelle
        self.current_room = next_room

        # Afficher le nom et la description de la nouvelle pièce
        print(f"Vous êtes maintenant dans : {next_room.name}")
        print(next_room.description)

        # Afficher les sorties uniquement si la pièce n'est pas le château
        if next_room.name.lower() != "chateau":
            print(f"Sorties: {', '.join(next_room.exits.keys())}\n")

        return True

    # Define the get_history method.
    def get_history(self):
        if not self.history:
            return "\nVous n'avez pas encore visité de pièces."

        # Create a list of room descriptions from the history.
        visited_rooms = [room.get_long_description() for room in self.history]
        history_str = "\nVous avez déjà visité les pièces suivantes:\n    - " + "\n    - ".join(visited_rooms)
        return history_str
    
    def get_inventory(self):
        """Retourne une chaîne représentant l'inventaire du joueur."""
        if not self.inventory:
            return "Votre inventaire est vide."

        inventory_list = "\nVous disposez des items suivants :\n"
        for name, item in self.inventory.items():
            inventory_list += f"    - {name}: {item.description} ({item.weight} kg)\n"
        return inventory_list
    
    def get_army(self):

        army_list = f"\nVotre armée possède {self.army} :\n"
        return army_list



    