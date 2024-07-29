import requests
import matplotlib.pyplot as plt
class Portfolio:
    def __init__(self):
        self.stocks = []
        self.total_value = 0
        self.sectors = {
            "Basic Materials": [],
            "Communication Services": [],
            "Consumer Cyclical": [],
            "Consumer Defensive": [],
            "Energy": [],
            "Financial Services": [],
            "Healthcare": [],
            "Industrials": [],
            "Miscellaneous": [],
            "Real Estate": [],
            "Technology": [],
            "Utilities": []
        }

        for stock in self.stocks:
            self.total_value += stock.stock_value
            print(str(stock.stock_value))
        self.color_list = ['blue', 'red', 'green', 'yellow', 'purple', 'orange']

    def add_stock(self, stock):
        self.stocks.append(stock)
        self.sectors[stock.sector].append(self.stocks)
        self.total_value += stock.stock_value

    def get_stock(self, name):
        for stock in self.stocks:
            if stock.name == name:
                return stock

        return None


    def pie_chart(self, sector):
        plt.style.use("fivethirtyeight")
        if(sector == False):
            plt.title("Total Investment")
            plt.tight_layout()
            # will python trat doubles properly
            slices = []
            labels = []
            for stock in self.stocks:
                slices.append(stock.stock_value)
                labels.append(stock.name)
            plt.pie(slices, labels=labels, colors=self.color_list, wedgeprops={'edgecolor': 'black'})
            plt.show()
        else:
            plt.title("Total Investment By sector")
            plt.tight_layout()
            sector_totals = {key: 0 for key in self.sectors.keys()}
            for stock in self.stocks:
                sector_totals[stock.sector] += stock.stock_value
            slices = [amount for amount in sector_totals.values() if amount > 0]
            labels = [sector for sector, amount in sector_totals.items() if amount > 0]
            plt.pie(slices, labels=labels, colors=self.color_list, wedgeprops={'edgecolor': 'black'})
            plt.show()

        # Graphing method\

    def total_value(self):
        return sum(stock.value() for stock in self.stocks)

    def calculate_weights(self):
        total_value = self.total_value
        print("toal value is " + str(total_value))
        if total_value > 0:
            for stock in self.stocks:
                stock.weight = stock.stock_value / total_value
        else:
            for stock in self.stocks:
                stock.weight = 0

    def calculate_weighted_return(self):
        total_return = 0
        self.calculate_weights()
        for stock in self.stocks:
            print(stock.weight)
            weighted_return = stock.weight * stock.return_rate
            total_return += weighted_return
        return total_returnimport
