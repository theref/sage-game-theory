"""
Documentation for the game theory catalog
"""
from sage.game_theory.normal_form_game import NormalFormGame
from sage import matrix

def PrisonersDilemma():
    """
    Return a Prisoners Dilemma game

        sage: g = PrisonersDilemma()
        sage: g
    """
    A = matrix([[2,5],[0,4]])
    g = NormalFormGame([A, A.transpose()])
    return g
