from commands.command import Attack
from evennia import CmdSet

class Combat(CmdSet):

    key = "Combat"

    def at_cmdset_creation(self):
        self.add(Attack())
        pass
    pass
