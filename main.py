from portfolio import Portfolio
from stock import Stock
import stock


if __name__ == '__main__':
    # YOU NEED TO ATTRIBUTE TO FINANCIAL MODELING PREP
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
        print("5. Create Stock Price Prediction Model")
        print("6. Calculate Weighted Portfolio Return")
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
            newStock =Stock(ticker, month, year, day, time, money_spent)
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
            ticker = input("Enter the ticker for prediction: ")
            stock_data = stock.fetch_stock_data(ticker)
            model, scaler, X_test, y_test = stock.create_and_train_lstm_model(stock_data) #create and train model, get test data
            last_100_days = stock.fetch_last_100_days(stock_data)

            
            predicted_price = stock.predict_next_day_price(model, scaler, last_100_days) # predict 
            #stock.predict_stock_prices(model, scaler, X_test, y_test)
            cur_price = stock.get_current_price(ticker)
            print(f"The current price for {ticker} is {cur_price}")
            print(f"The predicted price for {ticker} for tomorrow is: {predicted_price}")
        elif menu_selection == 6:
            print("Weighted Return is: " + str(portfolio.calculate_weighted_return()) +  "%")
