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
        Prisoners dilemma: Normal Form Game with the following utilities: {(0, 1): [0, 3], (1, 0): [3, 0], (0, 0): [2, 2], (1, 1): [1, 1]}
        sage: g.obtain_nash()
        [[(0, 1), (0, 1)]]
    """
    A = matrix([[2, 0], [3, 1]])
    g = NormalFormGame([A, A.transpose()])
    g.rename('PrisonersDilemma: ' + repr(g))
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
    g.rename('Battle of the sexes: ' + repr(g))
    return g

def HawkDove():
    """
    Return a Hawk Dove game

        sage: g = game_theory.HawkDove()
        sage: g
        Hawk-Dove: Normal Form Game with the following utilities: {(0, 1): [2, 3], (1, 0): [6, -1], (0, 0): [4, 2], (1, 1): [0, 0]}
        sage: g.obtain_nash()
        [[(1, 0), (0, 1)]]
    """
    A = matrix([[4, 2], [6, 0]])
    B = matrix([[2, 3], [-1, 0]])
    g = NormalFormGame([A, B])
    g.rename('Hawk-Dove: ' + repr(g))
    return g
