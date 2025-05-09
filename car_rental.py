from datetime import timedelta
from datetime import datetime
import sys
from os import system
from utils import Utility
import tabulate


class CarRental(object):
    """
    A class representing a car rental system.

    Attributes:
        rates (dict): A dictionary containing the rental rates for different durations.
    """

    def __init__(self):
        self.rates = {
            'hourly': 10,  # $10 per hour
            'daily': 50,   # $50 per day
            'weekly': 200  # $200 per week
        }

    def __del__(self):
        classname = self.__class__.__name__
        # log.info(classname +" deleted")

    def hourly(self):
        """
        Calculate the rental cost for a specified number of hours.

        Returns:
            int: The rental cost in dollars.
        """
        hours = int(input("How many hours do you want to rent the car?"))
        current_time = datetime.now()
        print("You have rented a car for ", hours, " hours")
        print("Current time is: ", current_time)
        print("Expected return time is: ", current_time + timedelta(hours=hours))
        return hours * self.rates['hourly']

    def daily(self):
        """
        Calculate the rental cost for a specified number of days.

        Returns:
            int: The rental cost in dollars.
        """
        days = int(input("How many days do you want to rent the car?"))
        current_time = datetime.now()
        print("You have rented a car for ", days, " days")
        print("Current time is: ", current_time)
        print("Expected return time is: ", current_time + timedelta(days=days))
        return days * self.rates['daily']

    def weekly(self):
        """
        Calculate the rental cost for a specified number of weeks.

        Returns:
            int: The rental cost in dollars.
        """
        weeks = int(input("How many weeks do you want to rent the car?"))
        current_time = datetime.now()
        print("You have rented a car for ", weeks, " weeks")
        print("Current time is: ", current_time)
        print("Expected return time is: ", current_time + timedelta(weeks=weeks))
        return weeks * self.rates['weekly']

    def rent_car(self, cars):
        """
        Rent a car by selecting the rental duration and car model.

        Args:
            cars (DataFrame): A DataFrame containing the available cars.

        Returns:
            int: The total rental cost in dollars.
        """
        car_id = int(input("Enter ID of the car to book :"))
        while True:
            filtered_df = cars[cars['id'] == car_id]
            for index, row in filtered_df.iterrows():
                if row['available'] == 'Not Available':
                    print(f" {row['model']} is not available")
                    amt = 0
                else:
                    name_cust = input("Enter Name of the customer to book :")
                    cars.loc[cars['id'] == int(car_id), 'available'] = 'Not Available'
                    rent_duration = ["Rent hourly", "Rent Daily", "Rent Weekly", "Back to Main Menu", "Exit"]
                    menu_items = dict(enumerate(rent_duration, start=1))
                    amt = 0
                    carRentalObj = CarRental()
                    Utility.display_menu(menu_items)
                    selection = int(input("Please enter your selection number: "))
                    if selection == 1:
                        amt = CarRental.hourly(carRentalObj);
                    elif selection == 2:
                        amt = CarRental.daily(carRentalObj)
                    elif selection == 3:
                        amt = CarRental.weekly(carRentalObj)
                    elif selection == 4:
                        CarRental.main_menu(carRentalObj, cars)
                    elif selection == 5:
                        Utility.done()
                details={'car_id':car_id,'rent_amt':amt}
                return details

    def return_car(self, cars, details:list):
        """
        Return a rented car and update its availability status.

        Args:
            cars (DataFrame): A DataFrame containing the available cars.
            bill (float): The total bill for the rental.

        Returns:
            None
        """
        car_id = int(input("Enter Car Id to return "))
        if not any(d['car_id'] == car_id for d in details):
            print(f"Car {car_id} was not rented by this customer")
            return None
        
        elif cars.loc[cars['id'] == car_id, 'available'].ne('Available').any():
            cars.loc[cars['id'] == car_id, 'available'] = 'Available'
            bill= [d['rent_amt'] for d in details if d['car_id'] == car_id]
            print(f"Car {car_id} has been returned successfully. Total bill: ${bill[0]:.2f}")
        else:
            print(f"Car {car_id} is already available or does not exist")

    def rent_multiple_car(self, cars):
        """
        Rent multiple cars by calling the rent_car method multiple times.

        Args:
            cars (DataFrame): A DataFrame containing the available cars.

        Returns:
            int: The total rental cost in dollars.
        """
        details = []
        no_of_cars = int(input("How many cars do you want to rent?"))
        for i in range(no_of_cars):
            details.append(CarRental.rent_car(self, cars))
        return details

    def single_rent(self, cars):
        """
        Rent a single car by calling the rent_car method.

        Args:
            cars (DataFrame): A DataFrame containing the available cars.

        Returns:
            int: The total rental cost in dollars.
        """
        amt = CarRental.rent_car(self, cars)
        input("Press Enter to Continue\n")
        system('cls')
        return amt

    def multi_rent(self, cars):
        """
        Rent multiple cars by calling the rent_multiple_car method.

        Args:
            cars (DataFrame): A DataFrame containing the available cars.

        Returns:
            int: The total rental cost in dollars.
        """
        amt = CarRental.rent_multiple_car(self, cars)
        system('cls')
        return amt

    def main_menu(self, cars):
        """
        Display the main menu and handle user selections.

        Args:
            cars (DataFrame): A DataFrame containing the available cars.

        Returns:
            None
        """
        display_names = ["Rent a single car", "Rent multiple car", "check list of cars", "Return car", "Exit"]
        amt = 0
        menu_items = dict(enumerate(display_names, start=1))

        while True:
            
            Utility.display_menu(menu_items)
            selection = int(input("Please enter your selection number: "))
            if selection == 1:
                amt = [CarRental.single_rent(self, cars)]
            elif selection == 2:
                amt = CarRental.multi_rent(self, cars)
            elif selection == 3:
                print(tabulate.tabulate(cars, headers='keys', tablefmt='psql'))
            elif selection == 4:
                CarRental.return_car(self, cars, amt)
            elif selection == 5:
                Utility.done()
            




