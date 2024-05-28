import requests
from Portfolio import Portfolio
from Stock import Stock
import matplotlib.pyplot as plt
# Press the green button in the gutter to run the script.


if __name__ == '__main__':
  # YOU NEEDE TO TATTRIBUTE TO FINANCIAL MODELING PREP
  menu_selection = -2
  portfolio = Portfolio()
  while menu_selection != 0:
   print()
   print("Menu")
   print("-------- ")
   print("0. Exit")
   print("1. Buy New Stock")
   print("2. Buy More Shares")
   print("3. Display Diversification by Industry")
   print("4. Display Total Investments")
   menu_selection = int(input())
   if menu_selection == 0:
       break
   elif menu_selection == 1:
       ticker = input("Whats the ticker ")
       year = input("Year ")
       month = input("Month ")
       day = input("Day ")
       time = input("Time ")
       money_spent = input("Money Spent ")
       newStock = Stock(ticker, month, year, day, time, money_spent)
       portfolio.add_stock(newStock)
   elif menu_selection == 2:
       ticker = input("Whats the ticker ")
       year = input("Year ")
       month = input("Month ")
       day = input("Day ")
       time = input("Time ")
       money_spent = input("Money Spent ")
       stock_to_buy_more = portfolio.get_stock(ticker)
       stock_to_buy_more.extra_purchase(month, year, day, time, money_spent)
   elif menu_selection == 3:
       portfolio.pie_chart(True)
   elif menu_selection == 4:
       portfolio.pie_chart(False)
   elif menu_selection == 5:
       print("Weighted Return is: " + str(portfolio.calculate_weighted_return()) +  "%")