"""
Solutions the for problems of day 1 of Advent of Code
------------------------
Tristan Barber
"""

def prev_measurement_num(filename):
    increased_count = 0
    with open(filename) as file:
        for depth in file:
            try:
                previous_depth = current_depth
            except UnboundLocalError:
                previous_depth = 0
            current_depth = int(depth)
            if current_depth > previous_depth:
                increased_count += 1
        return increased_count -1

def main():
    print(prev_measurement_num("day_1_problems/data/depths.txt"))
    print(prev_measurement_num("day_1_problems/data/test_1.txt"))

if __name__ == "__main__":
    main()