# def BinarySearch(lys, val):
#     first = 0
#     last = len(lys) - 1
#     index = -1
#     while (first <= last) and (index == -1):
#         mid = (first + last) // 2
#         if lys[mid] == val:
#             index = mid
#         else:
#             if val < lys[mid]:
#                 last = mid - 1
#             else:
#                 first = mid + 1
#     return index

# print(BinarySearch([10, 20, 30, 40, 50], 20))

# dic = {'rating': 4.666666666666667}

#  d = {'a': 1, 'b': {'c': 2}} -> Iterable[('a', 1), ('b.c': 2)]

# d = {'a': 1, 'b': {'c': 2}}
#
#
# def something(a):
#     ret = []
#     for e in a:
#         if ...:
#             ret.append(e)
#         else:
#             something(e)
#     return ret
#
#
# print(something(d))


# def func1(a):
#     def func2(b, c):
#         try:
#             for e in c:
#                 if type(c) is not dict:
#                     return f'{b}.{e}', c[e]
#                 else:
#                     return func2(f'{b}.{e}', c[e])
#         except TypeError:
#             return {b: c}
#
#     ret = []
#     for e in a:
#         if type(a[e]) is not dict:
#             ret.append((e, a[e]))
#         else:
#             ret.append(func2(e, a[e]))
#     return ret
#
#
# if __name__ == '__main__':
#     d = {'a': 1, 'b': {'c': {'d': {'e': 2}}}, 'f': {'g': 2}}
#     print(d)
#     print(func1(d))


def factorial_recursive(n):
    if n == 1:
        return n
    else:
        return n * factorial_recursive(n - 1)


print(factorial_recursive(1))
print(factorial_recursive(2))
print(factorial_recursive(3))
