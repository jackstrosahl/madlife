"""
Room

Rooms are simple containers that has no location of their own.

"""
import random
from evennia import DefaultRoom, TICKER_HANDLER



class Room(DefaultRoom):
    """
    Rooms are like any Object, except their location is None
    (which is default). They also use basetype_setup() to
    add locks so they cannot be puppeted or picked up.
    (to change that, use at_object_creation instead)

    See examples/object.py for a list of
    properties and methods available on all Objects.
    """

ECHOES = ["You make eye contact with a passerby. Awkward.",
          "The seat you sit on is warm. FeelsGoodMan",
          "The bus jiggles slightly as it drives.",
          "You lean into the various turns.",
          "Looking out the window, you're hypnotized by the moving scenery.",
          "The bus driver reminds everyone to go to the back of the bus if possible. Being an upstanding citizen, you already are.",
          "You make eye contact with a cutey at the other end of the bus"]

class Bus(DefaultRoom):
    "Room is ticked at regular intervals"
    def at_object_creation(self):
        TICKER_HANDLER.add(20, self.at_weather_update)

    def at_weather_update(self, *args, **kwargs):
        echo = random.choice(ECHOES)
        self.msg_contents(echo)
