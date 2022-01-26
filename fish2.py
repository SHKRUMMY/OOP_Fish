
class Fish:

    def __init__(self, name: str, price_in_uah_per_kilo: float, origin: str, body_only: bool, weight: float) -> None:
        self.name = name
        self.price_in_uah_per_kilo = price_in_uah_per_kilo
        self.origin = origin
        self.body_only = body_only
        self.weight = weight


class FishShop:
    profit = 0

    def __init__(self) -> None:
        self.fish_list = []
    # self, fish_name: str, total_weight: float

    def add_fish(self, fish: Fish) -> None:
        self.fish_list.append(fish)
        print(fish.name, "was added!\n")

    def get_fish_names_sorted_by_price(self) -> None:
        self.fish_list.sort(key=lambda x: x.price_in_uah_per_kilo)
        print("Fish list sorted by price:")
        print("Name:", "\t\tPrice per kilo in UAH:")
        for i in self.fish_list:
            print("\n" + i.name, "\t\t", str(i.price_in_uah_per_kilo), "\n")

    def sell_fish(self, fish: Fish, weight: float) -> None:

        if fish.weight > weight:
            self.profit = fish.price_in_uah_per_kilo * weight
            fish.weight -= weight
            print("\n", weight, "kg of", fish.name, "was sold!")
            print("\n", fish.weight, "kg", fish.name, "left!")

        elif weight == fish.weight:
            self.fish_list.remove(fish)
            self.profit = fish.price_in_uah_per_kilo * weight
            print("\n", fish.name, "Was sold out!")

        elif fish.weight < weight:
            print("\n", "Not that much", fish.name, "left!")
            self.fish_list.remove(fish)
            self.profit = fish.price_in_uah_per_kilo * weight
            print("\n", fish.name, "Was sold out!")
        print("\nProfit:", self.profit, "₴")

    def cast_out_old_fish(self, fish: Fish) -> None:
        self.fish_list.remove(fish)
        print("\n", fish.name, "was old and cast out!", "\n")


class Seller:
    pass

    def show_fish_sorted_by_price():
        pass

    def sell():
        pass

    def add_profit_to_account():
        pass


class Buyer:
    pass
    money = 5000
    bought_fish = []

    def enter_shop():
        print("Hello!")

    def buy_fish(self, fish: Fish, weight):
        self.money -= fish_shop.profit
        self.bought_fish.append(fish)
        fish_shop.sell_fish(fish)

    def leave_shop():
        print("Goodbye!")


# in
fish1 = Fish(name="Shark", price_in_uah_per_kilo=125.5,
             origin="Norway", body_only=True, weight=50)

fish2 = Fish(name="Salmon", price_in_uah_per_kilo=300.25,
             origin="Norway", body_only=False, weight=100)

fish3 = Fish(name="Carp", price_in_uah_per_kilo=500.4,
             origin="Norway", body_only=True, weight=200)

fish4 = Fish(name="Scumbria", price_in_uah_per_kilo=60.6,
             origin="Norway", body_only=False, weight=300)

fish_shop = FishShop()

print("\n\n\n")
fish_shop.add_fish(fish1)

fish_shop.add_fish(fish2)

fish_shop.add_fish(fish3)

fish_shop.add_fish(fish4)

#print("Fish list sorted by price:")
fish_shop.get_fish_names_sorted_by_price()

fish_shop.sell_fish(fish1, 30)

fish_shop.cast_out_old_fish(fish2)

#print("Fish list sorted by price:")
fish_shop.get_fish_names_sorted_by_price()


buyer1 = Buyer()
seller1 = Seller()
