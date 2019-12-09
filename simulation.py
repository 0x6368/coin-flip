import logging
import time

from dealer import Dealer
import numpy as np


class Simulation:
    @staticmethod
    def simulate_throw(throw, number_of_coins, number_of_throws, number_of_dealers):
        paper_value = bin(throw).count("1")
        logging.info(f'Throw: {throw:0{number_of_coins}b} - Value: {paper_value:.2f}')

        average_estimation = 0
        number_of_sellers = 0
        number_of_buyers = 0

        estimates = np.zeros(number_of_dealers)
        profits = np.zeros(number_of_dealers)

        for dealer in range(0, number_of_dealers):
            description = Dealer.get_description(dealer)
            estimated_value = Dealer.get_estimated_inner_value(throw, dealer, number_of_coins)
            average_estimation += estimated_value / number_of_dealers
            estimates[dealer] = estimated_value
            logging.debug(f'{description}: {estimated_value:09.4f}')

        for dealer in range(0, number_of_dealers):
            estimated_value = estimates[dealer]
            if Dealer.will_sell(average_estimation, estimated_value):
                number_of_sellers += 1
            else:
                number_of_buyers += 1

        profit = (average_estimation - paper_value)

        if number_of_buyers < number_of_sellers:
            real_profit = profit * number_of_buyers / number_of_sellers
            real_loss = - profit
        elif number_of_sellers < number_of_buyers:
            real_profit = profit
            real_loss = - profit * number_of_sellers / number_of_buyers
        else:
            real_profit = profit
            real_loss = - profit

        for dealer in range(0, number_of_dealers):
            estimated_value = estimates[dealer]
            if Dealer.will_sell(average_estimation, estimated_value):
                profits[dealer] += real_profit / number_of_throws
            else:
                profits[dealer] += real_loss / number_of_throws

        logging.info(f'Average estimation: {average_estimation:.4f}\n')
        logging.info('===============\n')
        return profits
