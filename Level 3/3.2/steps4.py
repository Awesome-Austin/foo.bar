def answer(total_bricks):

    combinations = [[0 for rows in range(total_bricks)] for cols in range(total_bricks + 1)]

    # If total_bricks < 3, there are no possibilities for building the stairwell.
    # this will loop through all8
    for first_three in range(3):
        for row in range(first_three, total_bricks):
            combinations[first_three][row] = 1

    # For the rest of them, the formula is incremental.
    for row in range(3, total_bricks + 1):
        for col in range(2, total_bricks):
            combinations[row][col] = combinations[row][col - 1]
            if col <= row:
                combinations[row][col] += combinations[row - col][col - 1]

    # This index on the matrix should contain our solution to the number of distinct combinations.
    return combinations[total_bricks][total_bricks - 1]


print(answer(200))