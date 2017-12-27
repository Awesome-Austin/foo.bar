__author__ = 'ausgi_000'
#! python2.7.6
# The Grandest Staircase Of Them All
# ==================================
#
# With her LAMBCHOP doomsday device finished, Commander Lambda is
# preparing for her debut on the galactic stage - but in order to make
# a grand entrance, she needs a grand staircase! As her personal
# assistant, you've been tasked with figuring out how to build the
# best staircase EVER.
#
# Lambda has given you an overview of the types of bricks available,
# plus a budget. You can buy different amounts of the different types
# of bricks (for example, 3 little pink bricks, or 5 blue lace bricks).
# Commander Lambda wants to know how many different types of staircases
# can be built with each amount of bricks, so she can pick the one with
# the most options.
#
# Each type of staircase should consist of 2 or more steps.  No two
# steps are allowed to be at the same height - each step must be lower
# than the previous one. All steps must contain at least one brick. A
# step's height is classified as the total amount of bricks that
# make up that step.
# For example, when N = 3, you have only 1 choice of how to build the
# staircase, with the first step having a height of 2 and the second
# step having a height of 1: (# indicates a brick)
#
# #
# ##
# 21
#
# When N = 4, you still only have 1 staircase choice:
#
# #
# #
# ##
# 31
#
# But when N = 5, there are two ways you can build a staircase from the given bricks.The two staircases can have
# heights(4, 1) or (3, 2), as shown below:
#
# #
# #
# #
# ##
# 41
#
# #
# ##
# ##
# 32
#
# Write a function called answer(n) that takes a positive integer n and returns the number of different staircases that
# can be built from exactly n bricks. n will always be at least 3 (so you can have a staircase at all), but no more than
# 200, because Commander Lambda 's not made of money!
#
# Test cases
# ==========
#
# Inputs:
#     (int) n = 3
# Output:
#     (int) 1
#
# Inputs:
#     (int) n = 200
# Output:
#     (int) 487067745
# given some number n we first find the max number of steps by finding where f(x) = (x(x+1))/2 > n. we then loop
# through all the steps to see all the combinations of bricks
#
# In practice we are looking for the unique combinations for a given number of bricks.
# first we find the max number of columns by finding the first number 'n' on the triangle number sequence that is
# greater than number of bricks provided.
# then we loop through each column and find the unique arrangements for bricks for each column set of bricks




def answer(n):
    bricks = n
    max_columns = triangle_number(n)
    unique_count = 0
    for column in range(2, max_columns + 1):
        unique_count += unique_staircases(bricks,column)
    return unique_count


def triangle_number(bricks):
    column = 0
    while True:
        column += 1
        total_bricks = (column * (column + 1)) / 2
        # print(str(n) + ': ' + str(f_n))
        if total_bricks > bricks:
            column -= 1
            # because we are using range(n) in answer(), we don't need to reduce a step here
            return column


def unique_staircases(bricks, columns):
    staircase_count = 0
    for staircase in sums_to_bricks(bricks, columns):
        if unique_staircase(staircase):
            staircase_count += 1
    return staircase_count


def sums_to_bricks(bricks, columns, limit=None):
    if columns == 1:
        yield [bricks]
        return
    if limit is None:
        limit = bricks
    start = (bricks + columns - 1) // columns
    stop = min(limit, bricks - columns + 1) + 1
    for i in range(start, stop):
        for tail in sums_to_bricks(bricks - i, columns - 1, i):
            yield [i] + tail


def unique_staircase(staircase):
    for i in range(len(staircase)-1):
        if staircase[i] == staircase[i + 1]:
            return False
    return True


# print(triangle_number(10))
# print(unique_staircases(6, 4))
# print(unique_staircase([3, 3]))

bricks1 = 100
answer1 = 1
bricks2 = 200
answer2 = 487067745

# print(answer(bricks1))

# print(answer(bricks2))

for i in range(3,100):
    print('columns: %s; combos: %s' % (i, answer(i)))