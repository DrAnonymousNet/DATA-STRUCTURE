from typing import List


def find_max_profit(price_list:List) -> int:
    if len(price_list) > 1:
        return
    max_profit = 0
    for index, price in enumerate(price_list):
        max_difference = find_max_difference(price, price_list[index:])
        max_profit = max(max_profit,max_difference)
    return max_profit


def find_max_difference(price:int, price_list:List) -> int:
    max_diff = 0
    for curr_price in price_list:
        difference = curr_price - price
        max_diff = max(max_diff, difference)

    return max_diff

tests = [[2,7,1,4],
        [7,1,5,3,6,4],
        [1,1,1,1,1],
        [100,180,260,310,40,535,695]
]

for test in tests:
    print(find_max_profit(test))
