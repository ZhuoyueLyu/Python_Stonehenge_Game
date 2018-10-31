"""
An implementation of a state for Stonehenge.
"""
from typing import Any
from game_state import GameState


class StonehengeState(GameState):
    """
    The state of a game at a certain point in time.
    """
    def __init__(self, is_p1_turn: bool, length: int,
                 letters: list, claim: list)-> None:
        """
        Initialize this game state and set the current player based on
        is_p1_turn.
        """
        super().__init__(is_p1_turn)
        self.length = length
        self.letters = letters
        self.claim = claim
        if length == 1:
            self.board = (
                "      {}   {}\n" +
                "     /   /\n" +
                "{} - {} - {}\n" +
                "     \\ / \\ \n" +
                "  {} - {}   {}\n" +
                "       \\ \n" +
                "        {}\n").format(self.claim[0], self.claim[1],
                                       self.claim[2], self.letters[0],
                                       self.letters[1], self.claim[3],
                                       self.letters[2], self.claim[4],
                                       self.claim[5])

        if length == 2:
            self.board = (
                "        {}   {}\n" +
                "       /   / \n" +
                "  {} - {} - {}   {}\n" +
                "     / \\ / \\ / \n" +
                "{} - {} - {} - {}\n" +
                "     \\ / \\ / \\ \n" +
                "  {} - {} - {}   {}\n" +
                "       \\   \\ \n" +
                "        {}   {}\n").format(self.claim[0], self.claim[1],
                                            self.claim[2], self.letters[0],
                                            self.letters[1], self.claim[3],
                                            self.claim[4], self.letters[2],
                                            self.letters[3], self.letters[4],
                                            self.claim[5], self.letters[5],
                                            self.letters[6], self.claim[6],
                                            self.claim[7], self.claim[8])

        if length == 3:
            self.board = (
                "           {}   {}\n" +
                "          /   /\n" +
                "     {} - {} - {}   {}\n" +
                "        / \\ / \\ /\n" +
                "   {} - {} - {} - {}   {} \n" +
                "      / \\ / \\ / \\ /    \n"
                " {} - {} - {} - {} - {} \n" +
                "      \\ / \\ / \\ / \\    \n" +
                "   {} - {} - {} - {}   {} \n" +
                "        \\   \\   \\     \n" +
                "         {}   {}   {}\n")\
                .format(self.claim[0], self.claim[1],
                        self.claim[2], self.letters[0], self.letters[1],
                        self.claim[3], self.claim[4], self.letters[2],
                        self.letters[3], self.letters[4], self.claim[5],
                        self.claim[6], self.letters[5], self.letters[6],
                        self.letters[7], self.letters[8], self.claim[7],
                        self.letters[9], self.letters[10], self.letters[11],
                        self.claim[8], self.claim[9], self.claim[10],
                        self.claim[11])

        if length == 4:
            self.board = (
                "              {}   {}\n" +
                "             /   /\n" +
                "        {} - {} - {}   {}\n" +
                "           / \\ / \\ /\n" +
                "      {} - {} - {} - {}   {} \n" +
                "         / \\ / \\ / \\ /    \n"
                "    {} - {} - {} - {} - {}   {}\n" +
                "       / \\ / \\ / \\ / \\ /  \n"
                "  {} - {} - {} - {} - {} - {} \n" +
                "       \\ / \\ / \\ / \\ / \\  \n" +
                "    {} - {} - {} - {} - {}   {}\n" +
                "         \\   \\   \\   \\  \n" +
                "          {}   {}   {}   {}\n") \
                .format(self.claim[0], self.claim[1],
                        self.claim[2], self.letters[0], self.letters[1],
                        self.claim[3], self.claim[4], self.letters[2],
                        self.letters[3], self.letters[4], self.claim[5],
                        self.claim[6], self.letters[5], self.letters[6],
                        self.letters[7], self.letters[8], self.claim[7],
                        self.claim[8], self.letters[9], self.letters[10],
                        self.letters[11], self.letters[12], self.letters[13],
                        self.claim[9], self.letters[14], self.letters[15],
                        self.letters[16], self.letters[17], self.claim[10],
                        self.claim[11], self.claim[12], self.claim[13],
                        self.claim[14])

        if length == 5:
            self.board = (
                "                 {}   {}\n" +
                "                /   /\n" +
                "           {} - {} - {}   {}\n" +
                "              / \\ / \\ /\n" +
                "         {} - {} - {} - {}   {} \n" +
                "            / \\ / \\ / \\ /    \n" +
                "       {} - {} - {} - {} - {}   {}\n" +
                "          / \\ / \\ / \\ / \\ /  \n" +
                "     {} - {} - {} - {} - {} - {}   {}\n" +
                "        / \\ / \\ / \\ / \\ / \\ /\n" +
                "   {} - {} - {} - {} - {} - {} - {} \n" +
                "        \\ / \\ / \\ / \\ / \\ / \\\n" +
                "     {} - {} - {} - {} - {} - {}   {}\n" +
                "          \\   \\   \\   \\   \\\n" +
                "           {}   {}   {}   {}   {}\n")\
                .format(self.claim[0], self.claim[1],
                        self.claim[2], self.letters[0], self.letters[1],
                        self.claim[3], self.claim[4], self.letters[2],
                        self.letters[3], self.letters[4], self.claim[5],
                        self.claim[6], self.letters[5], self.letters[6],
                        self.letters[7], self.letters[8], self.claim[7],
                        self.claim[8], self.letters[9], self.letters[10],
                        self.letters[11], self.letters[12], self.letters[13],
                        self.claim[9], self.claim[10], self.letters[14],
                        self.letters[15], self.letters[16], self.letters[17],
                        self.letters[18], self.letters[19], self.claim[11],
                        self.letters[20], self.letters[21], self.letters[22],
                        self.letters[23], self.letters[24], self.claim[12],
                        self.claim[13], self.claim[14], self.claim[15],
                        self.claim[16], self.claim[17])

    def __str__(self) -> str:
        """
        Return a string representation of the current state of the game.
        """
        return self.board

    def get_possible_moves(self) -> list:
        """
        Return all possible moves that can be applied to this state.
        """
        if self.p1_turn:
            name = '2'
        else:
            name = '1'

        count = 0
        for i in self.claim:
            if i == name:
                count += 1
        over = count >= 0.5 * len(self.claim)

        moves = []
        if not over:
            for i in self.letters:
                if i.isalpha():
                    moves.append(i)
        return moves

    def make_move(self, move: Any) -> "StonehengeState":
        """
        Return the GameState that results from applying move to this GameState.
        """
        new_state = StonehengeState(self.p1_turn, self.length,
                                    self.letters[:], self.claim[:])
        state = new_state
        if new_state.length == 1:
            state = self.move_length_1(move, new_state)
        if new_state.length == 2:
            state = self.move_length_2(move, new_state)
        if new_state.length == 3:
            state = self.move_length_3(move, new_state)
        if new_state.length == 4:
            if move in ["A", "B", "J", "O", "N", "R",
                        "C", "F", "E", "I", "P", "Q"]:
                state = self.move_length_4(move, new_state)
            else:
                state = self.move_length_41(move, new_state)
        if new_state.length == 5:
            if move in ["A", "B", "U", "O", "T", "Y",
                        "C", "J", "E", "N", "V", "X"]:
                state = self.move_length_5(move, new_state)
            elif move in ["F", "I", "W"]:
                state = self.move_length_51(move, new_state)
            else:
                state = self.move_length_52(move, new_state)
        return state

    def move_length_1(self, move, new_state):
        """
        dealing with make move of length 1
        """
        for i in [["A", 1, 2, 2, 5, 0],
                  ["B", 0, 2, 2, 1, 4],
                  ["C", 0, 5, 1, 1, 3]]:
            if move == i[0]:
                if new_state.letters[i[1]].isalpha():
                    new_state.claim[i[2]] \
                        = new_state.get_current_player_name()[1]
                if new_state.letters[i[3]].isalpha():
                    new_state.claim[i[4]] \
                        = new_state.get_current_player_name()[1]
                new_state.claim[i[5]] = \
                    new_state.get_current_player_name()[1]

        new_state.letters = [self.get_current_player_name()[1]
                             if i == move else i for i in self.letters]

        return StonehengeState(not self.p1_turn, new_state.length,
                               new_state.letters, new_state.claim)

    def move_length_2(self, move, new_state):
        """
        dealing with make move of length 2
        """
        for i in [["A", 1, 2, 2, 0, 3, 6, 8],
                  ["B", 0, 2, 4, 6, 3, 5, 1],
                  ["C", 0, 0, 5, 7, 3, 4, 4],
                  ["E", 1, 6, 6, 3, 2, 3, 4],
                  ["F", 2, 7, 6, 5, 1, 3, 1],
                  ["G", 4, 3, 5, 5, 0, 3, 8]]:
            if move == i[0]:
                if new_state.letters[i[1]].isalpha():
                    new_state.claim[i[2]] \
                        = new_state.get_current_player_name()[1]
                if new_state.letters[i[3]].isalpha():
                    new_state.claim[i[4]] \
                        = new_state.get_current_player_name()[1]
                if new_state.get_current_player_name()[1] \
                        == new_state.letters[i[5]] \
                        or new_state.get_current_player_name()[1] \
                        == new_state.letters[i[6]]:
                    new_state.claim[i[7]] \
                        = new_state.get_current_player_name()[1]
        if move == "D":
            if new_state.get_current_player_name()[1] == \
                    (new_state.letters[0] or new_state.letters[6]):
                new_state.claim[8] = new_state.get_current_player_name()[1]
            if new_state.get_current_player_name()[1] == \
                    (new_state.letters[1] or new_state.letters[5]):
                new_state.claim[1] = new_state.get_current_player_name()[1]
            if new_state.get_current_player_name()[1] == \
                    (new_state.letters[2] or new_state.letters[4]):
                new_state.claim[4] = new_state.get_current_player_name()[1]
        new_state.letters = [self.get_current_player_name()[1]
                             if i == move else i for i in self.letters]

        return StonehengeState(not self.p1_turn, new_state.length,
                               new_state.letters, new_state.claim)

    def move_length_3(self, move, new_state):
        """
        dealing with make move of length 3
        """
        # First consider the move on 6 corners
        for i in [["A", 1, 2, 2, 5, 0, 3, 7, 11, 11],
                  ["B", 0, 2, 4, 8, 8, 3, 6, 9, 1],
                  ["F", 9, 9, 2, 0, 0, 6, 7, 8, 6],
                  ["J", 5, 9, 10, 11, 7, 6, 3, 1, 1],
                  ["I", 11, 5, 4, 1, 8, 5, 6, 7, 6],
                  ["L", 8, 5, 9, 10, 7, 3, 0, 7, 11]]:
            if move == i[0]:
                if new_state.letters[i[1]].isalpha():
                    new_state.claim[i[2]] \
                        = new_state.get_current_player_name()[1]
                if new_state.get_current_player_name()[1] \
                        == new_state.letters[i[3]] \
                        or new_state.get_current_player_name()[1] \
                        == new_state.letters[i[4]]:
                    new_state.claim[i[5]] \
                        = new_state.get_current_player_name()[1]
                if (new_state.get_current_player_name()[1]
                        == new_state.letters[i[6]]
                        or new_state.get_current_player_name()[1]
                        == new_state.letters[i[7]]
                        or new_state.get_current_player_name()[1]
                        == new_state.letters[i[8]]) \
                        and new_state.claim[i[9]] == "@":
                    new_state.claim[i[9]] \
                        = new_state.get_current_player_name()[1]

        # then consider the move on the middle of each side
        for i in [["C", 0, 5, 0, 3, 4, 4, 6, 10, 10],
                  ["E", 1, 8, 8, 2, 3, 4, 7, 10, 3],
                  ["K", 9, 11, 7, 2, 6, 10, 7, 4, 3]]:
            if move == i[0]:
                if (new_state.get_current_player_name()[1]
                        == new_state.letters[i[1]]
                        or new_state.get_current_player_name()[1]
                        == new_state.letters[i[2]]) \
                        and new_state.claim[i[3]] == "@":
                    new_state.claim[i[3]] \
                        = new_state.get_current_player_name()[1]
                if (new_state.get_current_player_name()[1]
                        == new_state.letters[i[4]]
                        or new_state.get_current_player_name()[1]
                        == new_state.letters[i[5]]) \
                        and new_state.claim[i[6]] == "@":
                    new_state.claim[i[6]] \
                        = new_state.get_current_player_name()[1]

                if (new_state.get_current_player_name()[1]
                        == new_state.letters[i[7]]
                        or new_state.get_current_player_name()[1]
                        == new_state.letters[i[8]]) \
                        and new_state.claim[i[9]] == "@":
                    new_state.claim[i[9]] \
                        = new_state.get_current_player_name()[1]
        # Finally consider the internal move
        internal = [["D", 2, 4, 4, 1, 6, 9, 1, 0, 7, 11, 11],
                    ["G", 2, 10, 10, 9, 3, 1, 1, 5, 7, 8, 6],
                    ["H", 4, 10, 3, 0, 3, 11, 11, 5, 6, 8, 6]]
        for i in internal:
            if move == i[0]:
                if (new_state.get_current_player_name()[1]
                        == new_state.letters[i[1]]
                        or new_state.get_current_player_name()[1]
                        == new_state.letters[i[2]]) \
                        and new_state.claim[i[3]] == "@":
                    new_state.claim[i[3]] \
                        = new_state.get_current_player_name()[1]
                if (new_state.get_current_player_name()[1]
                        == new_state.letters[i[4]]
                        or new_state.get_current_player_name()[1]
                        == new_state.letters[i[5]]
                        or new_state.get_current_player_name()[1]
                        == new_state.letters[i[6]]) \
                        and new_state.claim[i[7]] == "@":
                    new_state.claim[i[7]] \
                        = new_state.get_current_player_name()[1]

                if (new_state.get_current_player_name()[1]
                        == new_state.letters[i[8]]
                        or new_state.get_current_player_name()[1]
                        == new_state.letters[i[9]]
                        or new_state.get_current_player_name()[1]
                        == new_state.letters[i[10]]) \
                        and new_state.claim[i[11]] == "@":
                    new_state.claim[i[11]] \
                        = new_state.get_current_player_name()[1]

        new_state.letters = [self.get_current_player_name()[1]
                             if i == move else i for i in self.letters]

        return StonehengeState(not self.p1_turn, new_state.length,
                               new_state.letters, new_state.claim)

    def move_length_4(self, move, new_state):
        """
        dealing with make move of length 4
        """
        # First consider the move on 6 corners
        if move in ["A", "B", "J", "O", "N", "R"]:
            corners = [["A", 1, 2, 2, 5, 9, 0, 3, 7, 12, 17, 14],
                       ["B", 0, 2, 4, 8, 13, 10, 3, 6, 10, 14, 1],
                       ["J", 14, 11, 5, 2, 0, 0, 10, 11, 12, 13, 8],
                       ["O", 9, 11, 15, 16, 17, 9, 10, 6, 3, 1, 1],
                       ["N", 17, 7, 1, 4, 8, 10, 9, 10, 11, 12, 8],
                       ["R", 13, 7, 14, 15, 16, 9, 0, 3, 7, 12, 14]]
            for i in corners:
                new_state = self.loop1(move, new_state, i)
            return StonehengeState(not self.p1_turn, new_state.length,
                                   new_state.letters, new_state.claim)

        # then consider the move on the middle of each side
        middle = [["C", 3, 4, 4, 6, 11, 16, 13, 0, 5, 9, 0],
                  ["F", 10, 15, 12, 9, 2, 0, 0, 6, 7, 8, 6],
                  ["E", 2, 3, 4, 1, 8, 13, 10, 7, 11, 15, 3],
                  ["I", 12, 16, 5, 5, 6, 7, 6, 1, 4, 13, 10],
                  ["P", 5, 10, 12, 14, 16, 17, 9, 11, 7, 4, 3],
                  ["Q", 12, 8, 5, 14, 15, 17, 9, 2, 6, 11, 13]]
        for i in middle:
            if move == i[0]:
                # analyze the other 2 cells
                if (new_state.get_current_player_name()[1]
                        == new_state.letters[i[1]]
                        or new_state.get_current_player_name()[1]
                        == new_state.letters[i[2]]) \
                        and new_state.claim[i[3]] == "@":
                    new_state.claim[i[3]] \
                        = new_state.get_current_player_name()[1]
                # analyze the other 3 cells
                if (new_state.get_current_player_name()[1]
                        == new_state.letters[i[4]]
                        or new_state.get_current_player_name()[1]
                        == new_state.letters[i[5]]
                        or new_state.get_current_player_name()[1]
                        == new_state.letters[i[6]]) \
                        and new_state.claim[i[7]] == "@":
                    new_state.claim[i[7]] \
                        = new_state.get_current_player_name()[1]
                # analyze the other 3 cells
                if (new_state.get_current_player_name()[1]
                        == new_state.letters[i[8]]
                        or new_state.get_current_player_name()[1]
                        == new_state.letters[i[9]]
                        or new_state.get_current_player_name()[1]
                        == new_state.letters[i[10]]) \
                        and new_state.claim[i[11]] == "@":
                    new_state.claim[i[11]] \
                        = new_state.get_current_player_name()[1]
        new_state.letters = [self.get_current_player_name()[1]
                             if i == move else i for i in self.letters]

        return StonehengeState(not self.p1_turn, new_state.length,
                               new_state.letters, new_state.claim)

    def loop1(self, move, new_state, i):
        """
        A help function of move_length_4
        """
        if move == i[0]:
            # analyze another cell
            if new_state.letters[i[1]].isalpha():
                new_state.claim[i[2]] \
                    = new_state.get_current_player_name()[1]
            # analyze the other 3 cells
            if (new_state.get_current_player_name()[1]
                    == new_state.letters[i[3]]
                    or new_state.get_current_player_name()[1]
                    == new_state.letters[i[4]]
                    or new_state.get_current_player_name()[1]
                    == new_state.letters[i[5]]) \
                    and new_state.claim[i[6]] == "@":
                new_state.claim[i[6]] \
                    = new_state.get_current_player_name()[1]
            # analyze the other 4 cells
            count = 0
            for x in [new_state.letters[i[7]],
                      new_state.letters[i[8]],
                      new_state.letters[i[9]],
                      new_state.letters[i[10]]]:
                if new_state.get_current_player_name()[1] == x:
                    count += 1
            if count == 2 and new_state.claim[i[11]] == "@":
                new_state.claim[i[11]] = \
                    new_state.get_current_player_name()[1]
            new_state.letters = [self.get_current_player_name()[1]
                                 if i == move else i for i in self.letters]
        return new_state

    def loop2(self, move, new_state, i):
        """
        A help function of move_length_4
        """
        if move == i[0]:
            # analyze the other 2 cells
            if (new_state.get_current_player_name()[1]
                    == new_state.letters[i[1]]
                    or new_state.get_current_player_name()[1]
                    == new_state.letters[i[2]]) \
                    and new_state.claim[i[3]] == "@":
                new_state.claim[i[3]] \
                    = new_state.get_current_player_name()[1]

            # analyze the other 4 cells
            count = 0
            for x in [new_state.letters[i[4]],
                      new_state.letters[i[5]],
                      new_state.letters[i[6]],
                      new_state.letters[i[7]]]:
                if new_state.get_current_player_name()[1] == x:
                    count += 1
            if count == 2 and new_state.claim[i[8]] == "@":
                new_state.claim[i[8]] = \
                    new_state.get_current_player_name()[1]

            # analyze the other 4 cells
            count = 0
            for x in [new_state.letters[i[9]],
                      new_state.letters[i[10]],
                      new_state.letters[i[11]],
                      new_state.letters[i[12]]]:
                if new_state.get_current_player_name()[1] == x:
                    count += 1
            if count == 2 and new_state.claim[i[13]] == "@":
                new_state.claim[i[13]] = \
                    new_state.get_current_player_name()[1]
            new_state.letters = [self.get_current_player_name()[1]
                                 if i == move else i for i in self.letters]
        return new_state

    def loop3(self, move, new_state, i):
        """
        A help function of move_length_4
        """
        if move == i[0]:
            # analyze the other 3 cells
            if (new_state.get_current_player_name()[1]
                    == new_state.letters[i[1]]
                    or new_state.get_current_player_name()[1]
                    == new_state.letters[i[2]]
                    or new_state.get_current_player_name()[1]
                    == new_state.letters[i[3]]) \
                    and new_state.claim[i[4]] == "@":
                new_state.claim[i[4]] \
                    = new_state.get_current_player_name()[1]

            # analyze the other 3 cells
            if (new_state.get_current_player_name()[1]
                    == new_state.letters[i[5]]
                    or new_state.get_current_player_name()[1]
                    == new_state.letters[i[6]]
                    or new_state.get_current_player_name()[1]
                    == new_state.letters[i[7]]) \
                    and new_state.claim[i[8]] == "@":
                new_state.claim[i[8]] \
                    = new_state.get_current_player_name()[1]

            # analyze the other 4 cells
            count = 0
            for x in [new_state.letters[i[9]],
                      new_state.letters[i[10]],
                      new_state.letters[i[11]],
                      new_state.letters[i[12]]]:
                if new_state.get_current_player_name()[1] == x:
                    count += 1
            if count == 2 and new_state.claim[i[13]] == "@":
                new_state.claim[i[13]] = \
                    new_state.get_current_player_name()[1]

            new_state.letters = [self.get_current_player_name()[1]
                                 if i == move else i for i in self.letters]
        return new_state

    def move_length_41(self, move, new_state: "StonehengeState"):
        """
        dealing with make move of length 4
        """
        # Then consider the internal1 move
        new1_state = new_state
        if move in ["D", "K", "M"]:
            for i in [["D", 2, 4, 4, 1, 6, 10, 14, 1, 0, 7, 12, 17, 14],
                      ["K", 5, 15, 12, 1, 3, 6, 14, 1, 9, 11, 12, 13, 8],
                      ["M", 8, 16, 5, 9, 10, 11, 13, 8, 0, 3, 7, 17, 14]]:
                new1_state = self.loop2(move, new_state, i)
        # Finally consider the internal2 move
        internal2 = [["G", 2, 11, 16, 13, 5, 7, 8, 6, 1, 3, 10, 14, 1],
                     ["H", 4, 11, 15, 3, 5, 6, 8, 6, 0, 3, 12, 17, 14],
                     ["L", 2, 6, 16, 13, 4, 7, 15, 3, 9, 10, 12, 13, 8]]
        if move in ["G", "H", "L"]:
            for i in internal2:
                new1_state = self.loop3(move, new_state, i)
        return StonehengeState(not self.p1_turn, new1_state.length,
                               new1_state.letters, new1_state.claim)

    def loop51(self, move, new_state, i):
        """
        A help function of move_length_5
        """
        if move == i[0]:
            # analyze another cell
            if new_state.letters[i[1]].isalpha():
                new_state.claim[i[2]] \
                    = new_state.get_current_player_name()[1]

            # analyze the other 4 cells
            count = 0
            for x in [new_state.letters[i[3]],
                      new_state.letters[i[4]],
                      new_state.letters[i[5]],
                      new_state.letters[i[6]]]:
                if new_state.get_current_player_name()[1] == x:
                    count += 1
            if count == 2 and new_state.claim[i[7]] == "@":
                new_state.claim[i[7]] = \
                    new_state.get_current_player_name()[1]

            # analyze the other 5 cells
            count = 0
            for x in [new_state.letters[i[8]],
                      new_state.letters[i[9]],
                      new_state.letters[i[10]],
                      new_state.letters[i[11]],
                      new_state.letters[i[12]]]:
                if new_state.get_current_player_name()[1] == x:
                    count += 1
            if count == 2 and new_state.claim[i[13]] == "@":
                new_state.claim[i[13]] = \
                    new_state.get_current_player_name()[1]
            new_state.letters = [self.get_current_player_name()[1]
                                 if i == move else i for i in self.letters]
        return new_state

    def loop52(self, move, new_state, i):
        """
        A help function of move_length_5
        """
        if move == i[0]:
            # analyze the other 2 cells
            if (new_state.get_current_player_name()[1]
                    == new_state.letters[i[1]]
                    or new_state.get_current_player_name()[1]
                    == new_state.letters[i[2]]) \
                    and new_state.claim[i[3]] == "@":
                new_state.claim[i[3]] \
                    = new_state.get_current_player_name()[1]

            # analyze the other 4 cells
            count = 0
            for x in [new_state.letters[i[4]],
                      new_state.letters[i[5]],
                      new_state.letters[i[6]],
                      new_state.letters[i[7]]]:
                if new_state.get_current_player_name()[1] == x:
                    count += 1
            if count == 2 and new_state.claim[i[8]] == "@":
                new_state.claim[i[8]] = \
                    new_state.get_current_player_name()[1]

            # analyze the other 4 cells
            count = 0
            for x in [new_state.letters[i[9]],
                      new_state.letters[i[10]],
                      new_state.letters[i[11]],
                      new_state.letters[i[12]]]:
                if new_state.get_current_player_name()[1] == x:
                    count += 1
            if count == 2 and new_state.claim[i[13]] == "@":
                new_state.claim[i[13]] = \
                    new_state.get_current_player_name()[1]
            new_state.letters = [self.get_current_player_name()[1]
                                 if i == move else i for i in self.letters]
        return new_state

    def move_length_5(self, move, new_state):
        """
        dealing with make move of length 5
        """
        # First consider the move on 6 corners
        new1_state = new_state
        if move in ["A", "B", "O", "U", "T", "Y"]:
            corners = [["A", 1, 2, 2, 5, 9, 14, 0, 3, 7, 12, 18, 24, 17],
                       ["B", 0, 2, 4, 8, 13, 19, 12, 3, 6, 10, 15, 20, 1],
                       ["O", 20, 13, 9, 5, 2, 0, 0, 15, 16, 17, 18, 19, 10],
                       ["U", 14, 13, 21, 22, 23, 24, 11, 1, 3, 6, 10, 15, 1],
                       ["T", 24, 9, 1, 4, 8, 13, 12, 14, 15, 16, 17, 18, 10],
                       ["Y", 19, 9, 20, 21, 22, 23, 11, 0, 3, 7, 12, 18, 17]]
            for i in corners:
                new1_state = self.loop51(move, new_state, i)

        if move in ["C", "E", "J", "N", "V", "X"]:
            # then consider the move on the middle1 of each side
            middle1 = [["C", 3, 4, 4, 0, 5, 9, 14, 0, 6, 11, 17, 23, 16],
                       ["E", 2, 3, 4, 1, 8, 13, 19, 12, 7, 11, 16, 21, 3],
                       ["J", 15, 21, 14, 10, 11, 12, 13, 8, 0, 2, 5, 14, 0],
                       ["N", 18, 23, 7, 1, 4, 8, 19, 12, 9, 10, 11, 12, 8],
                       ["V", 9, 15, 14, 20, 22, 23, 24, 11, 4, 7, 11, 16, 3],
                       ["X", 13, 18, 7, 20, 21, 22, 24, 11, 2, 6, 11, 17, 16]]
            for i in middle1:
                new1_state = self.loop52(move, new_state, i)
        return StonehengeState(not self.p1_turn, new1_state.length,
                               new1_state.letters, new1_state.claim)

    def loop53(self, move, new_state, i):
        """
        A help function of move_length_5
        """
        if move == i[0]:
            # analyze the other 3 cells
            if (new_state.get_current_player_name()[1]
                    == new_state.letters[i[1]]
                    or new_state.get_current_player_name()[1]
                    == new_state.letters[i[2]]
                    or new_state.get_current_player_name()[1]
                    == new_state.letters[i[3]]) \
                    and new_state.claim[i[4]] == "@":
                new_state.claim[i[4]] \
                    = new_state.get_current_player_name()[1]

            # analyze the other 3 cells
            if (new_state.get_current_player_name()[1]
                    == new_state.letters[i[5]]
                    or new_state.get_current_player_name()[1]
                    == new_state.letters[i[6]]
                    or new_state.get_current_player_name()[1]
                    == new_state.letters[i[7]]) \
                    and new_state.claim[i[8]] == "@":
                new_state.claim[i[8]] \
                    = new_state.get_current_player_name()[1]

            # analyze the other 4 cells
            count = 0
            for x in [new_state.letters[i[9]],
                      new_state.letters[i[10]],
                      new_state.letters[i[11]],
                      new_state.letters[i[12]]]:
                if new_state.get_current_player_name()[1] == x:
                    count += 1
            if count == 2 and new_state.claim[i[13]] == "@":
                new_state.claim[i[13]] = \
                    new_state.get_current_player_name()[1]
            new_state.letters = [self.get_current_player_name()[1]
                                 if i == move else i for i in self.letters]
        return new_state

    def move_length_51(self, move, new_state):
        """
        Help function of make move
        """
        # then consider the move on the middle2 of each side
        new1_state = new_state
        if move in ["F", "I", "W"]:
            middle2 = [["F", 6, 7, 8, 6, 10, 16, 22, 15, 0, 2, 9, 14, 0],
                       ["I", 5, 6, 7, 6, 12, 17, 22, 5, 1, 4, 13, 19, 12],
                       ["W", 5, 10, 16, 15, 8, 12, 17, 5, 20, 21, 24, 23, 11]]
            for i in middle2:
                new1_state = self.loop53(move, new_state, i)
        return StonehengeState(not self.p1_turn, new1_state.length,
                               new1_state.letters, new1_state.claim)

    def loop54(self, move, new_state, i):
        """
        A help function of move_length_5
        """
        if move == i[0]:
            # analyze the other 2 cells
            if (new_state.get_current_player_name()[1]
                    == new_state.letters[i[1]]
                    or new_state.get_current_player_name()[1]
                    == new_state.letters[i[2]]) \
                    and new_state.claim[i[3]] == "@":
                new_state.claim[i[3]] \
                    = new_state.get_current_player_name()[1]

            # analyze the other 5 cells
            count = 0
            for x in [new_state.letters[i[4]],
                      new_state.letters[i[5]],
                      new_state.letters[i[6]],
                      new_state.letters[i[7]],
                      new_state.letters[i[8]]]:
                if new_state.get_current_player_name()[1] == x:
                    count += 1
            if count == 2 and new_state.claim[i[9]] == "@":
                new_state.claim[i[9]] = \
                    new_state.get_current_player_name()[1]

            # analyze the other 5 cells
            count = 0
            for x in [new_state.letters[i[10]],
                      new_state.letters[i[11]],
                      new_state.letters[i[12]],
                      new_state.letters[i[13]],
                      new_state.letters[i[14]]]:
                if new_state.get_current_player_name()[1] == x:
                    count += 1
            if count == 2 and new_state.claim[i[15]] == "@":
                new_state.claim[i[15]] = \
                    new_state.get_current_player_name()[1]
            new_state.letters = [self.get_current_player_name()[1]
                                 if i == move else i for i in self.letters]
        return new_state

    def loop55(self, move, new_state, i):
        """
        A help function of move_length_5
        """
        if move == i[0]:

            # analyze the other 3 cells
            if (new_state.get_current_player_name()[1]
                    == new_state.letters[i[1]]
                    or new_state.get_current_player_name()[1]
                    == new_state.letters[i[2]]
                    or new_state.get_current_player_name()[1]
                    == new_state.letters[i[3]]) \
                    and new_state.claim[i[4]] == "@":
                new_state.claim[i[4]] \
                    = new_state.get_current_player_name()[1]

            # analyze the other 4 cells
            count = 0
            for x in [new_state.letters[i[5]],
                      new_state.letters[i[6]],
                      new_state.letters[i[7]],
                      new_state.letters[i[8]]]:
                if new_state.get_current_player_name()[1] == x:
                    count += 1
            if count == 2 and new_state.claim[i[9]] == "@":
                new_state.claim[i[9]] = \
                    new_state.get_current_player_name()[1]

            # analyze the other 5 cells
            count = 0
            for x in [new_state.letters[i[10]],
                      new_state.letters[i[11]],
                      new_state.letters[i[12]],
                      new_state.letters[i[13]],
                      new_state.letters[i[14]]]:
                if new_state.get_current_player_name()[1] == x:
                    count += 1
            if count == 2 and new_state.claim[i[15]] == "@":
                new_state.claim[i[15]] = \
                    new_state.get_current_player_name()[1]
            new_state.letters = [self.get_current_player_name()[1]
                                 if i == move else i for i in self.letters]
        return new_state

    def loop56(self, move, new_state, i):
        """
        A help function of move_length_5
        """
        if move == i[0]:

            # analyze the other 4 cells
            count = 0
            for x in [new_state.letters[i[1]],
                      new_state.letters[i[2]],
                      new_state.letters[i[3]],
                      new_state.letters[i[4]]]:
                if new_state.get_current_player_name()[1] == x:
                    count += 1
            if count == 2 and new_state.claim[i[5]] == "@":
                new_state.claim[i[5]] = \
                    new_state.get_current_player_name()[1]

            # analyze the other 4 cells
            count = 0
            for x in [new_state.letters[i[6]],
                      new_state.letters[i[7]],
                      new_state.letters[i[8]],
                      new_state.letters[i[9]]]:
                if new_state.get_current_player_name()[1] == x:
                    count += 1
            if count == 2 and new_state.claim[i[10]] == "@":
                new_state.claim[i[10]] = \
                    new_state.get_current_player_name()[1]

            # analyze the other 4 cells
            count = 0
            for x in [new_state.letters[i[11]],
                      new_state.letters[i[12]],
                      new_state.letters[i[13]],
                      new_state.letters[i[14]]]:
                if new_state.get_current_player_name()[1] == x:
                    count += 1
            if count == 2 and new_state.claim[i[15]] == "@":
                new_state.claim[i[15]] = \
                    new_state.get_current_player_name()[1]

            new_state.letters = [self.get_current_player_name()[1]
                                 if i == move else i for i in self.letters]
        return new_state

    def move_length_52(self, move, new_state):
        """
        Help function of make move
        """
        # Then consider the internal1 move
        new1_state = new_state
        if move in ["D", "P", "S"]:
            for i in [["D", 2, 4, 4, 1, 6, 10, 15, 20, 1,
                       0, 7, 12, 18, 24, 17],
                      ["P", 9, 21, 14, 14, 16, 17, 18, 19,
                       0, 1, 3, 6, 10, 20, 1],
                      ["S", 13, 23, 7, 14, 15, 16, 17, 19,
                       10, 0, 3, 7, 12, 24, 17]]:
                new1_state = self.loop54(move, new_state, i)

        # Then consider the internal2 move
        internal2 = \
            [["G", 5, 7, 8, 6, 2, 11, 17, 23, 16, 1, 3, 10, 15, 20, 1],
             ["H", 5, 6, 8, 6, 4, 11, 16, 21, 3, 0, 3, 12, 18, 24, 17],
             ["K", 5, 16, 22, 15, 9, 11, 12, 13, 8, 1, 3, 6, 15, 20, 1],
             ["M", 8, 17, 22, 5, 9, 10, 11, 13, 8, 0, 3, 7, 18, 24, 17],
             ["Q", 5, 10, 22, 15, 4, 7, 11, 21, 3, 14, 15, 17, 18, 19, 10],
             ["R", 8, 12, 22, 5, 2, 6, 11, 23, 16, 14, 15, 16, 18, 19, 10]]
        if move in ["G", "H", "K", "M", "Q", "R"]:
            for i in internal2:
                new1_state = self.loop55(move, new_state, i)

        # Finally consider the move "L"
        internal3 = [["L", 9, 10, 12, 13, 8, 2, 6,
                      17, 23, 16, 4, 7, 16, 21, 3]]
        if move in ["L"]:
            for i in internal3:
                new1_state = self.loop56(move, new_state, i)
        return StonehengeState(not self.p1_turn, new1_state.length,
                               new1_state.letters, new1_state.claim)

    def __repr__(self) -> str:
        """
        Return a representation of this state (which can be used for
        equality testing).
        """
        return "P1's Turn: {} - Board: {}".format(self.p1_turn,
                                                  self.board)

    def rough_outcome(self) -> float:
        """
        Return an estimate in interval [LOSE, WIN] of best outcome the current
        player can guarantee from state self.
        """

        if self.p1_turn:
            name = '2'
        else:
            name = '1'

        count = 0
        for i in self.claim:
            if i == name:
                count += 1
        over = (self.get_possible_moves() == []) or \
               (count >= 0.5 * len(self.claim))

        result = []
        if over:
            return -1
        else:
            for move in self.get_possible_moves():
                new_state = self.make_move(move)
                if new_state.rough_outcome() == -1:
                    result.append(1)
                else:
                    result.append(0)
            if 1 in result:
                return 1
            return -1


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
