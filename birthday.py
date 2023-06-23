"""
CSCI-141 Week 9: Dictionaries & Dataclasses
Homework: Birthday
Author: Johnathan Green
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class Birthday:
    month: str
    day: int
    year: int

def build_dictionary(filename):
    """
    Goes through a file and makes a object for the birthday class and adds it to a dictionary with the value of a count
    :param filename: The name of file that is going to be opened
    :return: a dictionary of all the birthdays with the count
    """
    with open(filename) as file:
        dict = {}
        for line in file:
            lst = line.split()
            birth = Birthday(lst[0], int(lst[1]), int(lst[2]))
            if birth in dict:
                dict[birth] += 1
            else:
                dict[birth] = 1
    return dict

def birthdays_atleast(bd_counts, min_count):
    """
    This function takes in the dictionary of birthdays and makes a list of all the birthdays greater than or eual to the min count
    :param bd_counts: the diction of birthdays
    :param min_count: the min number the birthday appears
    :return: a list of all the birthdays that satisfy the count
    """
    total_list = []
    for birth in bd_counts:
        if min_count <= bd_counts[birth]:
            total_list.append(birth)
    return total_list

def to_strings(list_birthdays):
    """
    This function takes in a list of the birthdays greater or equal than the count and returns a lsit of strings for the birthdays
    :param list_birthdays: The list of the items from the dictionary
    :return: a list of strings of the birthdays in numerical form
    """
    string_lst = []
    for i in list_birthdays:
        new_string = month_to_num(str(i.month)) + "/" + str(i.day) + '/' + str(i.year)
        string_lst.append(new_string)
    return string_lst

def month_to_num(month):
    """
    This function Takes in the three letter abrrivation of the month and returns the numerical value
    :param month: str
    :return: str
    """
    if month == 'JAN':
        return "1"
    elif month == 'FEB':
        return "2"
    elif month == 'MAR':
        return "3"
    elif month == 'APR':
        return "4"
    elif month == 'MAY':
        return "5"
    elif month == 'JUN':
        return '6'
    elif month =='JUL':
        return '7'
    elif month == 'AUG':
        return '8'
    elif month == 'SEP':
        return '9'
    elif month == 'OCT':
        return '10'
    elif month == 'NOV':
        return '11'
    else:
        return '12'

def main():
    dct = build_dictionary("birthday20000.txt")
    min_count = int(input("Enter a minimum count: "))
    a_list = birthdays_atleast(dct, min_count)
    print("Birthdays occurred at least " + str(min_count) + " times:")
    print(a_list)
    print()
    strings = to_strings(a_list)
    print(strings)

if __name__ == '__main__':
    main()
