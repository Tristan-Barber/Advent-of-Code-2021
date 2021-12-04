"""
Solutions the for problems of day 1 of Advent of Code
------------------------
Tristan Barber
"""

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
        return [int(i.strip()) for i in file.readlines()]

def sum_comp(filename):
    increased_count = 0
    sums = []
    total = 0
    depths = easy_iterable(filename)
    i = 0
    back = None
    back_flag = False
    while i != len(depths):
        current = i
        if i-1 < 0:
            prev = i-1
        print(depths[current], depths[prev])
        if increased_count == 3:
            i-=1
            sums.append(total)
            total = 0

        if back_flag == True:
            back_flag = False
            i = back

        if depths[current] > depths[prev] and ((i-1 < 0) == False):
            total += depths[current]
            increased_count += 1
        elif depths[current] > 0 and ((i-1 < 0) == True):
            total += depths[current]
            increased_count += 1
        else:
            total += depths[current]
            back = current
            back_flag = True
            increased_count += 1
    return sums

def main():
    print(prev_measurement_num("day_1_problems/data/depths.txt"))
    print(prev_measurement_num("day_1_problems/data/test_1.txt"))
    #Infinite loop Below:
    #print(sum_comp("day_1_problems/data/test_1.txt"))

if __name__ == "__main__":
    main()