"""
Solutions the for problems of day 1 of Advent of Code
------------------------
Tristan Barber
"""

numbers_to_call = [12,28,0,63,26,38,64,17,74,67,51,44,77,32,6,10,52,47,61,46,50,29,15,1,39,37,13,66,45,8,68,96,53,40,76,72,21,93,16,83,62,48,11,9,20,36,91,19,5,42,99,84,4,95,92,89,7,71,34,35,55,22,59,18,49,14,54,85,82,58,24,73,31,97,69,43,65,27,81,56,87,70,33,88,60,2,75,90,57,94,23,30,78,80,41,3,98,25,79,86]
test_numbers = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
bingo_board_source = "Day_4_Problems/data/boards.txt"
test_bingo = "Day_4_Problems/data/test_boards_1.txt"

def easy_iterable(filename):
    with open(filename) as file:
        return [i.strip().split() for i in file.readlines()]

def easy_board_print(board):
    for row in board:
        print(row)

def make_boards(filename):
    boards = []
    data = easy_iterable(filename)
    board = []
    for row in data:
        if row != []:
            board.append(row)
        else:
            boards.append(board)
            board = []
    boards.append(board)
    return boards

def find_winner(boards, numbers):
    for number in numbers:
        for board in boards:
            for row in board:
                i = 0
                for num in row:
                    if num == str(number):
                        row.pop(i)
                    i+=1
                if row == []:
                    return board, number

def winning_score(winning_board, winning_number):
    sum = 0
    for row in winning_board:
        for number in row:
            sum += int(number)
    print(sum)
    print(winning_number)
    score = sum * winning_number
    return score

def main():
    boards = make_boards(bingo_board_source)
    winning_board, winning_number = find_winner(boards, numbers_to_call)
    print(winning_score(winning_board, winning_number))

if __name__ == "__main__":
    main()