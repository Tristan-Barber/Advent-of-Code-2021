from day_3_problem_1 import *

def generator(filename):
    binaries = easy_iterable(filename)
    for place in range(len(binaries[0])):
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
                else:
                    position += 1
            elif one > zero:
                print(binary[place])
                if binary[place] == "0":
                    print(binary)
                    print("Place:", place)
                    print(binary[place])
                    print("position:",position)
                    print(binaries[position])
                    binaries.pop(position) 
                position +=1
    return binaries

def scrubber(filename):
    pass

def main():
    #print(generator("Day_3_Problems/data/day_3_input.txt"))
    print(generator("Day_3_Problems/data/test_1.txt"))

if __name__ == "__main__":
    main()