"""
Solutions the for problems of day 5 of Advent of Code
------------------------
Tristan Barber
"""

main_data = "Day_5_Problems/data/input.txt"

#Create 2d list for the graph and start 0,0 in top left 10000 each direction
def create_graph(size):
    graph = [["." for _ in range(size)] for _ in range(size)]
    return graph

def arrow_parser(filename):
    coordinated = []
    with open(filename) as file:
        for line in file:
            line.strip()
            line = line.split(" -> ")
            line[1].replace('\n', "")
            print(line)

def main():
    graph = create_graph(20)
    arrow_parser(main_data)

if __name__ == "__main__":
    main()