# Program for passsword generating

import random
from string import ascii_lowercase
from string import ascii_uppercase
from string import digits
from string import punctuation

class Password:
    def __init__(self):
        self.number = None
        self.length = None
        self.number_of_small_letters = None
        self.number_of_large_letters = None
        self.number_of_digits = None
        self.number_of_punctuations = None
        self.password_list = []


    def start(self):
        print("""This is a password generator, user can choose how many passwords needs to be generated, their length, a number
of uppercase letters, digits and punctuation symbols in each password. Remember that the sumeric number of uppercase
letters, digits and punctuation symbols can't be larger than the length of the passsword. The rest of the password
will be filled with lowercase letters\n""")
        self.basic_data()

    def basic_data(self):
        while True:
            # Number of passwords
            self.number = input("How many passwords needs to be generated? ")
            if self.number.isnumeric():
                break
            print("The input should be a number\n")

        while True:
            # length of each password
            self.length = input("How long these password should be? ")
            if self.length.isnumeric():
                print()
                break
            print("The input should be a number\n")


        print("""Do you want to specify the number of uppercase letters, digits and punctuation symbols? Remember that the
sumeric number of uppercase letters, digits and punctuation symbols can't be larger than the length of the passsword\n""")
        while True:
            decision = input("Input \"Yes\"  or \"No\": ").strip().title()
            if decision == "Yes":
                self.detail_data()
                break
            elif decision == "No":
                self.password_basic_create()
                break
            else:
                print("User needs to input \"Yes\"  or \"No\"\n")


    def detail_data(self):
        print("\nThis is a section in witch you can decine on a number of digits, \
punctuation symbols and uppercase letters. The rest of the password will be filled with lowercase letters")
        while True:
            while True:
                self.number_of_large_letters = input("Number of uppercase letters in each password: ")
                if self.number_of_large_letters.isnumeric():
                    break
                print("The input should be a number\n")
            while True:
                self.number_of_digits = input("Number of digits in each password: ")
                if self.number_of_digits.isnumeric():
                    break
                print("The input should be a number\n")
            while True:
                self.number_of_punctuations = input("Number of punctuation symbols in each password: ")
                if self.number_of_punctuations.isnumeric():
                    break
                print("The input should be a number\n")

            inputs = int(self.number_of_large_letters) + int(self.number_of_digits) + int(self.number_of_punctuations)
            self.number_of_small_letters = 0
            while inputs + self.number_of_small_letters < int(self.length):
                self.number_of_small_letters += 1

            if inputs < int(self.length):
                self.password_detail_create()
                break
            print("The number of uppercase letters, digits and punctuation symbols can't be larger than the length of the passsword\n")

    def password_basic_create(self):
        possibilities = [ascii_uppercase, ascii_lowercase, digits, punctuation]
        password = ""
        for i in range(int(self.number)):
            for j in range(int(self.length)):
                element_type = random.choice(possibilities)
                element = random.choice(element_type)
                password += element
            self.password_list.append(password)
            password = ""
        self.show()

    def password_detail_create(self):
        password = ""

        for i in range(int(self.number)):
            for element in range(int(self.number_of_large_letters)):
                element  = random.choice(ascii_uppercase)
                password += element
            for element in range(int(self.number_of_small_letters)):
                element  = random.choice(ascii_lowercase)
                password += element
            for element in range(int(self.number_of_digits)):
                element  = random.choice(digits)
                password += element
            for element in range(int(self.number_of_punctuations)):
                element  = random.choice(punctuation)
                password += element
            password = self.shuffle(password)
            self.password_list.append(password)
            password = ""
        self.show()

    def shuffle(self, password):
        temp_password = []
        password_shuffled = ""
        for i in password:
            temp_password.append(i)

        for i in password:
            element = random.choice(temp_password)
            password_shuffled += element
            temp_password.remove(element)
        return(password_shuffled)

    def show(self):
        i = 1
        print()
        for element in self.password_list:
            print(f"Password numer {i}: {element}")
            i += 1

first = Password()
first.start()