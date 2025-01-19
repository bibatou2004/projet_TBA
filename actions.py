# Description: The actions module.

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.


# The error message is stored in the MSG0 and MSG1 variables and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

class Actions:

    @staticmethod
    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        
        """
        player = game.player
        if len(list_of_words) != number_of_parameters + 1:
            print(MSG1.format(command_word=list_of_words[0]))
            return False

        direction = list_of_words[1].strip().upper()
        current_room = game.player.current_room
        if direction not in player.current_room.exits:
            print(f"\nIl n'y a pas de sortie dans la direction '{direction}'.\n")
            return False
        next_room = current_room.exits[direction]
        player.move(direction)
        #print(f"Vous êtes maintenant dans : {next_room.name}")
        #print(f"Vous êtes dans {next_room.description}\n")
        #print(f"Sorties: {', '.join(next_room.exits.keys())}\n")
        if game.player.current_room == game.victory_room:
            print(f"\nFélicitations {player.name} ! Vous avez atteint le château et remporté la victoire !")
            game.finished = True
            
            return True

        
        return True

    @staticmethod
    def back(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de revenir dans la pièce précédente.
        """
        player = game.player
        if len(list_of_words) != number_of_parameters + 1:
            print("\nLa commande 'back' ne prend pas de paramètre.\n")
            return False

        if not player.history:
            print("\nImpossible de revenir en arrière, aucun historique disponible.\n")
            return False

        player.current_room = player.history.pop()
        print(player.current_room.get_long_description())
        return True

    @staticmethod
    def quit(game, list_of_words, number_of_parameters):
        """
        Quitter le jeu.
        """
        if len(list_of_words) != number_of_parameters + 1:
            print(MSG0.format(command_word=list_of_words[0]))
            return False

        print(f"\nMerci d'avoir joué. Au revoir.\n")
        game.finished = True
        return True

    @staticmethod
    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        """
        if len(list_of_words) != number_of_parameters + 1:
            print(MSG0.format(command_word=list_of_words[0]))
            return False

        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print(f"\t- {command}")
        print()
        return True
        
    
    @staticmethod
    def look(game, list_of_words, number_of_parameters):
        """
        Affiche la description de la pièce actuelle et la liste des items présents.

        
        """
       
        if len(list_of_words) != number_of_parameters + 1:
            print("\nLa commande 'look' ne prend pas de paramètre.\n")
            return False
        player = game.player
        

        # Afficher la description de la pièce actuelle
        

        # Afficher les items présents dans la pièce
        print(player.current_room.get_inventory())
        return True
    
    @staticmethod
    def take(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de prendre un item dans la pièce actuelle et de l'ajouter à son inventaire.

        """
        player = game.player
        if len(list_of_words) != number_of_parameters + 1:
            print("\nLa commande 'take' nécessite un paramètre: le nom de l'item.\n")
            return False

        item_name = list_of_words[1]
        current_room = player.current_room

        # Vérifier si l'item est présent dans la pièce
        if item_name not in current_room.inventory:
            print(f"\nL'item '{item_name}' n'est pas présent dans cette pièce.\n")
            return False

        # Ajouter l'item à l'inventaire du joueur
        item = current_room.inventory.pop(item_name)
        player.inventory[item_name] = item
        print(f"\nVous avez pris '{item_name}'.\n")
        return True
    
    @staticmethod
    def drop(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de déposer un item de son inventaire dans la pièce actuelle.

        """
        player = game.player
        if len(list_of_words) != number_of_parameters + 1:
            print("\nLa commande 'drop' nécessite un paramètre: le nom de l'item.\n")
            return False

        item_name = list_of_words[1]

        # Vérifier si l'item est dans l'inventaire du joueur
        if item_name not in player.inventory:
            print(f"\nL'item '{item_name}' n'est pas dans votre inventaire.\n")
            return False

        # Déposer l'item dans la pièce actuelle
        item = player.inventory.pop(item_name)
        player.current_room.inventory[item_name] = item
        print(f"\nVous avez déposé '{item_name}' dans la pièce.\n")
        return True
    
    @staticmethod
    def check(game, list_of_words, number_of_parameters):
        """
        Affiche la liste des items présents dans l'inventaire du joueur.

        """
         #player = game.
        if len(list_of_words) != number_of_parameters + 1:
            print("\nLa commande 'check' ne prend pas de paramètre.\n")
            return False

        # Afficher l'inventaire du joueur
        print(game.player.get_inventory())
        return True
    
    def attack_enemy(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de combattre l'armée ennemie dans la pièce actuelle.
        """
        current_room = game.player.current_room
        if current_room.enemy_army > 0:
            print(f"Vous attaquez l'armée ennemie dans {current_room.name} !")
        if game.player.army > current_room.enemy_army:
            print("Victoire ! Vous avez éliminé toutes les forces ennemies de cette pièce.")
            game.player.army -= current_room.enemy_army // 2  # Réduction de l'armée du joueur
            current_room.enemy_army = 0
        else:
            game.player.army -= current_room.enemy_army
            print("L'armée ennemie était trop forte. Vous avez subi de lourdes pertes.")

            if game.player.army <= 0:
                print("Votre armée a été complètement détruite !")
                print("Oups ! Vous avez perdu.")
                game.finished = True
            else:
                print("Il n'y a plus d'ennemis dans cette pièce.")


    def armies(game,list_of_words,number_of_parameters):
        if len(list_of_words) != number_of_parameters + 1:
            print("\nLa commande 'look' ne prend pas de paramètre.\n")
            return False
        player = game.player
        

        
        print(player.get_army())
        return True
    def talk(game,list_of_words,number_of_parameters) :
        player = game.player
        PNJ_name = list_of_words[1]
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            # Affiche un message d'erreur si le nombre d'arguments est incorrect
            print(MSG1.format(command_word=command_word))
            return False

        if PNJ_name in player.current_room.character:
            print(player.current_room.character[PNJ_name].get_msg())
            return True
        else:
            print(f"{PNJ_name} n’est pas ici.")
            return False


    
    



    
   

