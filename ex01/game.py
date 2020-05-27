
class GotCharacter:

    def __init__(self, name, alive=True):
        self.first_name = name
        self.is_alive = alive


class Stark(GotCharacter):

    """A class representing the Stark family.\
       Or when bad things happen to good people."""

    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words():
        print(self.house_words)

    def die():
        self.is_alive = False
