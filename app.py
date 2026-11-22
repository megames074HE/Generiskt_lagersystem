from typing import TypeVar, Generic

T = TypeVar("T")

class Lager(Generic[T]):

    antal_produkter = 0 #Class variable

    def __init__(self, namn, produkter: list[T]):
        self.namn = namn #Instance variable
        self.produkter = produkter #Instance variable
        Lager.antal_produkter += len(produkter) #Class variable

    def get_lager_products(self) -> list[T]:
        return self.produkter

    def show_lager_info(self):
        lager_namn = self.namn #Enclosed variable
        lager_produkter = self.produkter #Enclosed variable
        antal_produkter = Lager.antal_produkter #Enclosed variable

        def print_lager_info():
            print(f"\nNamnet av lager är: {lager_namn}")
            print(f"Antal produkter i alla lager: {antal_produkter}")

        def print_lager_contents():
            print("Alla produkter sparad i lager: ")
            for item in lager_produkter:
                print(f"Produkt{lager_produkter.index(item)}: {item}")


        print_lager_info()
        print_lager_contents()


lager1 = Lager[str]('strlager', ['test', 'test2'])

lager2 = Lager[int]('intlager', [1, 2, 3])

lager3 = Lager[float]('floatlager', [1.2, 3.5, 6.7])

lager1.show_lager_info()

print(f"\n{lager2.get_lager_products()}")

lager3.show_lager_info()

#Frågor del:


#Fråga 1
'''

'''