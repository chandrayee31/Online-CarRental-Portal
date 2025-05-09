import sys
import pandas as pd

class Utility(object):
    def __init__(self):
        """
        Initialize the Utility class.
        Reads the CSV file into a DataFrame.
        """
        df = pd.read_csv('data.csv')
        self.df=df

    def display_menu(menu):
        """
        Display a menu where the key identifies the name of a function.
        :param menu: dictionary, key identifies a value which is a function name
        :return: None
        """
        for k, function in menu.items():
            print(k, function)

    def done(): 
        """
        Display a farewell message and exit the program.
        """
        message = """
    Thank you for using our service
          Have a great day!
                    """
    
        border = '+' + '-' * 36 + '+'
        print(border)
        print('|' + ' ' * 36 + '|')
        print('|' + message.center(36) + '|')
        print('|' + ' ' * 36 + '|')
        print(border)
        sys.exit()
    

    def car_list(self,*args):
        """
        Update the 'available' column in the DataFrame and return it.
        :param args: list of arguments
        :return: DataFrame
        """
        args[0].df['available'] = args[0].df['available'].apply(lambda x: 'Available' if x else 'Not Available')
        return args[0].df
        

        
        
