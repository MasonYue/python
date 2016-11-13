"""
Some functions for working with puzzles
"""
from puzzle import Puzzle
from collections import deque
# set higher recursion limit
# which is needed in PuzzleNode.__str__
# uncomment the next two lines on a unix platform, say CDF
# import resource
# resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
import sys
sys.setrecursionlimit(10**6)

# implement depth_first_solve
# do NOT change the type contract
# you are welcome to create any helper functions
# you like


def depth_first_solve(puzzle):
    """
    Return a path from PuzzleNode(puzzle) to a PuzzleNode containing
    a solution, with each child containing an extension of the puzzle
    in its parent.  Return None if this is not possible.

    @type puzzle: Puzzle
    @rtype: PuzzleNode
    """

    root_node = PuzzleNode(puzzle)
    # first node in loop
    if root_node.puzzle.is_solved():
        return root_node
    # if this is solved, then return this one
    elif root_node.puzzle.fail_fast():
        return None
    # if fail fast, means can't do it and return None
    else:
        unused = [root_node]
        return find_path(dfs([], unused))
        # else use DFS to find a solution and return path


# result.append(GridPegSolitairePuzzle(new_marker, self._marker_set))
# implement breadth_first_solve
# do NOT change the type contract
# you are welcome to create any helper functions
# you like
# Hint: you may find a queue useful, that's why
# we imported deque


def breadth_first_solve(puzzle):
    """
    Return a path from PuzzleNode(puzzle) to a PuzzleNode containing
    a solution, with each child PuzzleNode containing an extension
    of the puzzle in its parent.  Return None if this is not possible.

    @type puzzle: Puzzle
    @rtype: PuzzleNode
    """
    root_node = PuzzleNode(puzzle)
    # first node in loop
    if root_node.puzzle.is_solved():
        return root_node
    # if this is solved, then return this one
    elif root_node.puzzle.fail_fast():
        return None
    # if fail fast, means can't do it and return None
    else:
        unused = [root_node]
        return find_path(bfs([], unused))
        # else use BFS to find a solution and return path


def find_path(node):
    """
    find the first node from child node

    @type node: PuzzleNode
    @rtype: PuzzleNode

    """
    current = node
    # set node as current node
    while current.parent is not None and current.puzzle is not None:
        # loop as parent is not none and puzzle is not None
        current.parent.children = [current]
        current = current.parent
        # use node fo define its parent node
    return current


def bfs(used_list, unused_list):
    """
    using BFS to find a solution PuzzleNode

    @type used_list:list
    @type unused_list: list
    @rtype: PuzzleNode
    """
    if not unused_list:
        return None
    # if used_list is empty, then can't find a solution, return None
    if unused_list[0].puzzle.is_solved():
        return unused_list[0]
    # if the bottom unused list is solution, then return it
    else:
        for extension in unused_list[0].puzzle.extensions():
            unused = True
            for obj in unused_list:
                if extension == obj.puzzle:
                    unused = False
            if extension not in used_list and unused:
                # for all extensions, first find if they are used before, if not
                # used, change it to a PuzzleNode and append it to unused_list
                unused_list.append(PuzzleNode(extension, parent=unused_list[0]))
    return bfs(used_list + [unused_list[0].puzzle], unused_list[1:])
    # put bottom unused puzzle to used list and test the next bottom one.
    # this method test PuzzleNode from the most bottom, so it will fnd all
    # extensions first and then find extensions' extension. This is a BFS


def dfs(used_list, unused_list):
    """
    @type used_list:list
    @type unused_list: list
    @rtype: PuzzleNode
    """
    if not unused_list:
        return None
    # if used_list is empty, then can't find a solution, return None
    if unused_list[len(unused_list)-1].puzzle.is_solved():
        return unused_list[len(unused_list)-1]
    # if the topmost unused list is a solution, then return it
    else:
        outer = unused_list.pop()
        # outer is the topmost unused list, unused list will delete this one
        for extension in outer.puzzle.extensions():
            unused = True
            for obj in unused_list:
                if obj.puzzle == extension:
                    unused = False

            if extension == outer.puzzle:
                unused = False
            if extension not in used_list and unused:
                # for all extensions, first find if they are used before, if not
                # used, change it to a PuzzleNode and append it to unused_list
                unused_list.append(PuzzleNode(extension, parent=outer))
    return dfs(used_list + [outer.puzzle], unused_list[:])
    # put topmost unused puzzle to used list and test the next topmost one.
    # this method test PuzzleNode from the topmost, so it will fnd one
    # extension first and then find this extensions' extension. This is a DFS


# Class PuzzleNode helps build trees of PuzzleNodes that have
# an arbitrary number of children, and a parent.


class PuzzleNode:
    """
    A Puzzle configuration that refers to other configurations that it
    can be extended to.
    """

    def __init__(self, puzzle=None, children=None, parent=None):
        """
        Create a new puzzle node self with configuration puzzle.

        @type self: PuzzleNode
        @type puzzle: Puzzle | None
        @type children: list[PuzzleNode]
        @type parent: PuzzleNode | None
        @rtype: None
        """
        self.puzzle, self.parent = puzzle, parent
        if children is None:
            self.children = []
        else:
            self.children = children[:]

    def __eq__(self, other):
        """
        Return whether PuzzleNode self is equivalent to other

        @type self: PuzzleNode
        @type other: PuzzleNode | Any
        @rtype: bool

        >>> from word_ladder_puzzle import WordLadderPuzzle
        >>> pn1 = PuzzleNode(WordLadderPuzzle("on", "no", {"on", "no", "oo"}))
        >>> pn2 = PuzzleNode(WordLadderPuzzle("on", "no", {"on", "oo", "no"}))
        >>> pn3 = PuzzleNode(WordLadderPuzzle("no", "on", {"on", "no", "oo"}))
        >>> pn1.__eq__(pn2)
        True
        >>> pn1.__eq__(pn3)
        False
        """
        return (type(self) == type(other) and
                self.puzzle == other.puzzle and
                all([x in self.children for x in other.children]) and
                all([x in other.children for x in self.children]))

    def __str__(self):
        """
        Return a human-readable string representing PuzzleNode self.

        # doctest not feasible.
        """
        return "{}\n\n{}".format(self.puzzle,
                                 "\n".join([str(x) for x in self.children]))
