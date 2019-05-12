from test_framework import generic_test


def buy_and_sell_stock_once(prices):
	max_profit = 0.0
	min_price = float('inf')
	for price in prices:
		min_price = min(min_price, price)
		max_profit= max(max_profit, price - min_price)
	return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
