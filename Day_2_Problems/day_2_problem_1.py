"""
Solutions the for problems of day 2 of Advent of Code
------------------------
Tristan Barber
"""

#Functions:
def coordinates(filename):
    horizontal_position = 0     #x
    depth = 0                   #y
    with open(filename) as file:
        for line in file:
            command = line[:-2].strip()
            if line[-2].strip() != "":
                movement = int(line[-2].strip())
            else:
                movement = 2
            if command == "forward":
                horizontal_position += movement
            elif command == "down":
                depth += movement
            elif command == "up":
                depth -= movement
        print("x:", horizontal_position, "y:", depth)
        return horizontal_position, depth

def main():
    x, y = coordinates("day_2_problems/data/day_2_input.txt")
    #x, y = coordinates("day_2_problems/data/test_1.txt")
    print(x*y)

if __name__ == "__main__":
    main()