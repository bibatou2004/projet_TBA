# Define the Room class.

class Room:

    # Define the constructor. 
    def __init__(self, name, description,enemy_army):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = {}
        self.valid_directions={"N","E","S","O","NORD","EST","SUD","OUEST"}#set of direction
        self.character = {}
        self.enemy_army = enemy_army  # Nombre d'unités ennemies
    
    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\nVous êtes dans {self.description}\n\n{self.get_exit_string()}\n"
    
    # def get_inventory(self):
        """Retourne une chaîne représentant l'inventaire du joueur."""
        if not self.inventory and self.character :
            return "La piece est vide."

        print ("\nLa piece dispose des items suivants :")
        
        items = [str(item) for item in self.inventory if item is not None]
        characters= {characterx.name : characterx.description for characterx in self.character.values()}

        return "\n".join(items+characters)

    
    def get_inventory(self):
        """Retourne une chaîne représentant l'inventaire de la pièce."""
        if not self.inventory and not self.character:
            return "La pièce est vide."

        result = []

        # Ajouter les items
        if self.inventory:
            items = [str(item) for item in self.inventory if item is not None]
            result.append("La pièce dispose des items suivants :")
            result.extend(items)

        # Ajouter les personnages
        if self.character:
            characters = [f"{character.name} : {character.description}" for character in self.character.values()]
            result.append("\nLes personnages présents dans la pièce :")
            result.extend(characters)

        return "\n".join(result)


    
        
    
    

        
        #for name, item in self.inventory.items():
           # inventory_list += f"    - {name}: {item.description} ({item.weight} kg)\n"
        #return inventory_list
