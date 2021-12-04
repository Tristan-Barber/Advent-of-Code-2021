def binary_to_decimal(bits):
    bits = bits[::-1]
    total = 0
    place = 0
    for bit in bits:
        total += int(bit) *2**place
        place += 1
    return total

def main():
    print(binary_to_decimal("100101"))

if __name__ == "__main__":
    main()