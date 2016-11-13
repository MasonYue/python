from puzzle import Puzzle


class GridPegSolitairePuzzle(Puzzle):
    """
    Snapshot of peg solitaire on a rectangular grid. May be solved,
    unsolved, or even unsolvable.
    """

    def __init__(self, marker, marker_set):
        """
        Create a new GridPegSolitairePuzzle self with
        marker indicating pegs, spaces, and unused
        and marker_set indicating allowed markers.

        @type marker: list[list[str]]
        @type marker_set: set[str]
                          "#" for unused, "*" for peg, "." for empty
        """
        assert isinstance(marker, list)
        assert len(marker) > 0
        assert all([len(x) == len(marker[0]) for x in marker[1:]])
        assert all([all(x in marker_set for x in row) for row in marker])
        assert all([x == "*" or x == "." or x == "#" for x in marker_set])
        self._marker, self._marker_set = marker, marker_set

    # implement __eq__, __str__ methods
    # __repr__ is up to you
    def __eq__(self, other):
        """
        Return whether GridPegSolitairePuzzle self is equivalent to other.
        @type self: GridPegSolitairePuzzle
        @type other: GridPegSolitairePuzzle
        @rtype: bool
        >>> grid = [["*", "*", "*", "*", "*"],["*", "*", "*", "*", "*"]]
        >>> gpsp = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
        >>> xy = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
        >>> xy.__eq__(gpsp)
        True
        """
        return (type(self) == type(other) and
                self._marker == other._marker and
                self._marker_set == other._marker_set)

    def __str__(self):
        """
        Return a human-readable string representation of GridPegPuzzle self.
        @type self:GridPegSolitairePuzzle
        @rtype:str
        >>> grid = [["*", "*", "*", "*", "*"],["*", "*", "*", "*", "*"]]
        >>> xy = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
        >>> print(xy)
        *****
        *****
        <BLANKLINE>
        """
        result = ''
        for i in self._marker:
            for m in i:
                result += m
            result += '\n'
        return result

    # override extensions
    # legal extensions consist of all configurations that can be reached by
    # making a single jump from this configuration

    def extensions(self):
        """
        @type self: GridPegSolitairePuzzle
        @rtype: list[GridPegSolitairePuzzle]
        >>> grid = [[".", "*", "*", "*"]]
        >>> gpsp = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
        >>> x = [["*", ".", ".", "*"]]
        >>> y = GridPegSolitairePuzzle(x, {"*", ".", "#"})
        >>> y in gpsp.extensions()
        True

        """
        row_number = 0
        result = []
        # set initial row_number is 0 and result is a list
        for i in self._marker:
            index = 0
            for m in i:
                if m == '.':
                    # locate "."
                    if index < len(self._marker[0])-2 and i[index + 1] == '*' \
                            and i[index + 2] == '*':
                        # if right next two is '*' and length is enough,
                        #  jump left
                        new_line = i[:index] + ['*', '.', '.'] + i[index + 3:]
                        # change it to a new line
                        new_marker = self._marker.copy()
                        # copy _marker to avoid change original data
                        new_marker[row_number] = new_line
                        # change the row
                        result.append(GridPegSolitairePuzzle(new_marker,
                                                             self._marker_set))
                    # jump left

                    if index > 1 and i[index - 2] == '*' \
                            and i[index - 1] == '*':
                        # if left next two is '*' and length is enough,
                        #  jump right
                        new_line = i[:index-2] + ['.', '.', '*'] + i[index + 1:]
                        # change it to a new line
                        new_marker = self._marker.copy()
                        # copy _marker to avoid change original data
                        new_marker[row_number] = new_line
                        # change the row
                        result.append(GridPegSolitairePuzzle(new_marker,
                                                             self._marker_set))
                    # jump right

                    if row_number < len(self._marker) - 2 \
                            and self._marker[row_number + 1][index] == '*' \
                            and self._marker[row_number + 2][index] == '*':
                        # if top next two is '*' and length is enough, jump down

                        new_line = i[:index] + ['*'] + i[index + 1:]
                        # change first line
                        new_line2 = self._marker[row_number + 1][:index]\
                            + ['.']\
                            + self._marker[row_number + 1][index + 1:]
                        # change first top line
                        new_line3 = self._marker[row_number + 2][:index] +\
                            ['.'] +\
                            self._marker[row_number + 2][index + 1:]
                    # change second top line
                        new_marker = self._marker.copy()
                        new_marker[row_number] = new_line
                        new_marker[row_number + 1] = new_line2
                        new_marker[row_number + 2] = new_line3
                    # append all three line
                        result.append(GridPegSolitairePuzzle(new_marker,
                                                             self._marker_set))
                # jump down

                    if row_number > 1 \
                            and self._marker[row_number - 1][index] == '*' \
                            and self._marker[row_number - 2][index] == '*':
                        # if bottom next tow is '*', jump above
                        new_line = i[:index] + ['*'] + i[index + 1:]
                        new_line2 = self._marker[row_number - 1][:index]\
                            + ['.'] +\
                            self._marker[row_number - 1][index + 1:]
                        new_line3 = self._marker[row_number - 2][:index]\
                            + ['.'] +\
                            self._marker[row_number - 2][index + 1:]
                        # change all three line
                        new_marker = self._marker.copy()
                        new_marker[row_number] = new_line
                        new_marker[row_number - 1] = new_line2
                        new_marker[row_number - 2] = new_line3
                    # append all three line
                        result.append(GridPegSolitairePuzzle(new_marker,
                                                             self._marker_set))
                # jump above
                index += 1
            else:
                index += 1
            row_number += 1
        return result

    # override is_solved
    # A configuration is solved when there is exactly one "*" left
    def is_solved(self):
        """
        Return whether SudokuPuzzle self is solved.
        @type self:GridPegSolitairePuzzle
        @rtype:bool
        >>> grid = [["*", "*", "*", "*", "*"],["*", "*", ".", "*", "*"]]
        >>> xy = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
        >>> xy.is_solved()
        False
        >>> grid = [[".", ".", "#", ".", "."],[".", ".", ".", ".", "*"]]
        >>> xy = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
        >>> xy.is_solved()
        True
        """
        n = 0
        # n is number of '*'
        for i in self._marker:
            for m in i:
                if m == '*':
                    n += 1
        # check every position, if is '*', then n + 1
        return n == 1
        # is solved if only one '*'

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    from puzzle_tools import depth_first_solve

    grid = [["*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*"],
            ["*", "*", ".", "*", "*"],
            ["*", "*", "*", "*", "*"]]
    gpsp = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
    import time

    start = time.time()
    solution = depth_first_solve(gpsp)
    end = time.time()
    print("Solved 5x5 peg solitaire in {} seconds.".format(end - start))
    print("Using depth-first: \n{}".format(solution))
