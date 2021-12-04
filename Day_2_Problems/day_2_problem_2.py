"""
Solutions the for problems of day 2 of Advent of Code
------------------------
Tristan Barber
"""

#Functions:
def coordinates(filename):
    horizontal_position = 0     #x
    depth = 0                   #y
    aim = 0                     #degrees (but in weird)
    with open(filename) as file:
        for line in file:
            command = line[:-2].strip()
            if line[-2].strip() != "":
                movement = int(line[-2].strip())
            else:
                movement = 2 #Some weird file thing
            if command == "forward":
                horizontal_position += movement
                depth += aim*movement
            elif command == "down":
                aim += movement
            elif command == "up":
                aim -= movement
        print("x:", horizontal_position, "y:", depth, "Aim:", aim)
        return horizontal_position, depth

def main():
    x, y = coordinates("day_2_problems/data/day_2_input.txt")
    #x, y = coordinates("day_2_problems/data/test_1.txt")
    print(x*y)

if __name__ == "__main__":
    main()