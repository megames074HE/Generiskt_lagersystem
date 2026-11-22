from typing import TypeVar, Generic

T = TypeVar("T")

class Lager(Generic[T]):

    antal_produkter = 0 #Enclosed variable

    def __init__(self, namn, produkter: list[T]):
        self.namn = namn
        self.produkter = produkter
        Lager.antal_produkter += len(produkter)

    def get_lager_products(self) -> T:
        return self.produkter

    def show_lager_info(self):
        lager_namn = self.namn
        lager_produkter = self.produkter
        antal_produkter = Lager.antal_produkter

        def print_lager_info():
            print(f"Namnet av lager är: {lager_namn}")
            print(f"Antal produkter i alla lager: {antal_produkter}")

        def print_lager_contents():
            print("Alla produkter sparad i lagern: ")
            for item in lager_produkter:
                print(f"Produkt{lager_produkter.index(item)}: {item}")


        print_lager_info()
        print_lager_contents()


lager1 = Lager[str]('lager1', ['test', 'test2'])

lager2 = Lager[int]('lager2', [1, 2, 3])

lager1.show_lager_info()