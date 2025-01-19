class Item:
    """
    Représente un objet manipulé par le joueur.

   
    """

    def __init__(self, name, description, weight):
        """
        Initialise un nouvel objet.

        """
        self.name = name
        self.description = description
        self.weight = weight

    def __str__(self):
        """
        Retourne une représentation textuelle de l'objet.

        Returns:
            str: Une chaîne formatée représentant l'objet.
        """
        return f"{self.name} : {self.description} ({self.weight} kg)"

    def to_dict(self) :
        return {self.name : [self.description,self.weight] }



