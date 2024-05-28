import matplotlib.pyplot as plt
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