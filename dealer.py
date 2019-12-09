from bit import nth_bit


class Dealer:
    @staticmethod
    def get_estimated_inner_value(throw, number, number_of_coins):
        estimate = 0
        for i in range(0, number):
            coin_value = nth_bit(throw, i, number_of_coins)
            estimate += coin_value

        unknown_coins = number_of_coins - number
        estimate += unknown_coins * 0.5

        return estimate# / number_of_coins * 10

    @staticmethod
    def get_description(number):
        return f'H{number:04d}'

    @staticmethod
    def will_sell(price, estimated_inner_value):
        if price > estimated_inner_value:
            return True
        else:
            return False


class CleverDealer(Dealer):
    @staticmethod
    def will_sell(price, estimated_inner_value):
        should_sell = Dealer.will_sell(price, estimated_inner_value)
        return not should_sell
