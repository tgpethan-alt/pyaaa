print("Welcome to the Band name generator!")

# Overcomplicated functions to prevent blank names
def request_city():
    city = input("Enter your birth city:\n") # Request City
    if city == "":
        print("City cannot be blank!")
        return request_city() # City is blank, loop back and ask again
    else:
        return city

def request_pet_name():
    pet_name = input("Enter the name of one of your pets:\n") # Request pet name
    if pet_name == "":
        print("Pet name cannot be blank!")
        return request_pet_name() # Pet name is blank, loop back and ask again
    else:
        return pet_name

city = request_city()
pet_name = request_pet_name()

print("Your band name is: {0} {1}".format(city, pet_name))