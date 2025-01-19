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
        Retou

    

