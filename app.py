from typing import TypeVar, Generic

T = TypeVar("T") # global varabel

class Lager(Generic[T]):

    antal_produkter = 0 #Class variable

    def __init__(self, namn: str, produkter: list[T]):
        self.namn = namn #Instance variable
        self.produkter = produkter #Instance variable
        Lager.antal_produkter += len(produkter)

    def get_lager_products(self) -> list[T]:
        return self.produkter

    def show_lager_info(self):
        lager_namn = self.namn #local (enclosed variabel för print_lager_info)
        lager_produkter = self.produkter #local (enclosed variabel för lager_produkter)
        antal_produkter = Lager.antal_produkter #local (enclosed variabel för print_lager_info)

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
En klass variabel är en variabel som tillhör till själva klassen. Så alla instanser kan nå samma värdet på variabeln och ändra den. 
Den finns kvar sålänge klass objektet finns. Kan därrför användas när en instans tas bort. 

En lokal variabel är variabeln som är definierad i en funktion. Den dör när metoden är klar, den finns alltså kvar så länge funktionen excecutar.
Men python kan hålla kvar det i minnet om det används senare i koden. 

Skillnaden mellan de är att en klass variabel alltid finns kvar sålänge klassen finns kvar. Även när man ta bort en instans av klassen t.ex: 

lager1 = Lager("blablablalbalb")
del lager1

variabeln antal_produkter finns då fortfarande kvar. 
'''


#Fråga 2
'''
Den kan inte nå variabler i en annan metod för att varje metod har ett eget lokalt scope. Python letar inte i andra metoders scope.

Python letar efter legb regeln. Så en annan funktions lokala vairabel tillhör inte i samma enclosing scope så den kan inte komma åt den då. 
'''