from math import sqrt


def is_prime(number):
    return not any(number % divider == 0 for divider in xrange(2, int(sqrt(number)) + 2))