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

def answer(n):
    max_steps = triangle_number(n)
    staircase_count = 0
    bricks_in_step = 0
    for steps in range(2,max_steps):
        total_bricks = n
        for step in range(steps):
            print(step)

    return staircase_count


def triangle_number(x):
    n = 0
    while True:
        n += 1
        f_n = (n*(n+1))/2
        # print(str(n) + ': ' + str(f_n))
        if f_n > x:
            # n -= 1
            # because we are using range(n) in answer(), we don't need to reduce a step here
            return n


def combos_by_step(steps, brick_count):
    # given a number of steps and the brick count, find the combos available. ex with 3 steps and 5 bricks:
    #   [1,1,3]
    #   [1,2,2]
    step_combos = []
    step_bricks = []
    for step in range(0,steps):
        while True:
            step_bricks.append()
#



test1 = 3
a1 = 1

test2 = 200
a2 = 487067745

print(triangle_number(3))

# print(answer(test1))
# print(answer(test2))