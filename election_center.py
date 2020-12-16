from voters_info import Voter
import datetime
import sys
import os


def main():
    # Creating an empty dictionary
    my_dict = {"Name":[], "Age":[] }
    # Assigning variables

    # na 8umh8w na valw for loop edw

    name = input("Give your name:  ")
    age = input("Give your age: ")


    x = Voter(name, age)
    #new_list = [(k,v) for k,v in my_dict.items()]
    my_dict["Name"].append(name)
    my_dict["Age"].append(age)
    print(my_dict)
    """
    Here i am running eligibility
    """
    eligibility_name = x.name_eligibility()
    eligible_age = x.age_eligibility()

    print(eligible_age)
    file_name = 'voters_list.txt'

    # Trying to export to .txt or .csv file

    # f = open("file_name", "x")
    # for voterss in my_dict:
    #     f.write(voterss)
    # f.close


if __name__ == "__main__":
    main()


