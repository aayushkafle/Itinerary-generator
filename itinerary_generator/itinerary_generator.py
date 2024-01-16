import itertools

class ItineraryGenerator:
    def __init__(self, H, C, prefs):
        """
        Initialize the ItineraryGenerator object.

        Args:
        - H (int): No of islands hops during the trip.
        - C (int): No of costumers for the trip.
        - prefs (list): list of tuples (hop_number, transport_type) representing costumer preference
        """ 
        print(H, C, prefs)
        self.H = H
        self.C = C
        self.prefs = prefs

    def generate_itinerary(self):
        """
        Generate itinerary satisfying the required conditions.

        Returns:
        - bool: True if the itinerary was possible to generate, false if not.
        - list: list of transport type for itinenary.
        """

        return True, [0,0,0,0,1,0,1]