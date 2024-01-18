# Itinerary-generator
Itinerary Generator for coding test. The problem details can be found in [this pdf file](Technical%20Interview%20Problem.pdf).

## Project Tree

    Itinerary-generator/
    |--itinerary_generator/
        |--__init__.py
        |--helper.py
        |--itinerary_generator.py
    |--.gitignore
    |--README.md
    |--Technical Interview Problem.pdf
    |--input.txt
    |--LICENSE
    |--main.py
    |--requirement.py
    |--test.py

## Running the project

### Requirements:

- python3.x

This project was tested in Windows 11 machine and with ```python3.10```.

The project accepts input from both the file and stdin.

### Using input file:

Inside the root directory, type the following command in the terminal:

```
cd <project_root_dir>
python3 main.py <input_file>
```

- Input file structure
    
    Save the input in a text file, for e.g. [input.txt](input.txt). The structure of the file should be as follows:

    - First line: integer 𝐻, the number of island hops
    - Second line: integer 𝐶, the number of customers
    - Consecutive lines: one line per customer

        - Each line has a list of pairs ℎ 𝑡, where ℎ is the number of the island hop, and 𝑡 is the specified means of transport for that hop: either airborne or by sea
        - Each pair will occur at most once for a single customer
        - Each customer wants to specify at least one hop
        - Each customer wants airborne transport on at most one hop
        - The ℎ and the 𝑡 are separated by a single space, the pairs are separated by a comma and a space (,)

    The input does not contain special characters or malicious tricks.

### Using stdin:

Inside the root directory, type the following command in the terminal:

```
cd <project_root_dir>
python3 main.py
```
Then, provide the input in the terminal as the same structure as above. For e.g.: 
```
PS E:\Coding test\Itinerary-generator> python3 main.py
2
3
0 by-sea
0 airborne
1 by-sea
```

## Output

The output is either an itinerary as below:
```
PS E:\Coding test\Itinerary-generator> python3 main.py input.txt
0 by-sea, 1 by-sea, 2 airborne, 3 by-sea, 4 by-sea, 5 by-sea
```
or no itinerary:
```
PS E:\Coding test\Itinerary-generator> python3 main.py input.txt
NO ITINERARY
```

## Test

For unit-test and End-to-End test, run:
```
cd <project_root_dir>
python3  -m unittest test.py
```
