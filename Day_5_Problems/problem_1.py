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
    coordinates = []
    with open(filename) as file:
        for line in file:
            line.strip()
            line = line.split(" -> ")
            line[1] = line[1].replace('\n', "")
            line[0] = line[0].split(",")
            line[1] = line[1].split(",")
            coordinates.append(line)
        return coordinates

def plot_points(graph, coordinates):
    sum = 0
    for group in coordinates:
        for pair in group:
            for coordinate in pair:
                print(coordinate)
    return sum

def main():
    graph = create_graph(1000)
    coordinates = arrow_parser(main_data)
    print(plot_points(graph, coordinates))

if __name__ == "__main__":
    main()