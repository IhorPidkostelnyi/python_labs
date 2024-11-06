class Park:

    def __init__(self, adress = None, lenth = 0, price = 0):
        self.__adress = adress
        self.__lenth = lenth
        self.__price = price

    def get_adress(self):
        return self.__adress

    def set_adress(self, adress):
        self.__adress = adress

    def get_lenth(self):
        return self.__lenth

    def set_lenth(self, lenth):
        self.__lenth = lenth

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def __str__(self):
        return f"Park(Адреса: { self.__adress}, Довжина: {self.__lenth}, Ціна: {self.__price})"

    def __repr__(self):
        return f"Park(Адреса='{self.__adress}', Довжина='{self.__lenth}', Ціна: '{self.__price}')"

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
    print(type(park4))
    print(f"Тільки адреса: {park4.get_adress()}")
    print(repr(park1))
    print(repr(park2))
    print(repr(park3))

main()
