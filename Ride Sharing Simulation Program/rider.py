from location import Location
"""
The rider module contains the Rider class. It also contains
constants that represent the status of the rider.

=== Constants ===
@type WAITING: str
    A constant used for the waiting rider status.
@type CANCELLED: str
    A constant used for the cancelled rider status.
@type SATISFIED: str
    A constant used for the satisfied rider status
"""

WAITING = "waiting"
CANCELLED = "cancelled"
SATISFIED = "satisfied"


class Rider:
    """A rider has a unique identier, an origin, a destination and a status."""


    def __init__(self, identifier, origin, destination, patience):
        """
        Initialize a new rider

        @type self: Rider
        @type id: str
        @type origin: Location
        @type destination: Location
        @type status: String
        @type patience: int
        @rtype: None
        """
        self.id = identifier
        self.origin = origin
        self.destination = destination
        self.status = None
        self.patience = patience

    def __str__(self):
        """Return a string representation.

        @type self: Rider
        @rtype: str

        >>> a= Rider("Mike",Location(1,2),Location(3,4),10)
        >>> print(a)
        Rider: Mike 1,2 3,4 10

        """

        return "Rider: {} {} {} {}".format(self.id,self.origin,self.destination,
                                    self.patience)



