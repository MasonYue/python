from location import Location
from rider import Rider


class Driver:
    """A driver for a ride-sharing service.

    === Attributes ===
    @type id: str
        A unique identifier for the driver.
    @type location: Location
        The current location of the driver.
    @type is_idle: bool
        A property that is True if the driver is idle and False otherwise.
    """

    def __init__(self, identifier, location, speed):
        """Initialize a Driver.

        @type self: Driver
        @type identifier: str
        @type location: Location
        @type speed: int
        @rtype: None
         The default status of Driver is idle
        # The default destination of Driver is None
        """
        self.id = identifier
        self.location = location
        self.speed = speed
        self.destination = None
        self.is_idle = True

    def __str__(self):
        """Return a string representation.

        @type self: Driver
        @rtype: str
        >>> a=Driver("Mike",Location(1,2),10)
        >>> print(a)
        Driver: Mike 1,2 10
        """

        return "Driver: {} {} {}".format(self.id, self.location, self.speed)

    def __eq__(self, other):
        """Return True if self equals other, and false otherwise.

        @type self: Driver
        @rtype: bool
        >>> a=Driver("Mike", Location(2,3),10)
        >>> b=Driver("Mike",Location(2,3),10)
        >>> a==b
        True
        """
        return (type(self) == type(other) and
                self.id == other.id and
                self.location == other.location and
                self.speed == other.speed)

    def get_travel_time(self, destination):
        """Return the time it will take to arrive at the destination,
        rounded to the nearest integer.

        @type self: Driver
        @type destination: Location
        @rtype: int
         >>> a=Driver("Mike", Location(1,2),10)
        >>> a.get_travel_time(Location(11,2))
        1

        """
        self.destination = destination
        return int(round(Location.manhattan_distance(self.location,
                                                     destination))/self.speed)

    def start_drive(self, location):
        """Start driving to the location and return the time the drive will take.

        @type self: Driver
        @type location: Location
        @rtype: int
        >>> a=Driver("Mike", Location(1,2),10)
        >>> a.start_drive(Location(11,2))
        1

        """
        self.destination = location
        return int(round(Location.manhattan_distance(self.location, location))/self.speed)

    def end_drive(self):
        """End the drive and arrive at the destination.

        Precondition: self.destination is not None.

        @type self: Driver
        @rtype: None
        """
        self.location = self.destination
        self.destination = None
        self.is_idle = True

    def start_ride(self, rider):
        """Start a ride and return the time the ride will take.

        @type self: Driver
        @type rider: Rider
        @rtype: int

        >>> a=Driver("Mike", Location(1,2),10)
        >>> a.start_ride(Rider("Mike",Location(1,2),Location(11,2),10))
        1
        """
        self.is_idle = False
        self.location = rider.origin
        self.destination = rider.destination
        return int(round(Location.manhattan_distance
                         (rider.origin, rider.destination))/self.speed)

    def end_ride(self):
        """End the current ride, and arrive at the rider's destination.

        Precondition: The driver has a rider.
        Precondition: self.destination is not None.

        @type self: Driver
        @rtype: None
        """
        self.is_idle = True
        self.destination = None


if __name__ == "__main__":
    import doctest
    doctest.testmod()
