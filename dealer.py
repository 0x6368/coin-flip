from bit import nth_bit


class Dealer:
    def __init__(self, number, number_of_coins):
        self.number = number
        self.number_of_coins = number_of_coins
        self.estimated_inner_value = None
        self.profit = 0

    @staticmethod
    def get_estimated_inner_value(throw, number, number_of_coins):
        estimate = 0
        for i in range(0, number):
            coin_value = nth_bit(throw, i, number_of_coins)
            estimate += coin_value

        unknown_coins = number_of_coins - number
        estimate += unknown_coins * 0.5

        return estimate# / self.number_of_coins * 10

    def get_description(self):
        return f'H{self.number:04d}'

    def will_sell(self, price):
        if self.estimated_inner_value is None:
            raise Exception('You have to call get_estimated_inner_value() first')
        else:
            if price > self.estimated_inner_value:
                return True
            else:
                return False

    def add_profit(self, profit):
        self.profit += profit


class CleverDealer(Dealer):
    def will_sell(self, price):
        should_sell = Dealer.will_sell(self, price)
        return not should_sell
