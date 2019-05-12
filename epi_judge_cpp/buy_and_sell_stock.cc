#include <vector>
#include "test_framework/generic_test.h"
using std::vector;

double BuyAndSellStockOnce(const vector<double>& prices) {
	double maxProfit = 0.0, minPrice = INT_MAX;
	for (auto const& price: prices) {
		minPrice = std::min(price, minPrice);
		maxProfit= std::max(maxProfit, price - minPrice);
	}
	return maxProfit;
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"prices"};
  return GenericTestMain(args, "buy_and_sell_stock.cc",
                         "buy_and_sell_stock.tsv", &BuyAndSellStockOnce,
                         DefaultComparator{}, param_names);
}
