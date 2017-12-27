def answer(total_bricks):

    combinations = [[0 for rows in range(total_bricks)] for cols in range(total_bricks + 1)]

    # If total_bricks < 3, there are no possibilities for building the stairwell.
    # this will loop through all
    for first_three in range(3):
        for num in range(first_three, total_bricks):
            combinations[first_three][num] = 1

    # For the rest of them, the formula is incremental.
    for num in range(3, total_bricks + 1):
        for bot in range(2, total_bricks):
            combinations[num][bot] = combinations[num][bot - 1]
            if bot <= num:
                combinations[num][bot] += combinations[num - bot][bot - 1]

    # This index on the matrix should contain our solution to the number of distinct combinations.
    return combinations[total_bricks][total_bricks - 1]

tests = [
    [3,0],
    [4,0],
    [5,0],
    [6,0],
    [7,0],
    [10,0],
    [75,0],
    [100,0],
    [200,0]
]

for results in tests:
    # print('n = %s; Correct: %s' %(results[1]))
    print(results[1])