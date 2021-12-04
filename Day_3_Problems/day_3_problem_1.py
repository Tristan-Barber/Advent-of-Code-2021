def binary_to_decimal(bits):
    bits = bits[::-1]
    total = 0
    place = 0
    for bit in bits:
        total += int(bit) *2**place
        place += 1
    return total

def easy_iterable(filename):
    with open(filename) as file:
        return [i.strip() for i in file.readlines()]

#I could probably use a comparitor to make it less code
def epsilon(filename):
    #Least Common
    bits = ""
    place = 0
    binaries = easy_iterable(filename)
    while place != len(binaries[0]):
        zero = 0
        one = 0
        for line in binaries:
            if int(line[place]) == 0:
                zero += 1
            elif int(line[place]) == 1:
                one += 1
        if zero > one:
            bits += "1"
        elif one > zero:
            bits += "0"
        place += 1
    return bits

def gamma(filename):
    #Most Common
    bits = ""
    place = 0
    binaries = easy_iterable(filename)
    while place != len(binaries[0]):
        zero = 0
        one = 0
        for line in binaries:
            if int(line[place]) == 0:
                zero += 1
            elif int(line[place]) == 1:
                one += 1
        if zero > one:
            bits += "0"
        elif one > zero:
            bits += "1"
        place += 1
    return bits
    

def main():
    #print(binary_to_decimal("100101"))
    
    gam = binary_to_decimal(gamma("Day_3_Problems/data/day_3_input.txt"))
    eps = binary_to_decimal(epsilon("Day_3_Problems/data/day_3_input.txt"))
    print(gam*eps)

if __name__ == "__main__":
    main()