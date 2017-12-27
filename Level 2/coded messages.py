#
#
#


def answer(l, t):
    list_count = len(l)
    print(list_count)
    for start in range(list_count):
        for end in range(list_count+1):
            subtotal = sum(l[start:end])
            print('[%s:%s]: %s' % (start, end, subtotal))
            if subtotal == t:
                return [start, end-1]
    return [-1, -1]

l1 = [4, 3, 10, 2, 8]
t1 = 27
a1 = [2, 3]

l2 = [1, 2, 3, 4]
t2 = 15
a2 = [-1, -1]

l3 = [4, 3, 5, 7, 8]
t3 = 12
a3 = [0, 2]

l4 = [1, 2, 3, 4]
t4 = 15
a4 = [-1, -1]

l5 = [1, 2, 3, 4]
t5 = 15
a5 = [-1, -1]

l6 = [1, 2, 4, 8]
t6 = 15
a6 = [0, 4]


print(answer(l1, t1) == a1)
# print(answer(l2, t2) == a2)
# print(answer(l3, t3) == a3)
#
# print(answer(l6, t6) == a6)