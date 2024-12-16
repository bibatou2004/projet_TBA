# Define the Player class.
class Player():

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = []  # Initialize the history attribute as an empty list.
    
    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        # Add the current room to the history before moving.
        self.history.append(self.current_room)

        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())

        # Display the history after moving.
        print(self.get_history())
        return True
    # Define the get_history method.
    def get_history(self):
        if not self.history:
            return "\nVous n'avez pas encore visité de pièces."

        # Create a list of room descriptions from the history.
        visited_rooms = [room.get_short_description() for room in self.history]
        history_str = "\nVous avez déjà visité les pièces suivantes:\n    - " + "\n    - ".join(visited_rooms)
        return history_str

    # Define the back method to move the player back to the previous room.
    def back(self):
        if not self.history:
            print("\nImpossible de revenir en arrière, aucun historique disponible.\n")
            return False

        # Pop the last room from the history and set it as the current room.
        self.current_room = self.history.pop()
        print(self.current_room.get_long_description())
        return True

# Notes:
# - At the start of the game, the history should be empty because the player hasn't moved yet.
# - The history is updated only when the player moves to a new room.


    