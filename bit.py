import random


def nth_bit(number, bit, number_of_bits):
    return number >> (number_of_bits - (1 + bit)) & 1


def get_rand_number(number_of_bits):
    output = 0
    while number_of_bits > 0:
        bits = min(number_of_bits, 64)
        output = (output * (2 ** bits) + random.randint(0, 2 ** bits))
        number_of_bits -= bits

    return output
