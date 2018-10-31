"""
A module for strategies.

NOTE: Make sure this file adheres to python-ta.
Adjust the type annotations as needed, and implement both a recursive
and an iterative version of minimax.
"""
from typing import Any
import copy
from trees_api_mond import Tree
from stack_api import Stack


# TODO: Adjust the type annotation as needed.


def interactive_strategy(game: Any) -> Any:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)


def rough_outcome_strategy(game: Any) -> Any:
    """
    Return a move for game by picking a move which results in a state with
    the lowest rough_outcome() for the opponent.

    NOTE: game.rough_outcome() should do the following:
        - For a state that's over, it returns the score for the current
          player of that state.
        - For a state that's not over:
            - If there is a move that results in the current player winning,
              return 1.
            - If all moves result in states where the other player can
              immediately win, return -1.
            - Otherwise; return a number between -1 and 1 corresponding to how
              'likely' the current player will win from the current state.

        In essence: rough_outcome() will only look 1 or 2 states ahead to
        'guess' the outcome of the game, but no further. It's better than
        random, but worse than minimax.
    """
    current_state = game.current_state
    best_move = None
    best_outcome = -2  # Temporarily -- just so we can replace this easily later

    # Get the move that results in the lowest rough_outcome for the opponent
    for move in current_state.get_possible_moves():
        new_state = current_state.make_move(move)

        # We multiply the below by -1 since a state that's bad for the opponent
        # is good for us.
        guessed_score = new_state.rough_outcome() * -1
        if guessed_score > best_outcome:
            best_outcome = guessed_score
            best_move = move

    # Return the move that resulted in the best rough_outcome
    return best_move


# TODO: Implement a recursive version of the minimax strategy.

def recursive_minimax_strategy(game: Any) -> Any:
    """
    Using recursive structure,
    return a move for game by picking a move
    which garantee the current player to win,
    otherwise, pick a move which is available
    """
    lista = []
    if game.current_state.p1_turn:
        for i in game.current_state.get_possible_moves():
            game2 = copy.deepcopy(game)
            new_state = game2.current_state.make_move(i)
            game2.current_state = new_state
            lista.append(recursive1(game2, []))

    else:
        for i in game.current_state.get_possible_moves():
            game2 = copy.deepcopy(game)
            new_state = game2.current_state.make_move(i)
            game2.current_state = new_state
            lista.append(recursive2(game2, []))

    if 1 in lista:
        return game.current_state.get_possible_moves()[lista.index(1)]
    return game.current_state.get_possible_moves()[0]


def recursive1(game2: Any, t: list) -> int:
    """
    A help function of recursive_minimax_strategy
    """
    if game2.is_over(game2.current_state):
        if game2.is_winner("p1"):
            return 1
        if game2.is_winner("p2"):
            return -1
        return 0

    else:
        for i in game2.current_state.get_possible_moves():
            game3 = copy.deepcopy(game2)
            new_state = game3.current_state.make_move(i)
            game3.current_state = new_state
            t.append(recursive1(game3, []))
        if not game2.current_state.p1_turn and -1 in t:
            return -1
        return max(t)


def recursive2(game2: Any, t: list) -> int:
    """
    A help function of recursive_minimax_strategy
    """
    if game2.is_over(game2.current_state):
        if game2.is_winner("p1"):
            return -1
        if game2.is_winner("p2"):
            return 1
        return 0

    else:
        for i in game2.current_state.get_possible_moves():
            game3 = copy.deepcopy(game2)
            new_state = game3.current_state.make_move(i)
            game3.current_state = new_state
            t.append(recursive2(game3, []))
        if game2.current_state.p1_turn and -1 in t:
            return -1
        return max(t)


# TODO: Implement an iterative version of the minimax strategy.
def iterative_minimax_strategy(game: Any) -> Any:
    """
    Return a move for game by iterative minimax strategy.
    """
    s = Stack()
    id0 = 0
    d = {0: Tree([id0, game, None])}
    s.add(0)

    while not s.is_empty():
        id1 = s.remove()
        item = [id1]
        if d[id1].children == []:
            for move in d[id1].value[1].current_state.get_possible_moves():
                game1 = copy.deepcopy(d[id1].value[1])
                game1.current_state = game1.current_state.make_move(move)
                id0 += 1
                d[id0] = Tree([id0, game1, None])
                d[id1].children.append(id0)
                item.append(id0)
        else:
            item.extend(d[id1].children)
        for num in item:
            if d[num].value[1].is_over(d[num].value[1].current_state):
                d[num].value[2] = -1
            elif d[num].children != [] and all(d[x].value[2] is not None
                                               for x in d[num].children):
                d[num].value[2] = max([(-1) * d[y].value[2]
                                       for y in d[num].children])
            else:
                s.add(num)
    i = 0
    for q in d[0].children:
        if d[q].value[2] == -1:
            i = d[0].children.index(q)
    return game.current_state.get_possible_moves()[i]


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
