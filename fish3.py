class FishInfo:
    pass


class Fish(FishInfo):

    def __init__(self, name: str, price_in_uah_per_kilo: float, origin: str, body_only: bool, weight: float) -> None:
        self.name = name
        self.price_in_uah_per_kilo = price_in_uah_per_kilo
        self.origin = origin
        self.body_only = body_only
        self.weight = weight
        print(self.weight, "of", self.name, "was added")


class FishBox:

    def __init__(self, max_weight, fish: Fish, weight):
        self.name = fish.name
        self.max_weight = max_weight
        self.fish_in_the_box = fish
        print("\n"+self.name+"Box", "was added")
        if max_weight >= weight:
            if self.fish_in_the_box.weight >= weight:
                self.fish_in_the_box.weight = weight
                fish.weight -= weight
                print("The box with", weight, "kg of",
                      self.fish_in_the_box.name, "was added\n")
            else:
                print("Not enought fish to add")
        else:
            print("Box overfilled")


class FishShop:
    fish_list = []
    box_list = []
    frozen = []
    fresh = []
    all_fish = []

    def __init__(self) -> None:
        pass

    def add_fish(self, fish: Fish):
        self.fish_list.append(fish)
        self.fresh.append(fish)
        self.all_fish.append(fish)
        print(fish.weight, "kg of", fish.name, "was added!\n")

    def add_box(self, box: FishBox):
        self.box_list.append(box)
        self.frozen.append(box.fish_in_the_box)
        self.all_fish.append(box.fish_in_the_box)
        print("Box with", box.fish_in_the_box.weight,
              "of", box.name, "was added")

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

    def get_fish_sorted_by_price(self) -> None:
        self.all_fish.sort(key=lambda x: x.price_in_uah_per_kilo)
        print("Fish list sorted by price:")
        print("Name:", "\t\tPrice per kilo in UAH:")
        for i in self.all_fish:
            print("\n", i.name, "\t\t", str(i.price_in_uah_per_kilo), "\n")

    def get_fresh_fish_names_sorted_by_price(self) -> None:
        self.fresh.sort(key=lambda x: x.price_in_uah_per_kilo)
        print("Fresh fish sorted by price:")
        print("Name:", "\t\tPrice per kilo in UAH:")
        for i in self.fresh:
            print("\n" + i.name, "\t\t", str(i.price_in_uah_per_kilo), "\n")

    def get_frozen_fish_names_sorted_by_price(self) -> None:
        self.frozen.sort(key=lambda x: x.price_in_uah_per_kilo)
        print("Frozen fish sorted by price:")
        print("Name:", "\t\tPrice per kilo in UAH:")
        for i in self.frozen:
            print("\n" + i.name, "\t\t", str(i.price_in_uah_per_kilo), "\n")


# in
fish_shop = FishShop()

fish1 = Fish(name="Shark", price_in_uah_per_kilo=125.5,
             origin="Norway", body_only=True, weight=100)

fish2 = Fish(name="Salmon", price_in_uah_per_kilo=300.25,
             origin="Norway", body_only=False, weight=200)

fish3 = Fish(name="Carp", price_in_uah_per_kilo=500.4,
             origin="Norway", body_only=True, weight=200)

fish4 = Fish(name="Scumbria", price_in_uah_per_kilo=60.6,
             origin="Norway", body_only=False, weight=300)

box1 = FishBox(200, fish1, 100)
box2 = FishBox(200, fish2, 70)
box3 = FishBox(200, fish2, 120)
box4 = FishBox(200, fish3, 200)

fish_shop.add_fish(fish1)
fish_shop.add_fish(fish2)
fish_shop.add_fish(fish3)
fish_shop.add_fish(fish4)

fish_shop.add_box(box1)
fish_shop.add_box(box2)
fish_shop.add_box(box3)
fish_shop.add_box(box4)

fish_shop.get_fish_sorted_by_price()
fish_shop.get_fresh_fish_names_sorted_by_price()
fish_shop.get_frozen_fish_names_sorted_by_price()
