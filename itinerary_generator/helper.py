def itinerary_from_number(k, base_itienary, mode2="airborne"):
    """
    Helper function to generate a test itinerary from the provided number k.
    The logic behind it is to convert the given number into binary and modify 
    the base_itienary such that the mode2 text is placed in place of digit "1".

    Args:
    - k (int): sequence number for testing.
    - base_itinerary (list): list of base itinerary.
    - mode2 (str): mode of sencond transport, by default it is airborne.

    Returns:
    - list: list of generated itinerary.
    """

    itinerary = base_itienary.copy()
    x = bin(k)[2:]
    for i in range(len(x)):
        if x[-i-1] == "1":
            itinerary[-i-1] = mode2
    return itinerary

def check_can_satisfy(d1, d2):
    """
    Helper function to check if a test itinerary satisfies with one of costumer
    preferences.

    Args:
    - d1 (dict): dict of costumer preference.
    - d2 (dict): dict of test itinerary.

    Returns:
    - bool: True if it satisfies the costumer preference.
    """

    for element in d1.items():
        if element in d2.items():
            return True 
    return False