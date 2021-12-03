"""
First solution for problem 1 of day 1 of Advent of Code
------------------------
Tristan Barber
"""

def prev_measurement_num(filename):
    increased_count = 0
    with open(filename) as file:
        count = 0
        for depth in file:
            count += 1
            try:
                previous_depth = current_depth
            except UnboundLocalError:
                previous_depth = 0
            current_depth = int(depth)
            if current_depth > previous_depth:
                increased_count += 1
        return increased_count
       
def main():
    print(prev_measurement_num("data/depths.txt"))
    print(prev_measurement_num("data/test.txt"))

if __name__ == "__main__":
    main()