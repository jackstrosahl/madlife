from commands.command import Attack
from evennia import CmdSet


class CharacterCmdSet(CmdSet):
    def at_cmdset_creation(self):
        self.add(Attack)
        pass
    pass
