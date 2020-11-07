#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    route = [None] * length

    cache = {}

    for ticket in tickets:
        starting = ticket.source
        arriving = ticket.destination

        cache[starting] = arriving
    next = cache['NONE']

    for curr in range(0, length):
        route[curr] = next
        next = cache[next]

    return route
