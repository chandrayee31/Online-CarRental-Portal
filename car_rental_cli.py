"""
1. Add a menu to a console application to manage activities.
2. Run a selected function.
3. Clear the output
4. Display the menu again or exit if done is selected
"""

import getpass
import os
from os import system   
from utils import Utility
from customer import Customer
import pandas as pd
import tabulate
import time

class CarRentalMain(object):
        def __init__(self):
            # Read the CSV file into a DataFrame
            df = pd.read_csv('data.csv')
            self.df=df

        def cust_login(self,cars):
            input("Enter Username:\t \033[1;33m")
            print("\033[1;32m")
            getpass.getpass(prompt="Enter Password: ",stream=None)
            Customer.cust_menu(self,cars)

 
def main():
    system('cls')
    rentalmain= CarRentalMain()
    utils= Utility()
    cars=utils.car_list(rentalmain)
    print("\033[1;32m")
    def print_logo(position):
        logo = r"""
        ____  _       _ _          ____                       _         
        / ___|| |_   _| | |_ ___   / ___| ___ _ __   ___  _ __| |_ _   _ 
        \___ \| | | | | | __/ _ \ | |  _ / _ \ '_ \ / _ \| '__| __| | | |
        ___) | | |_| | | ||  __/ | |_| |  __/ | | | (_) | |  | |_| |_| |
        |____/|_|\__,_|_|\__\___|  \____|\___|_| |_|\___/|_|   \__|\__, |
                                                                |___/ 

                ______
        __  __//  ||\ \      
        |  |/  //___||_\ \___
        |     //   _    _    |
        |__|\//|  | |  | |   |
                |__|_|__|_|__|

        """
        # Clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')
        # Print the car at the given position
        print(' ' * position + logo)
    
    for position in range(0, 10):
        print_logo(position)
        time.sleep(0.1)
    print("\033[2;32m Welcome to Online Car Rental Platform CLI")   
    print(" ")
    print("########################################################################################################") 
    # functions_names = { 1: Utility.car_list,2: rentalmain.cust_login ,3: Utility.done} 
    display_names = ["View list of Cars", "Customer Login","Exit" ]
            
    menu_items = dict(enumerate(display_names, start=1))

    while True:
            Utility.display_menu(menu_items)
            selection = int(input("Please enter your selection number: "))  # Get function key
            if selection == 1:
                print(tabulate.tabulate(cars, headers='keys', tablefmt='psql'))
            elif selection ==2:
                rentalmain.cust_login(cars)
            elif selection == 3:
                 Utility.done()
    

if __name__ == "__main__":
    main()