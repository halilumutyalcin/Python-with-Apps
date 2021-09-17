
######################################
########                      ########
# https://github.com/halilumutyalcin #
########                      ########
######################################

from forex_python.converter import CurrencyRates

c = CurrencyRates()

def convert():
    print("Welcome to live foreign currency")
    index = input("Enter your index (first index): ")
    rate = input("Enter your exchange rate: ")
    index = index.upper()
    rate = rate.upper()
    amount = int(input("Enter your amount: "))
    print(f"Your total amount is {round(c.convert(index, rate, amount), 2)}")


# exchange = ["USD_TRY", "USD_EUR", "USD_GBP",
#             "EUR_TRY", "EUR_USD", "EUR_GBP",
#             "GBP_USD", "GBP_EUR", "GBP_TRY",
#             "TRY_USD", "TRY_EUR", "TRY_GBP"]
#
# exchange_value = [8.29, 0.83, 0.72,
#                   10.01, 1.21, 0.87,
#                   1.39, 1.15, 11.51,
#                   0.12, 0.1, 0.087]
#
# rate = input("Enter your index with '_', example;USD_TRY : ").upper()
# endex = exchange.index(rate)
# print(f"{exchange[endex]} | {exchange_value[endex]}")
# amount = int(input("Amount = "))
# total = amount * exchange_value[endex]
# print(f"Your total amount is {round(total,2)}")