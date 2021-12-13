"""
Solutions the for problems of day 1 of Advent of Code
------------------------
Tristan Barber
"""

numbers_to_call = [12,28,0,63,26,38,64,17,74,67,51,44,77,32,6,10,52,47,61,46,50,29,15,1,39,37,13,66,45,8,68,96,53,40,76,72,21,93,16,83,62,48,11,9,20,36,91,19,5,42,99,84,4,95,92,89,7,71,34,35,55,22,59,18,49,14,54,85,82,58,24,73,31,97,69,43,65,27,81,56,87,70,33,88,60,2,75,90,57,94,23,30,78,80,41,3,98,25,79,86]
bingo_board_source = "Day_4_Problems/data/boards.txt"

def easy_iterable(filename):
    with open(filename) as file:
        return [i.strip().split() for i in file.readlines()]

def make_boards():
    boards = []
    data = easy_iterable(bingo_board_source)
    board = []
    for row in data:
        if row != []:
            board.append(row)
        else:
            boards.append(board)
            board = []
    return boards

def main():
    boards = make_boards()
    for board in boards:
        for row in board:
            print(row)
        print("\n")
    #print(easy_iterable(bingo_board_source))

if __name__ == "__main__":
    main()