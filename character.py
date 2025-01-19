from room import Room
import random
#from game import DEBUG
DEBUG = True
class Character:
    def __init__(self, name, description, current_room, msgs):
        """
        Initialise un personnage avec un nom, une description, un lieu actuel et des messages.

        :param name: str, le nom du personnage
        :param description: str, la description du personnage
        :param current_room: Room, le lieu actuel du personnage
        :param msgs: list of str, les messages du personnage
        """
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs

    def __str__(self):
        """
        Retourne une représentation textuelle du personnage.

        :return: str, une description textuelle du personnage
        """
        return f"{self.name} : {self.description}"
    
    def get_msg(self):
        if not self.msgs:
            raise ValueError("La liste des messages ne peut pas être vide.")
        # Récupérer et réinsérer le message en fin de liste
        message = self.msgs.pop(0)
        self.msgs.append(message)
        return message

    def move(self):
        """
        Déplace le personnage non joueur vers une pièce adjacente au hasard si possible.
        Returns:
        bool: True si le personnage s'est déplacé, False sinon.
        """
         # Vérifier les sorties possibles
        exits = list(self.current_room.exits.keys())
        # Une chance sur deux de se déplacer
        if random.choice([True, False]):
            # Choisir une direction au hasard
            new_direction = random.choice(exits)
            next_room = self.current_room.exits.get(new_direction)
            if next_room is None:
                if DEBUG:
                    print(f"DEBUG: {self.name} se trouve devant une porte fermée et reste dans {self.current_room.name}.")
                    return False
                
                # Retirer le personnage de la pièce actuelle
                if self.name in self.current_room.character:
                    del self.current_room.character[self.name]
                    # Déplacer le personnage
                    self.current_room = next_room
                    # Ajouter le personnage à la nouvelle pièce
                    if next_room.character is None:
                        next_room.character = {}
                        next_room.character[self.name] = self
                    if DEBUG:
                        print(f"DEBUG: {self.name} s'est déplacé vers {self.current_room.name}.")
                        return True
                    if DEBUG:
                        print(f"DEBUG: {self.name} a décidé de rester dans {self.current_room.name}.")
                        return False

    
