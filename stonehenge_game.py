"""
An implementation of StonehengeGame
"""
from game import Game
from stonehenge_state import StonehengeState


class StonehengeGame(Game):
    """
    Abstract class for a game to be played with two players.
    """

    def __init__(self, p1_starts):
        """
        Initialize this Game, using p1_starts to find who the first player is.

        :param p1_starts: A boolean representing whether Player 1 is the first
                          to make a move.
        :type p1_starts: bool
        """
        length = int(input("Enter the side length of the board: "))
        if length == 1:
            letter = ["A", "B", "C"]
            claim = ["@", "@", "@", "@", "@", "@"]
        elif length == 2:
            letter = ["A", "B", "C", "D", "E", "F", "G"]
            claim = ["@", "@", "@", "@", "@", "@",
                     "@", "@", "@"]
        elif length == 3:
            letter = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                      "K", "L"]
            claim = ["@", "@", "@", "@", "@", "@",
                     "@", "@", "@", "@", "@", "@"]
        elif length == 4:
            letter = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                      "K", "L", "M", "N", "O", "P", "Q", "R"]
            claim = ["@", "@", "@", "@", "@", "@",
                     "@", "@", "@", "@", "@", "@",
                     "@", "@", "@"]
        elif length == 5:
            letter = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                      "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                      "U", "V", "W", "X", "Y"]
            claim = ["@", "@", "@", "@", "@", "@",
                     "@", "@", "@", "@", "@", "@",
                     "@", "@", "@", "@", "@", "@"]
        else:
            raise NotImplementedError
        self.current_state = StonehengeState(p1_starts, length, letter, claim)

    def get_instructions(self):
        """
        Return the instructions for this Game.

        :return: The instructions for this Game.
        :rtype: str
        """
        instructions = "Players take turns claiming cells (in the diagram: " \
                       "circles labelled with a capital letter). When a player" \
                       " captures at least half of the cells in a ley-line " \
                       ", then the player captures that ley-line." \
                       " The  first player to capture at least half of the " \
                       "ley-lines is the winner. A ley-line, once claimed," \
                       " cannot be taken by the other player."
        return instructions

    def is_over(self, state):
        """
        Return whether or not this game is over.

        :return: True if the game is over, False otherwise.
        :rtype: bool
        """
        if state.p1_turn:
            name = '2'
        else:
            name = '1'

        count = 0
        for i in state.claim:
            if i == name:
                count += 1
        return (state.get_possible_moves() == []) or \
               (count >= 0.5 * len(state.claim))

    def is_winner(self, player):
        """
        Return whether player has won the game.

        Precondition: player is 'p1' or 'p2'.

        :param player: The player to check.
        :type player: str
        :return: Whether player has won or not.
        :rtype: bool
        """
        # (self.current_state.get_current_player_name() == player
        #  and
        return (self.current_state.get_current_player_name() != player
                and self.is_over(self.current_state))

    def str_to_move(self, string):
        """
        Return the move that string represents. If string is not a move,
        return an invalid move (for example, "0" ).

        :param string:
        :type string:
        :return:
        :rtype:
        """
        if not string.strip().isalpha():
            return 0
        return string


if __name__ == "__main__":
    from python_ta import check_all

    check_all(config="a2_pyta.txt")
