#!/bin/env python3
import math

import numpy as np
from dealer import Dealer
from simulation import Simulation
import time
from tqdm import tqdm
from bit import get_rand_number
import matplotlib.pyplot as plt
from joblib import Parallel, delayed


def main():
    number_of_coins = 200

    start = time.time()

    throws = []
    number_of_dealers = number_of_coins#math.ceil(number_of_coins / 2)

    number_of_throws = 2**15

    if number_of_throws < 2**number_of_coins:
        print('Generating random throws...')
        for i in tqdm(range(0, number_of_throws)):
            throws.append(get_rand_number(number_of_coins))
    else:
        throws = range(0, 2**number_of_coins)

    print('Simulating throws...')
    cumulated_profits = np.zeros(number_of_dealers)
    profits = Parallel(n_jobs=12)(
        delayed(Simulation.simulate_throw)(throw, number_of_coins, number_of_throws, number_of_dealers) for throw in tqdm(throws)
    )

    for profits_single_simulation in profits:
        cumulated_profits += profits_single_simulation

    y_values = []
    x_values = []
    print('')
    for dealer in range(0, number_of_dealers):
        description = Dealer.get_description(dealer)
        profit = cumulated_profits[dealer]
        y_values.append(profit)
        x_values.append(dealer / number_of_coins)
        print(f'{description}: {profit: 6.4f}')

    end = time.time()

    plt.plot(x_values, y_values)
    plt.ylabel('profit')
    plt.xlabel(f'information\nnumber of coins: {number_of_coins}\nnumber of trades: {number_of_throws}')
    plt.axhline(y=0, color='r', linestyle='-')
    plt.show()

    print(f'{end - start:.2f} seconds elapsed.')


if __name__ == '__main__':
    main()
