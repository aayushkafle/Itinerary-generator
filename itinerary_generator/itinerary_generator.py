from itinerary_generator.helper import *

class ItineraryGenerator:
    def __init__(self, H, C, prefs):
        """
        Initialize the ItineraryGenerator object.

        Args:
        - H (int): No of islands hops during the trip.
        - C (int): No of costumers for the trip.
        - prefs (list): list of dicts {hop_number: transport_type} representing costumer preference
        """ 
        self.H = H
        self.C = C
        self.prefs = prefs

    def generate_itinerary(self):
        """
        Generate itinerary satisfying the required conditions.

        Returns:
        - dict: {hop_number: transport_type} for itinenary.
        or 
        - None: if no solutions are possible.
        """

        # check if there exists more than one airborne for each costumer
        more_than_one_airborne = self.has_multiple_airborne()
        if more_than_one_airborne:
            return None

        # all travel by-sea
        base_itienary = ["by-sea" for i in range(self.H)]

        # iterate through each one of available 2^H options
        for k in range(2**self.H):
            can_satisfy = True
            # create test itienary to check if it satisfies each user preference
            test_itinerary = dict(zip(list(range(self.H)), itinerary_from_number(k, base_itienary)))
            # iterate though each user
            for pref in self.prefs:
                can_satisfy = check_can_satisfy(pref, test_itinerary)
                # if can't satisfy any one user preference, move to next option
                if not can_satisfy:
                    break
            if can_satisfy:
                return test_itinerary

        # if no solution satisfies then return None
        return None
    
    def has_multiple_airborne(self):
        """
        Check if there are multiple airborne entries for a costumer.

        Returns:
        - bool: True if multiple entries exist.
        """
        for pref in self.prefs:
            v  = list(pref.values())
            if v.count("airborne") > 1:
                return True
        return False

    