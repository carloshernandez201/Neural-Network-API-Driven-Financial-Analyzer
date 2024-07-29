import matplotlib.pyplot as plt
import requests
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense


class Stock:
    def __init__(self, name, month, year, day, time, money_spent):

        #price implementation\
        self.name = name
        #self.industry = industry
        self.weight = 0


        base_url = "https://financialmodelingprep.com/api"
        current_price_url = f'{base_url}/v3/stock/real-time-price/{name}?apikey={API_KEY}'
        current_price = requests.get(current_price_url)
        if current_price.status_code != 200:
            print("AAA")
        current_price = current_price.json()
        self.current_price = current_price['companiesPriceList'][0]['price']
        #historic price
        date_no_time = f'{year}-{month}-{day}'
        date_as_search = f'{year}-{month}-{day} {time}:00'
        date = date_as_search
        purchase_price_url = f'{base_url}/v3/historical-chart/5min/{name}?from={date_no_time}&to={date_no_time}&apikey={API_KEY}'
        print(f"{name}   {purchase_price_url}")
        purchase_price = requests.get(purchase_price_url)
        if purchase_price.status_code == 200:
            found = False
            for entry in purchase_price.json():
                if entry['date'] == date_as_search:
                    print(entry['date'] + "for this cpmpany at price : " + str(entry["open"]))
                    self.average_price = entry['open']
                    found = True
                    break
            if not found:
                raise ValueError("no purchasse price found")
        else:
            raise ValueError("no connection found")

        self.shares = int(money_spent)/ self.current_price
        self.stock_investment = self.shares*self.average_price
        self.stock_value = self.shares * self.current_price


        #find sector
        company_info_url = f'https://financialmodelingprep.com/api/v3/profile/{name}?apikey={API_KEY}'
        company_info = requests.get(company_info_url)
        if company_info.status_code != 200:
            print(company_info_url)
            print("BBBBBB")
        company_info = company_info.json()
        self.sector =company_info[0]['sector']

        #implement industry and then jsut implement portfolio'''


    def extra_purchase(self, month, year, day, time, money_spent):


        base_url = "https://financialmodelingprep.com/api"
        current_price_url = f'{base_url}/v3/stock/real-time-price/{self.name}?apikey={API_KEY}'
        current_price = requests.get(current_price_url)
        if current_price.status_code != 200:
            print("AAA")
        current_price = current_price.json()
        current_price = current_price['companiesPriceList'][0]['price']

        date_no_time = f'{year}-{month}-{day}'
        date_as_search = f'{year}-{month}-{day} {time}:00'
        date = date_as_search
        purchase_price_url = f'{base_url}/v3/historical-chart/5min/{self.name}?from={date_no_time}&to={date_no_time}&apikey={API_KEY}'
        print(f"{self.name}   {purchase_price_url}")
        purchase_price = requests.get(purchase_price_url)
        if purchase_price.status_code == 200:
            found = False
            for entry in purchase_price.json():
                if entry['date'] == date_as_search:
                    print(entry['date'] + "for this cpmpany at price : " + str(entry["open"]))
                    old_cost = self.average_price*self.shares
                    self.shares+= int(money_spent)/self.current_price
                    self.average_price = (old_cost + int(money_spent))/self.shares

                    found = True
                    break
            if not found:
                raise ValueError("no purchasse price found")
        else:
            raise ValueError("no connection found")
        self.stock_investment = self.shares * self.average_price
        self.stock_value = self.shares * self.current_price
    @property
    def return_rate(self):
        if self.stock_investment > 0:
            print("my return rate is"+ str(100*(self.stock_value - self.stock_investment) / self.stock_investment))
            return (100*self.stock_value - self.stock_investment) / self.stock_investment
        else:
            return 0



def fetch_stock_data(ticker):
    url = f"https://financialmodelingprep.com/api/v3/historical-price-full/{ticker}?apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    if 'historical' in data:
        return pd.DataFrame(data['historical'])
    else:
        raise ValueError("Failed to fetch data. Check the ticker symbol or your API key.")

def create_and_train_lstm_model(stock_data):
    if isinstance(stock_data, np.ndarray):
        # Convert the numpy array to a DataFrame
        stock_data = pd.DataFrame(stock_data, columns=['date', 'close'])

        # Check if stock_data is now a DataFrame
    if not isinstance(stock_data, pd.DataFrame):
        raise ValueError("stock_data should be a pandas DataFrame or convertible to one")

        # Check if 'date' column exists
    if 'date' not in stock_data.columns:
        raise ValueError("'date' column is missing from stock_data")

        # Convert the date column to datetime
    stock_data['date'] = pd.to_datetime(stock_data['date'])
    stock_data.set_index('date', inplace=True)

    # Extract the close prices as a numpy array
    stock_data = stock_data['close'].values

    # Scale the data to the range [0, 1]
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(stock_data.reshape(-1, 1))

    # Split the data into training and testing sets
    train_size = int(len(scaled_data) * 0.8)
    train_data = scaled_data[:train_size]
    test_data = scaled_data[train_size:]

    # Create the dataset for training the LSTM model
    def create_dataset(data, time_step=1):
        X, Y = [], []
        for i in range(len(data) - time_step - 1):
            X.append(data[i:(i + time_step), 0])
            Y.append(data[i + time_step, 0])
        return np.array(X), np.array(Y)

    time_step = 100
    X_train, y_train = create_dataset(train_data, time_step)
    X_test, y_test = create_dataset(test_data, time_step)

    # Reshape the data to fit the LSTM model
    X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
    X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

    # Define the LSTM model
    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=(time_step, 1)))
    model.add(LSTM(50, return_sequences=False))
    model.add(Dense(1))

    # Compile the model
    model.compile(optimizer='adam', loss='mean_squared_error')

    # Train the model
    model.fit(X_train, y_train, epochs=1, batch_size=1, verbose=1)

    return model, scaler, X_test, y_test

def predict_stock_prices(model, scaler, X_test, y_test, time_unit='Days'):
    # Predict stock prices
    predictions = model.predict(X_test)
    predictions = scaler.inverse_transform(predictions)
    y_test = scaler.inverse_transform(y_test.reshape(-1, 1))

    # Plot true vs. predicted prices
    plt.figure(figsize=(10, 6))
    plt.plot(y_test, label='True Price', color='blue')
    plt.plot(predictions, label='Predicted Price', color='red')
    plt.xlabel(time_unit)
    plt.ylabel('Stock Price')
    plt.title('Stock Price Prediction')
    plt.legend()
    plt.show()

def predict_next_day_price(model, scaler, last_100_days):
    last_100_days_scaled = scaler.transform(last_100_days.reshape(-1, 1))
    X_input = last_100_days_scaled[-100:].reshape(1, 100, 1)
    predicted_price_scaled = model.predict(X_input)
    predicted_price = scaler.inverse_transform(predicted_price_scaled)[0][0]
    return predicted_price
def fetch_last_100_days(stock_data):
    # Ensure stock_data is sorted by date
    stock_data = stock_data.sort_index()
    # Get the last 100 days of the 'close' price
    last_100_days = stock_data['close'].values[-100:]
    return last_100_days
def get_current_price(ticker):
    base_url = "https://financialmodelingprep.com/api"
    current_price_url = f'{base_url}/v3/stock/real-time-price/{ticker}?apikey={API_KEY}'
    print(current_price_url)
    current_price = requests.get(current_price_url)
    if current_price.status_code != 200:
        print("AAA")
    current_price = current_price.json()
    current_price = current_price['companiesPriceList'][0]['price']
    return current_price
