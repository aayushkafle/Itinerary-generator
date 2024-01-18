import sys

from itinerary_generator.itinerary_generator import ItineraryGenerator

def parse_input(lines):
    """
    Parse customer input lines and return a list of customer preferences.
    Each preference is represented as a tuple (hop_number, transport_type).

    Args:
    - lines (list): list of strings which contain each line of costumer input.

    Returns:
    - list: list of dicts (hop_number: transport_type) representing costumer preference
    """

    preferences = []
    for line in lines:
        preference = {}
        for pair in line.strip().split(','):                # strip and split based on ","
            k, v = pair.split()
            preference[int(k)] = v                      
        preferences.append(preference)                      # add elements to dict
    return preferences

def print_results(itinenary):
    """
    Prints the final result.

    Args:
    - itinerary (dict): {hop_number: transport_type} for itinerary.
    """
    if itinenary:                                           # check if itinerary was created
        for i in itinenary:
            if i != 0:                                      # don't print comma on first item
                print(", ", end="")
            print("%d %s" % (i, itinenary[i]), end="")      # print the results
    else:
        print("NO ITINERARY")                               # print when no results are possible
        

def main(input_file=None):
    # Read input either from file
    if input_file:
        try:
            with open(input_file, 'r') as file:
                input_lines = file.readlines()
                H = int(input_lines[0].strip())                 # Number of island hops
                C = int(input_lines[1].strip())                 # Number of customers
                if C > 250:                                     # No of costumers exceeds 250
                    print("NO ITINERARY")
                    sys.exit(1)
                preferences = parse_input(input_lines[2:])      # parse input
        except FileNotFoundError as e:
            print("Error: %s doesn't exist, please input a valid file." % input_file)
            sys.exit(1)
        except Exception as e:
            print("Error: reading from file: %s." % e)
            sys.exit(1)

    else:                                                   # Input using stdin
        H = int(input())                                    # Number of island hops
        C = int(input())                                    # Number of costumers
        if C > 250:
            print("NO ITINERARY\n")                           # No of costumers exceeds 250
            sys.exit(1)
        input_lines = []
        input_lines.extend([input() for i in range(C)])
        preferences = parse_input(input_lines)              # Parse input

    # itinerary generator object
    itinerary_generator_obj = ItineraryGenerator(H, C, preferences)
    itinerary = itinerary_generator_obj.generate_itinerary()

    print_results(itinerary)
    sys.exit(0)

if __name__=="__main__":
    if len(sys.argv) > 2:
        print("Usage: python main.py [input.py]")
        sys.exit(1)

    input_file = sys.argv[1] if len(sys.argv) == 2 else None
    main(input_file)