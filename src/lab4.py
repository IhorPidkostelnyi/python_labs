class Park:

    def __init__(self, adress = None, lenth = 0, price = 0, lenth_unit="meters", price_unit="currency"):
        self.__adress = adress
        self.__lenth = lenth
        self.__price = price
        self.lenth_unit = lenth_unit
        self.price_unit = price_unit

    @property
    def adress(self):
        return self.__adress

    @adress.setter
    def adress(self, adress):
        self.__adress = adress

    @property
    def lenth(self):
        return self.__lenth

    @lenth.setter
    def lenth(self, lenth):
        self.__lenth = lenth

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    def __str__(self):
        return f"Park(Adress: { self.__adress}, Lenth: {self.__lenth}, Price: {self.__price})"

    def __repr__(self):
        return f"Park('{self.__adress}', '{self.__lenth}', '{self.__price}')"

    def __del__(self):
        print(f'Deleted {self.__adress}')

def main():
    park1 = Park("Стрийська 14", "5000", "300")
    park2 = Park("вул. Львівська, 24", "3000", "100")
    park3 = Park("Івана Франка", "2000", '500')
    park4 = Park()

    print(park1)
    print(park2)
    print(park3)
    print(park4)
    
    print(repr(park1))
    print(repr(park2))
    print(repr(park3))

main()
