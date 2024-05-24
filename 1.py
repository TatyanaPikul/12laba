class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors, location, working_hours):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
        self.location = location
        self.working_hours = working_hours

    def display_info(self):
        print(f"Название кафе-мороженого: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
        print("Список сортов мороженого:")
        for flavor in self.flavors:
            print(flavor)
        print(f"Локация: {self.location}")
        print(f"Время работы: {self.working_hours}")

    def add_flavor(self, new_flavor):
        self.flavors.append(new_flavor)
        print(f"Сорт мороженого '{new_flavor}' добавлен.")

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print(f"Сорт мороженого '{flavor}' удален.")
        else:
            print(f"Сорт мороженого '{flavor}' не найден.")

    def check_flavor(self, flavor):
        if flavor in self.flavors:
            print(f"Сорт мороженого '{flavor}' доступен.")
        else:
            print(f"Сорт мороженого '{flavor}' не доступен.")

    def serve_ice_cream(self, type_of_ice_cream):
        print(f"Подаю {type_of_ice_cream} мороженое.")

ice_cream_place = IceCreamStand("BR", "мороженое", ["пломбир", "шоколадное", "фисташковое", "крем-брюле"], "Невский проспект", "10:00-23:00")
ice_cream_place.display_info()
ice_cream_place.add_flavor("крем-брюле")
ice_cream_place.remove_flavor("шоколадное")
ice_cream_place.check_flavor("ваниль")
ice_cream_place.serve_ice_cream("мягкое" )
ice_cream_place.serve_ice_cream("эскимо")
ice_cream_place.serve_ice_cream("в рожке")

import tkinter as tk

class IceCreamStand:
    def __init__(self, master):
        self.master = master
        self.master.title("Ice Cream Stand")

        self.flavors = ["Пломбир", "Шоколадное", "Крем-брюле", "Фисташковое"]
        self.selected_flavor = tk.StringVar(value=self.flavors[0])

        self.types = ["Эскимо", "В рожке", "В стаканчике"]
        self.selected_type = tk.StringVar(value=self.types[0])

        self.flavor_label = tk.Label(master, text="Выберите вкус мороженого:")
        self.flavor_label.pack()

        self.flavor_option = tk.OptionMenu(master, self.selected_flavor, *self.flavors)
        self.flavor_option.pack()

        self.type_label = tk.Label(master, text="Выберите тип мороженого:")
        self.type_label.pack()

        self.type_option = tk.OptionMenu(master, self.selected_type, *self.types)
        self.type_option.pack()

        self.order_button = tk.Button(master, text="Заказать", command=self.place_order)
        self.order_button.pack()

    def place_order(self):
        flavor = self.selected_flavor.get()
        ice_cream_type = self.selected_type.get()
        message = f"Вы заказали {ice_cream_type.lower()} мороженое со вкусом '{flavor}'. Спасибо за заказ!"
        order_confirmation = tk.Label(self.master, text=message)
        order_confirmation.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = IceCreamStand(root)
    root.mainloop()