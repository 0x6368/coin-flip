#!/bin/env python3
import copy

import numpy as np
from dealer import Dealer
from dealer import CleverDealer
from simulation import Simulation
import time
from tqdm import tqdm
from bit import get_rand_number
import logging
import matplotlib.pyplot as plt


def main():
    number_of_coins = 30

    start = time.time()

    throws = []
    dealers = []

    number_of_throws = 10**6

    if number_of_throws < 2**number_of_coins:
        print('Generating random throws...')
        for i in tqdm(range(0, number_of_throws)):
            throws.append(get_rand_number(number_of_coins))
    else:
        throws = range(0, 2**number_of_coins)

    for i in range(0, number_of_coins):
        if False and i == 2:
            dealer = CleverDealer(i, number_of_coins)
        else:
            dealer = Dealer(i, number_of_coins)
        dealers.append(dealer)

    print('Simulating throws...')
    for throw in tqdm(throws):
        Simulation.simulate_throw(throw, number_of_coins, number_of_throws, dealers)

    y_values = []
    x_values = []
    print('')
    for dealer in dealers:
        description = dealer.get_description()
        profit = dealer.profit
        y_values.append(profit)
        x_values.append(dealer.number / number_of_coins)
        print(f'{description}: {profit: 6.4f}')

    end = time.time()

    plt.plot(x_values, y_values)
    plt.ylabel('profit')
    plt.xlabel('information')
    plt.axhline(y=0, color='r', linestyle='-')
    plt.show()

    print(f'{end - start:.2f} seconds elapsed.')


if __name__ == '__main__':
    main()
