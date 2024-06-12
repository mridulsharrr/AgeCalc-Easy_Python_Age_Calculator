#import
import datetime

def main():
    #variables
    current_year = datetime.date.today().year
    #input
    birth_year = int(input("What s your birth year? "))

    print("As of Year" , current_year)
    age = current_year - birth_year
    print("Your age is:" , age)

main()