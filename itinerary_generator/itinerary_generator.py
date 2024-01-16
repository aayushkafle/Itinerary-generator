import itertools

class ItineraryGenerator:
    def __init__(self, island_hops, costumers, preferences):
        """
        Initialize the ItineraryGenerator object.

        Args:
        - island_hops (int): No of islands hops during the trip.
        - costumers (int): No of costumers for the trip.
        - preference (list): list of tuples (hop_number, transport_type) representing costumer preference
        """ 
        print(island_hops, costumers, preferences)
        self.island_hops = island_hops
        self.costumers = costumers
        self.preferences = preferences

    def generate_itinerary(self):
        """
        Generate itinerary satisfying the required conditions.

        Returns:
        - bool: True if the itinerary was possible to generate, false if not.
        - list: List of travel medium for itinenary.
        """

        return false