""""
A template definition of a player, serving as the contract between different implementations and the game object.
"""

import abc

class AbstractPlayer(metaclass=abc.ABCMeta):
    def __init__(self, playernr, gamestate):
        self._playernr = playernr
        self._gamestate = gamestate

    def placepoints(self):
        pass