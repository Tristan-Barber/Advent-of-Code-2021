from day_3_problem_1 import *

def generator(filename):
    binaries = easy_iterable(filename)
    place = 0
    for place in range(12):
        zero = 0
        one = 0
        position = 0
        for line in binaries:
            if line[place] == "0":
                zero += 1
            elif line[place] == "1":
                one += 1
        for binary in binaries:
            if zero > one:
                if binary[place] == "1":
                    binaries.pop(position)
            elif one > zero:
                if binary[place] == "0":
                    binaries.pop(position)
            position+=1
    return binaries

def scrubber(filename):
    pass

def main():
    print(generator("Day_3_Problems/data/day_3_input.txt"))

if __name__ == "__main__":
    main()