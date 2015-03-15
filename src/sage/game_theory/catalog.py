r"""
Documentation for the game theory catalog

A catalog of named normal form games.
The docstrings give an interpretation of the situation they model.

AUTHOR:

- James Campbell and Vince Knight (06-2014)
"""
from sage.game_theory.normal_form_game import NormalFormGame
from sage.matrix.constructor import matrix


def PrisonersDilemma():
    r"""
    Return a Prisoners dilemma game.

    Assume two thieves have been caught by the police
    and separated for questioning.
    If both thieves cooperate and do not divulge any information they will
    each get a short sentence.
    If one defects he/she is offered a deal while the other thief will get a
    long sentence.
    If they both defect they both get a medium length sentence.

    This can be modeled as a normal form game using the following two matrices:

    .. math::

        A = \begin{pmatrix}
            3&1\\
            0&2\\
            \end{pmatrix}


        B = \begin{pmatrix}
            2&1\\
            0&3\\
            \end{pmatrix}


    There is a single Nash equilibria for this at which both thieves defect.
    This can be implemented in Sage using the following::

        sage: g = game_theory.PrisonersDilemma()
        sage: g
        Prisoners dilemma: Normal Form Game with the following utilities: {(0, 1): [0, 3], (1, 0): [3, 0], (0, 0): [2, 2], (1, 1): [1, 1]}
        sage: g.obtain_nash()
        [[(0, 1), (0, 1)]]
    """
    A = matrix([[2, 0], [3, 1]])
    g = NormalFormGame([A, A.transpose()])
    g.rename('Prisoners dilemma: ' + repr(g))
    return g


def BattleOfTheSexes():
    r"""
    Return a Battle of the Sexes game

    Consider two payers: Amy and Bob.
    Amy prefers to play video games and Bob prefers to
    watch a movie. They both however want to spend their evening
    together.
    This can be modeled as a normal form game using the following two matrices:

    .. math::

        A = \begin{pmatrix}
            3&1\\
            0&2\\
            \end{pmatrix}


        B = \begin{pmatrix}
            2&1\\
            0&3\\
            \end{pmatrix}

    There are three Nash equilibria:

    1. Amy and Bob both play video games;
    2. Amy and Bob both watch a movie;
    3. Amy plays video games 75% of the time and Bob watches a movie 75% of the time.

    This can be implemented in Sage using the following::

        sage: g = game_theory.BattleOfTheSexes()
        sage: g
        Battle of the sexes: Normal Form Game with the following utilities: {(0, 1): [1, 1], (1, 0): [0, 0], (0, 0): [3, 2], (1, 1): [2, 3]}
        sage: g.obtain_nash()
        [[(0, 1), (0, 1)], [(3/4, 1/4), (1/4, 3/4)], [(1, 0), (1, 0)]]
    """
    A = matrix([[3, 1], [0, 2]])
    B = matrix([[2, 1], [0, 3]])
    g = NormalFormGame([A, B])
    g.rename('Battle of the sexes: ' + repr(g))
    return g


def HawkDove():
    r"""
    Return a Hawk Dove game

    Suppose two birds of prey must share a limited resource.
    The birds can act like a hawk or a dove.
    Hawks always fight over the resource to the point of exterminating a
    fellow hawk and/or take a majority of the resource from a dove.
    Two doves can share the resource.
    This can be modeled as a normal form game using the following two matrices:

    .. math::

        A = \begin{pmatrix}
            0&3\\
            1&2\\
            \end{pmatrix}


        B = \begin{pmatrix}
            0&1\\
            3&2\\
            \end{pmatrix}

    There are three Nash equilibria:

        1. Both birds act like Hawks;
        2. Both birds act like Doves;
        3. Both birds are equally likely to act like a Hawk of a Dove.

    This can be implemented in Sage using the following::

        sage: g = game_theory.HawkDove()
        sage: g
        Hawk-Dove: Normal Form Game with the following utilities: {(0, 1): [3, 1], (1, 0): [1, 3], (0, 0): [0, 0], (1, 1): [2, 2]}
        sage: g.obtain_nash()
        [[(0, 1), (1, 0)], [(1/2, 1/2), (1/2, 1/2)], [(1, 0), (0, 1)]]
    """
    A = matrix([[0, 3], [1, 2]])
    g = NormalFormGame([A, A.transpose()])
    g.rename('Hawk-Dove: ' + repr(g))
    return g


def Pigs():
    r"""
    Return a Pigs game

    Consider two pigs.
    One dominant pig and one subservient pig.
    These pigs share a pen.
    There is a lever in the pen that delivers food but if either pig pushes
    the lever it will take them a little while to get to the food.
    If the dominant pig pushes the lever, the subservient pig has some time
    to eat most of the food before being pushed out of the way.
    If the subservient pig push the lever,
    the dominant pig will eat all the food.
    Finally if both pigs go to push the lever the subservient pig will be
    able to eat a third of the food.

    This can be modeled as a normal form game using the following two matrices:

    .. math::

        A = \begin{pmatrix}
            4&2\\
            6&0\\
            \end{pmatrix}


        B = \begin{pmatrix}
            2&3\\
            -1&0\\
            \end{pmatrix}

    There is a single Nash equilibrium at which the dominant pig pushes the
    lever and the subservient pig does not.

    This can be implemented in Sage using the following::

        sage: g = game_theory.Pigs()
        sage: g
        Pigs: Normal Form Game with the following utilities: {(0, 1): [2, 3], (1, 0): [6, -1], (0, 0): [4, 2], (1, 1): [0, 0]}
        sage: g.obtain_nash()
        [[(1, 0), (0, 1)]]
    """
    A = matrix([[4, 2], [6, 0]])
    B = matrix([[2, 3], [-1, 0]])
    g = NormalFormGame([A, B])
    g.rename('Pigs: ' + repr(g))
    return g


def MatchingPennies():
    r"""
    Return a Matching pennies game

    Consider two players who can choose to display a coin either Heads
    facing up or Tails facing up.
    If both players show the same face then player 1 wins,
    if not then player 2 wins.

    This can be modeled as a zero sum normal form game with the following
    matrix:

    .. math::

        A = \begin{pmatrix}
            1&-1\\
            -1&1\\
            \end{pmatrix}

    There is a single Nash equilibria at which both players randomly
    (with equal probability) pick heads or tails.

    This can be implemented in Sage using the following::

        sage: g = game_theory.MatchingPennies()
        sage: g
        Matching pennies: Normal Form Game with the following utilities: {(0, 1): [-1, 1], (1, 0): [-1, 1], (0, 0): [1, -1], (1, 1): [1, -1]}
        sage: g.obtain_nash()
        [[(1/2, 1/2), (1/2, 1/2)]]
    """
    A = matrix([[1, -1], [-1, 1]])
    g = NormalFormGame([A])
    g.rename('Matching pennies: ' + repr(g))
    return g
