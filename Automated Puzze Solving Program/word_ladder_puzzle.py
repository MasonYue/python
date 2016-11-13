from puzzle import Puzzle


class WordLadderPuzzle(Puzzle):
    """
    A word-ladder puzzle that may be solved, unsolved, or even unsolvable.
    """

    def __init__(self, from_word, to_word, ws):
        """
        Create a new word-ladder puzzle with the aim of stepping
        from from_word to to_word using words in ws, changing one
        character at each step.

        @type from_word: str
        @type to_word: str
        @type ws: set[str]
        @rtype: None
        """
        (self._from_word, self._to_word, self._word_set) = (from_word,
                                                            to_word, ws)
        # set of characters to use for 1-character changes
        self._chars = "abcdefghijklmnopqrstuvwxyz"

        # implement __eq__ and __str__
        # __repr__ is up to you
    def __eq__(self, other):
        """

        Return whether WordLadderPuzzle self is equivalent to other.

        @type self: WordLadderPuzzle
        @type other: WordLadderPuzzle | Any
        @rtype: bool
        >>> x = WordLadderPuzzle('cat', 'cap',set(['cat','cap','cad']))
        >>> y = WordLadderPuzzle('cat', 'cup',set(['cat','cap','cad']))
        >>> x.__eq__(y)
        False
        """
        return (type(self) == type(other) and
                self._from_word == other._from_word and
                self._to_word == other._to_word and
                self._word_set == other._word_set)

    def __str__(self):
        """
        Return a human-readable string representation of WordLadderPuzzle self.
        @type self:WordLadderPuzzle
        @rtype:str
        >>> x = WordLadderPuzzle('cat', 'cap',set(['cat','cox', 'asd', 'asdf']))
        >>> print(x)
        cat
        """
        return self._from_word

        # override extensions
        # legal extensions are WordLadderPuzzles that have a from_word that can
        # be reached from this one by changing a single letter to one of those
        # in self._chars

    def extensions(self):
        """
        Return list of extensions of WordLadderPuzzle self.

        @type self: WordLadderPuzzle
        @rtype: list[WordLadderPuzzle]
        >>> y = set(['cap','cop', 'asd', 'asdf','Aap'])
        >>> w = WordLadderPuzzle("cat", "cop", y)
        >>> z = WordLadderPuzzle("cap", "cop", y)
        >>> z in w.extensions()
        True
        """
        wlist = []
        return_list = []
        # create a  empty word list
        for word in self._word_set:
            # check every word in word list one by one
            if len(word) == len(self._from_word):
                index = 0
                n = 0
                # n is difference between two words
                # if length of word is the same with from_word, then we can
                # check their difference
                while index < len(self._from_word):
                    # check every letter one by one
                    if word[index] in self._chars:
                        # make sure every letter is legal correct
                        if word[index] == self._from_word[index]:
                            index += 1
                        else:
                            # if not same, then difference + 1
                            n += 1
                            index += 1
                    # check their difference
                    else:
                        index += 1
                        n = 999
                    # if contains illegal letter, n = 999, it's not correct
            else:
                n = 999
            if n == 1:
                wlist.append(word)
        for i in wlist:
            return_list.append((WordLadderPuzzle(i, self._to_word,
                                                 self._word_set)))
        # create new WordLadderPuzzle using new words
        return return_list

        # override is_solved
        # this WordLadderPuzzle is solved when _from_word is the same as
        # _to_word
    def is_solved(self):
        """
        Return whether WordLadderPuzzle self is solved.
        @type self:WordLadderPuzzle
        @rtype: bool
        >>> w = WordLadderPuzzle("bat", "bat", set(['cat', 'cap','cop']))
        >>> w.is_solved()
        True

        """
        return self._from_word == self._to_word


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    from puzzle_tools import breadth_first_solve, depth_first_solve
    from time import time
    with open("words.txt", "r") as words:
        word_set = set(words.read().split())
    w = WordLadderPuzzle("same", "cost", word_set)
    start = time()
    sol = breadth_first_solve(w)
    end = time()
    print("Solving word ladder from same->cost")
    print("...using breadth-first-search")
    print("Solutions: {} took {} seconds.".format(sol, end - start))
    start = time()
    sol = depth_first_solve(w)
    end = time()
    print("Solving word ladder from same->cost")
    print("...using depth-first-search")
    print("Solutions: {} took {} seconds.".format(sol, end - start))
