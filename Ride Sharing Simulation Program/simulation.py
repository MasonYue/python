from rider import Rider
from driver import Driver
from container import PriorityQueue
from dispatcher import Dispatcher
from event import Event, RiderRequest, DriverRequest, create_event_list
from monitor import Monitor
from location import Location

class Simulation:
    """A simulation.

    This is the class which is responsible for setting up and running a
    simulation.

    The API is given to you: your main task is to implement the run
    method below according to its docstring.

    Of course, you may add whatever private attributes and methods you want.
    But because you should not change the interface, you may not add any public
    attributes or methods.

    This is the entry point into your program, and in particular is used for
    auto-testing purposes. This makes it ESSENTIAL that you do not change the
    interface in any way!
    """

    # === Private Attributes ===
    # @type _events: PriorityQueue[Event]
    #     A sequence of events arranged in priority determined by the event
    #     sorting order.
    # @type _dispatcher: Dispatcher
    #     The dispatcher associated with the simulation.

    def __init__(self):
        """Initialize a Simulation.

        @type self: Simulation
        @rtype: None
        """
        self._events = PriorityQueue()
        self._dispatcher = Dispatcher()
        self._monitor = Monitor()

    def run(self, initial_events):
        """Run the simulation on the list of events in <initial_events>.

        Return a dictionary containing statistics of the simulation,
        according to the specifications in the assignment handout.

        @type self: Simulation
        @type initial_events: list[Event]
            An initial list of events.
        @rtype: dict[str, object]

        """
        # Add all initial events to the event queue
        for event in initial_events:
            self._events.add(event)

        # Until there are no more events, remove an event
        while not self._events.is_empty():
            new_event = self._events.remove()

            result_event = new_event.do(self._dispatcher, self._monitor)

            # from the event queue and do it. Add any returned
            # events to the event queue.
            for event in result_event:
                self._events.add(event)

        return self._monitor.report()




        # Add all initial events to the event queue.

        # Until there are no more events, remove an event
        # from the event queue and do it. Add any returned
        # events to the event queue.





