class Location:
    def __init__(self, row, column):
        """Initialize a location.

        @type self: Location
        @type row: int
        @type column: int
        @rtype: None
        """
        self.row = row
        self.column = column

    def __str__(self):
        """Return a string representation.

        @rtype: str
        >>> a=Location(2,3)
        >>> print (a)
        2,3
        """
        return "{},{}".format(self.row, self.column)

    def __eq__(self, other):
        """Return True if self equals other, and false otherwise.

        @rtype: bool
        >>> a=Location (2,3)
        >>> b=Location (2,4)
        >>> a==b
        False
        """
        return (self.row ==other.row and
                self.column == other.column and
                type(self) == type(other))


    def manhattan_distance(origin, destination):
        """Return the Manhattan distance between the origin and the destination.

        @type origin: Location
        @type destination: Location
        @rtype: int
       >>> a=Location(2,3)
       >>> b=Location(2,4)
       >>> Location.manhattan_distance(a,b)
       1
       """
        return abs(origin.row - destination.row) + abs(origin.column -
                                                       destination.column)

    def deserialize_location(location_str):
        """Deserialize a location.

        @type location_str: str
        A location in the format 'row,col'
        @rtype: Location
        >>> a='2,3'
        >>> deserialize_location(a)
        2,3
        """
        x = location_str.find(',')
        return Location(int(location_str[: x]), int(location_str[x+1:]))




