from puzzle import Puzzle


class MNPuzzle(Puzzle):
    """
    An nxm puzzle, like the 15-puzzle, which may be solved, unsolved,
    or even unsolvable.
    """

    def __init__(self, from_grid, to_grid):
        """
        MNPuzzle in state from_grid, working towards
        state to_grid

        @param MNPuzzle self: this MNPuzzle
        @param tuple[tuple[str]] from_grid: current configuration
        @param tuple[tuple[str]] to_grid: solution configuration
        @rtype: None
        """
        # represent grid symbols with letters or numerals
        # represent the empty space with a "*"
        assert len(from_grid) > 0
        assert all([len(r) == len(from_grid[0]) for r in from_grid])
        assert all([len(r) == len(to_grid[0]) for r in to_grid])
        self.n, self.m = len(from_grid), len(from_grid[0])
        self.from_grid, self.to_grid = from_grid, to_grid

    # TODO
    # implement __eq__ and __str__
    # __repr__ is up to you
    def __eq__(self, other):
        """
        @type self:MNPuzzle
        @type other:MNPuzzle
        @rtype: bool
        >>> target_grid = (("1", "2", "3"), ("4", "5", "*"))
        >>> start_grid = (("*", "2", "3"), ("1", "4", "5"))
        >>> x = MNPuzzle(start_grid,target_grid)
        >>> y = MNPuzzle(start_grid,target_grid)
        >>> x.__eq__(y)
        True
        """

        return(type(self) == type(other) and
               self.from_grid == other.from_grid and
               self.to_grid == other.to_grid)

    def __str__(self):
        """
        Return a human-readable string representation of MNPuzzle self.
        @type self:MNPuzzle
        >>> target_grid = (("1", "2", "3"), ("4", "5", "*"))
        >>> start_grid = (("*", "2", "3"), ("1", "4", "5"))
        >>> x = MNPuzzle(start_grid,target_grid)
        >>> print(x)
        *23
        145
        <BLANKLINE>
        """
        result = ''
        for i in self.from_grid:
            for m in i:
                result += str(m)
            result += '\n'
        return result

    # override extensions
    # legal extensions are configurations that can be reached by swapping one
    # symbol to the left, right, above, or below "*" with "*"

    def extensions(self):
        """
        Return list of extensions of SudokuPuzzle self.

        @type self: MNPuzzle
        @rtype: list[MNPuzzle]
        >>> target_grid = (("1", "2","3"), ("4", "5", "*"))
        >>> start_grid = (("1", "2", "3"), ("4", "5", "*"))
        >>> x = MNPuzzle(start_grid,target_grid)
        >>> y = x.extensions()
        >>> MNPuzzle((("1", "2","3"), ("4", "*", "5")),target_grid) in y
        True
        """

        def to_right(_list, _row_number, _index):
            """
            move '*' to right
            @type _list: list
            @type _row_number: int
            @type _index: int
            @rtype: tuple
            """
            y = list(_list[_row_number])
            y[_index] = y[_index+1]
            y[_index+1] = '*'
            x[_row_number] = tuple(y)

        def to_left(_list, _row_number, _index):
            """
            move '*' to left
            @type _list: list
            @type _row_number: int
            @type _index: int
            @rtype: tuple
            """
            y = list(_list[_row_number])
            y[_index] = y[_index-1]
            y[_index-1] = '*'
            x[_row_number] = tuple(y)

        def to_below(_list, _row_number, _index):
            """
            move '*' to below
            @type _list: list
            @type _row_number: int
            @type _index: int
            @rtype: tuple
            """
            y = list(_list[_row_number + 1])
            # second line
            z = list(_list[_row_number])  # first line
            z[_index] = y[_index]
            y[_index] = '*'
            x[_row_number] = tuple(z)
            x[_row_number + 1] = tuple(y)
            # to below

        def to_upper(_list, _row_number, _index):
            """
            move '*' up
            @type _list: list
            @type _row_number: int
            @type _index: int
            @rtype: tuple
            """
            y = list(_list[_row_number - 1])
            # upper line
            z = list(_list[_row_number])  # first line
            z[_index] = y[_index]
            y[_index] = '*'
            x[_row_number] = tuple(z)
            x[_row_number - 1] = tuple(y)
            # to up
        new_start_grid = list(self.from_grid)
        # change from_grid to a list
        row_number = 0
        result = []
        for i in new_start_grid:
            if '*' in i:
                index = i.index('*')
                break
            else:
                row_number += 1
        # find the location of '*'
        if row_number == 0:
            # first case: '*' is in first row
            x = new_start_grid.copy()
            to_below(x, row_number, index)
            result.append(MNPuzzle(tuple(x), self.to_grid))  # to below
            # change it to below
            if index == 0:
                x = new_start_grid.copy()
                to_right(x, row_number, index)
                result.append(MNPuzzle(tuple(x), self.to_grid))  # to right
                return result
            # first place, change it to right
            elif index == self.m-1:
                x = new_start_grid.copy()
                to_left(x, row_number, index)
                result.append(MNPuzzle(tuple(x), self.to_grid))  # to left
                return result
            # change it to left
            else:
                x = new_start_grid.copy()
                to_left(x, row_number, index)
                result.append(MNPuzzle(tuple(x), self.to_grid))  # to left

                x = new_start_grid.copy()
                to_right(x, row_number, index)
                result.append(MNPuzzle(tuple(x), self.to_grid))  # to right
                return result
            # can change it to both left and right
        elif row_number == self.n-1:
            x = new_start_grid.copy()
            to_upper(x, row_number, index)
            result.append(MNPuzzle(tuple(x), self.to_grid))  # to upper
            # '*' locate in the last row
            if index == 0:
                x = new_start_grid.copy()
                to_right(x, row_number, index)
                result.append(MNPuzzle(tuple(x), self.to_grid))  # to right
                return result
            # can change it to right
            elif index == self.m-1:
                x = new_start_grid.copy()
                to_left(x, row_number, index)
                result.append(MNPuzzle(tuple(x), self.to_grid))  # to left
                return result
            # can change it to left
            else:
                x = new_start_grid.copy()
                to_left(x, row_number, index)
                result.append(MNPuzzle(tuple(x), self.to_grid))  # to left

                x = new_start_grid.copy()
                to_right(x, row_number, index)
                result.append(MNPuzzle(tuple(x), self.to_grid))  # to right
                return result
            # can change it to left and right
        else:
            x = new_start_grid.copy()
            to_upper(x, row_number, index)
            result.append(x)  # to upper
            x = new_start_grid.copy()
            to_below(x, row_number, index)
            result.append(x)  # to below
            if index == 0:
                x = new_start_grid.copy()
                to_right(x, row_number, index)
                result.append(MNPuzzle(tuple(x), self.to_grid))  # to right
                return result
            elif index == self.m-1:
                x = new_start_grid.copy()
                to_left(x, row_number, index)
                result.append(MNPuzzle(tuple(x), self.to_grid))  # to left
                return result
            else:
                x = new_start_grid.copy()
                to_left(x, row_number, index)
                result.append(MNPuzzle(tuple(x), self.to_grid))  # to left

                x = new_start_grid.copy()
                to_right(x, row_number, index)
                result.append(MNPuzzle(tuple(x), self.to_grid))  # to right
                return result

    # override is_solved
    # a configuration is solved when from_grid is the same as to_grid
    def is_solved(self):
        """
        Return whether MNPuzzle self is solved.
        @type self: MNPuzzle
        @rtype: bool
        >>> target_grid = (("1", "2", "3"), ("4", "5", "*"))
        >>> start_grid = (("1", "2", "3"), ("4", "5", "*"))
        >>> x = MNPuzzle(start_grid,target_grid)
        >>> x.is_solved()
        True
        """
        return self.from_grid == self.to_grid

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    target_grid = (("1", "2", "3"), ("4", "5", "*"))
    start_grid = (("*", "2", "3"), ("1", "4", "5"))
    from puzzle_tools import breadth_first_solve, depth_first_solve
    from time import time
    start = time()
    solution = breadth_first_solve(MNPuzzle(start_grid, target_grid))
    end = time()
    print("BFS solved: \n\n{} \n\nin {} seconds".format(
        solution, end - start))
    start = time()
    solution = depth_first_solve((MNPuzzle(start_grid, target_grid)))
    end = time()
    print("DFS solved: \n\n{} \n\nin {} seconds".format(
        solution, end - start))
