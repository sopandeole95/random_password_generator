import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



print("Welcome to the PyPassword Generator!")

nr_letters= int(input("How many letters would you like in your password?\n")) 

nr_symbols = int(input(f"How many symbols would you like?\n"))

nr_numbers = int(input(f"How many numbers would you like?\n"))



#Easy method

first = random.sample(letters,nr_letters)

second = random.sample(symbols,nr_symbols)

third = random.sample(numbers,nr_numbers)

easy_method = first+second+third



listToStr = ''.join(map(str, easy_method))

print(f"The easy password is {listToStr}")

print("------------------------------------------")





new_listtostr = str(listToStr)

def Convert(string):

    list1=[]

    list1[:0]=string

    return list1

latest = Convert(new_listtostr)



#-----------------------------------------------------------------

# Tough method

random.shuffle(latest)

toughstr = ''.join(map(str, latest))

print(f"The tough password is {toughstr}")