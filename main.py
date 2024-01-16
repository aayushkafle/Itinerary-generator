import sys
from itinerary_generator.itinerary_generator import ItineraryGenerator

transport_type_dict = {"by-sea": 0, "airborne": 1}

def transport_type_to_int(pref):
    """
    Convert transport type string to int.

    Args:
    - pref (str): string with hop index and transport mode separated by space

    Returns:
    - tuple: (h, t) such that h is the hop index and t is mode where 0 is by-sea and 1 is airborne
    """
    
    pair = pref.split(" ")
    return (int(pair[0]), int(transport_type_dict[pair[1]]))

def parse_input(lines):
    """
    Parse customer input lines and return a list of customer preferences.
    Each preference is represented as a tuple (hop_number, transport_type).

    Args:
    - lines (list): list of strings which contain each line of costumer input.

    Returns:
    - list: list of tuples (hop_number, transport_type) representing costumer preference
            where the by-sea is indexed 0 whereas airborne is indexed as 1
    """

    preferences = []
    for line in lines:
        preference = [transport_type_to_int(pair) for pair in line.strip().split(', ')]
        preferences.append(preference)
    return preferences

def print_results(itinenary):
    """
    Prints the final result.

    Args:
    - itinerary (list): list of tranport type for itinerary
    """
    
    for i in range(len(itinenary)):
        tranport_id = itinenary[i]
        transport_type = list(transport_type_dict.keys())[list(transport_type_dict.values()).index(tranport_id)]
        if i != 0:
            print(", ")
        print("%d %s" % (i, transport_type))
    print("\n")
        

def main(input_file=None):
    # Read input either from file or stdin

    if input_file:
        with open(input_file, 'r') as file:
            input_lines = file.readlines()
            H = int(input_lines[0].strip())                 # Number of island hops
            C = int(input_lines[1].strip())                 # Number of customers
            if C > 250:                                     # No of costumers exceeds 250
                print("NO ITINERARY")
                sys.exit(1)
            preferences = parse_input(input_lines[2:])      # parse input
            
    else:                                                   # Input using stdin
        H = int(input())                                    # Number of island hops
        C = int(input())                                    # Number of costumers
        if C > 250:
            print("NO ITINERARY")                           # No of costumers exceeds 250
            sys.exit(1)
        input_lines = []
        input_lines.extend([input() for i in range(C)])
        preferences = parse_input(input_lines)              # Parse input

    # itinerary generator object
    itinerary_generator_obj = ItineraryGenerator(H, C, preferences)
    ret, itinerary = itinerary_generator_obj.generate_itinerary()

    if ret:
        print_results(itinenary)
    else:
        print("NO ITINERARY")

if __name__=="__main__":
    if len(sys.argv) > 2:
        print("Usage: python main.py [input.py]")
        sys.exit(1)

    input_file = sys.argv[1] if len(sys.argv) == 2 else None
    main(input_file)