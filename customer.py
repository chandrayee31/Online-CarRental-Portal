import sys
from utils import Utility
from car_rental import CarRental
import tabulate


class Customer:
    """
    Represents a customer in the car rental system.
    """

    def __init__(self):
        pass

    def cust_menu(self, cars):
        """
        Displays the customer menu and handles the user's selection.

        Args:
            cars (list): A list of cars available for rental.

        Returns:
            None
        """
        display_names = ["Rent/Return a Car", "Exit"]
        menu_items = dict(enumerate(display_names, start=1))

        while True:
            Utility.display_menu(menu_items)
            selection = int(input("Please enter your selection number: "))
            if selection == 1:
                Customer.book_car(self, cars)
            elif selection == 2:
                Utility.done()

    def book_car(self, cars):
        """
        Displays the list of available cars and allows the customer to book a car.

        Args:
            cars (list): A list of cars available for rental.

        Returns:
            None
        """
        print(tabulate.tabulate(cars, headers='keys', tablefmt='psql'))
        CarRental.main_menu(self, cars)
        

