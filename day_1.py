"""
First solution for problem 1 of day 1 of Advent of Code
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

"""
When it reaches a decreased number, it goes back to the decreased and starts the letters over
199  A      
200  A B    
208  A B C  
210    B C D
200  E   C D
207  E F   D
240  E F G  
269    F G H
260      G H
263        H

A: 607 (N/A - no previous sum)
B: 618 (increased)
C: 618 (no change)
D: 617 (decreased)
E: 647 (increased)
F: 716 (increased)
G: 769 (increased)
H: 792 (increased)
"""

def easy_iterable(filename):
    depths = []
    with open(filename) as file:
        for depth in file:
            depths.append(depth)
        return depths

def sum_comp(filename):
    increased_count = 0
    sums = []
    total = 0
    depths = easy_iterable(filename)
    
       
def main():
    # print(prev_measurement_num("data/depths.txt"))
    # print(prev_measurement_num("data/test_1.txt"))
    print(sum_comp("data/test_1.txt"))

if __name__ == "__main__":
    main()