"""
Documentation for the game theory catalog
"""
from sage.game_theory.normal_form_game import NormalFormGame
from sage.matrix.constructor import matrix

def PrisonersDilemma():
    """
    Return a Prisoners Dilemma game

        sage: g = game_theory.PrisonersDilemma()
        sage: g
        Prisoners dilemma: Normal Form Game with the following utilities: {(0, 1): [5, 0], (1, 0): [0, 5], (0, 0): [2, 2], (1, 1): [4, 4]}
        sage: g.obtain_nash()
        [[(0, 1), (0, 1)]]
    """
    A = matrix([[2, 5], [0, 4]])
    g = NormalFormGame([A, A.transpose()])
    return g

def BattleOfTheSexes():
    """
    Return a Battle of the Sexes game

        sage: g = game_theory.BattleOfTheSexes()
        sage: g
        Battle of the sexes: Normal Form Game with the following utilities: {(0, 1): [0, 1], (1, 0): [1, 0], (0, 0): [3, 2], (1, 1): [2, 3]}
        sage: g.obtain_nash()
        [[(0, 1), (0, 1)], [(3/4, 1/4), (1/2, 1/2)], [(1, 0), (1, 0)]]
    """
    A = matrix([[3, 0], [1, 2]])
    B = matrix([[2, 1], [0, 3]])
    g = NormalFormGame([A, B])
    return g
