from location import Location
from driver import Driver
from rider import Rider,WAITING, CANCELLED, SATISFIED


class Dispatcher:
    """
    A dispatcher fulfills requests from riders and drivers for a
    ride-sharing service.

    When a rider requests a driver, the dispatcher assigns a driver to the
    rider. If no driver is available, the rider is placed on a waiting
    list for the next available driver. A rider that has not yet been
    picked up by a driver may cancel their request.

    When a driver requests a rider, the dispatcher assigns a rider from
    the waiting list to the driver. If there is no rider on the waiting list
    the dispatcher does nothing. Once a driver requests a rider, the driver
    is registered with the dispatcher, and will be used to fulfill future
    rider requests.
    """

    def __init__(self):
        """Initialize a Dispatcher.

        @type self: Dispatcher
        @rtype: None
        """
        self.rider = []
        self.driver = []
        self.available_driver = []

    def __str__(self):
        """Return a string representation.

        @type self: Dispatcher
        @rtype: str
        """
        return "rider{}, available_driver{}".format(self.rider,
                                                    self.available_driver)

    def request_driver(self, rider):

        """Return a driver for the rider, or None if no driver is available.

        Add the rider to the waiting list if there is no available driver.

        @type self: Dispatcher
        @type rider: Rider
        @rtype: Driver | None
        >>> a=Dispatcher()
        >>> a.available_driver.append(Driver("Mike", Location(1,2),10))
        >>> rider=Rider("Alice",Location(1,2),Location(3,4),10)
        >>> print(a.request_driver(rider))
        Driver: Mike 1,2 10
        """
        i = 0
        driver_num = 0
        if len(self.available_driver) == 0:
            self.rider.append(rider)
            rider.status = WAITING
            return None
        #if no driver,then put this rider on the list
        else:
            time = self.available_driver[i].start_drive(rider.origin)
            while i+1 < len(self.available_driver):
                i += 1
                if time > self.available_driver[i].start_drive(rider.origin):
                    driver_num = i
                    #choose the driver who can arrive quickest
            rider.status = WAITING
            return self.available_driver[driver_num]
        #return a most fast driver

    def request_rider(self, driver):

        """Return a rider for the driver, or None if no rider is available.

        If this is a new driver, register the driver for future rider requests.

        @type self: Dispatcher
        @type driver: Driver
        @rtype: Rider | None
        >>> driver=Driver("Mike", Location(1,2),10)
        >>> a=Dispatcher()
        >>> a.rider.append(Rider("Mike",Location(1,2),Location(3,4),10))
        >>> print(a.request_rider(driver))
        Rider: Mike 1,2 3,4 10

        """
        self.available_driver.append(driver)
        if driver not in self.driver:
            self.driver.append(driver)
            #if it's a new driver, then register him/her on driver's list
        else:
            pass

        if len(self.rider) > 0:
            return self.rider[0]
        #if there is a rider, then return this rider
        else:
            pass

    def cancel_ride(self, rider):
        """Cancel the ride for rider.

        @type self: Dispatcher
        @type rider: Rider
        @rtype: None
        """
        #the rider cancel this ride
        rider.status = CANCELLED
        self.rider.remove(rider)











