
# RECURSION EXAMPLES

# ---------------------------------------------#
# -------TO FIND FACTORIAL OF A NUMBER---------#
# ---------------------------------------------#

def get_fact(n: int):
    if n >= 1:
        return n * get_fact(n-1)
    else:
        return 1


#  performed multiple operations to check factorial
# print(get_fact(2))
# print(get_fact(1))
# print(get_fact(0))
# print(get_fact(3))


# ---------------------------------------------#
# -----------TO GET FIBONACCI SERIES----------#
# ---------------------------------------------#


# def get_fib_series(num):
#     if num >= 3:
#         return (get_fib_series(num-1) + get_fib_series(num-2))
#     else:
#         return 1


# print(get_fib_series(10))
# print(get_fib_series(1))
# print(get_fib_series(2))
# print(get_fib_series(3))
# print(get_fib_series(4))
# print(get_fib_series(5))
# print(get_fib_series(6))


""" --------------------------------PRACTISE SETS-------------------------------- """

"""Question1:  check whether a passed integer is the power of three or not return True if it is a power of Three otherwise return False"""


def power_of_three(num):
    pass


print(power_of_three(3))
