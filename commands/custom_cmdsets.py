from commands.command import Attack
from commands.command import DrinkBeer
from evennia import CmdSet


class CharacterCmdSet(CmdSet):
    def at_cmdset_creation(self):
        self.add(Attack())
        self.add(DrinkBeer())
        pass
    pass
