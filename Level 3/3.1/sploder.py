# import math
#
#
# def answer(M, F):
#     gen = 0
#     m, f = int(M), int(F)
#     while True:
#         if m == 1 and f == 1:
#             return str(gen)
#         elif m < 1 or f < 1 or m == f:
#             return "impossible"
#         else:
#             if m > f:
#                 arr = gen_jump(m, f)
#                 gen += arr[0]
#                 m = arr[1]
#             else:
#                 arr = gen_jump(f, m)
#                 gen += arr[0]
#                 f = arr[1]
#
#
#
# def gen_jump(greater_value, lesser_value):
#     gen = 0
#     if greater_value > 100 * lesser_value:
#         gen += math.floor(greater_value / lesser_value)
#         greater_value -= (math.floor(greater_value / lesser_value) * lesser_value)
#     else:
#         greater_value -= lesser_value
#         gen += 1
#     return [gen, greater_value]



def answer(M, F):
    gen = 0
    m, f = int(M), int(F)
    while True:
        if m == 1 and f == 1:
            return str(gen)
        elif m < 1 or f < 1 or m == f:
            return 'impossible'
        else:
            if m > f:
                lst = gen_increase(m,f)
                gen += lst[0]
                m = lst[1]
            elif m < f:
                lst = gen_increase(f,m)
                gen += lst[0]
                f = lst[1]


def gen_increase(greater_value, lesser_value):
    gen = 0
    gen += int(greater_value/lesser_value)
    greater_value %= lesser_value
    # if the lesser value is 1, greater value will zero out, so we remove one generation
    if lesser_value == 1:
        gen -= 1
        greater_value += 1

    return [gen, greater_value]


print(answer("4", "7"))
print(answer("2", "1"))
print(answer("2", "4"))
print(answer("5555567", "4"))