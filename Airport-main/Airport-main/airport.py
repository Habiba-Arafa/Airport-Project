import haversine as hs

# get user data
while True:
    try:
        no_of_travellers_from_user = int(input("Please enter how many traveller: "))
        break
    except ValueError:
        print("Error!,Please enter number of traveller again.")
        continue

def passenger_data():
    file = open("user_data.txt", "+a")

    # checking if the input is an integer
    no_of_travellers_from_user

    # enter all names of passengers

    for i in range(0, no_of_travellers_from_user):
        passenger_name = input("Please enter name of passenge no " f"{ i + 1 } ")



    while True:
        try:
            phone_number = int(input("Please enter phone number "))
            break
        except ValueError:
            print("Error!,Please enter an integar phone number ")
            continue

    file.write("\n%s\t\t%s\t\t%s\t" % (passenger_name, phone_number, no_of_travellers_from_user))

    # return (passenger_name, phone_number , number_of_travellers)


passenger_data()


def read_airport():
    file = open("locations.txt", "r")
    all_data = []
    for line in file:
        vals = line.strip().split(",")
        # print(vals)
        x = dict(country_name=vals[0].lower(), airport_name= vals[1].lower(), x = vals[2], y = vals[3])
        all_data.append(x)
    return all_data



def getting_country1(all_data):
    flag = True
    while flag:
        input_country1 = input("please enter your departure country name ").lower()


        for i in range(len(all_data)):

            if input_country1 == all_data[i]["country_name"]:
                flag = False

    for i in range(len(all_data)):

        if input_country1 == all_data[i]["country_name"]:
            print( all_data[i]["airport_name"] )
    print("these are all " ,input_country1," avilabale airports choose one please")



user_airport1_data = []

def user_airport_1(all_data):
    flag = True
    while flag:
        user_airport1_input =input("please enter your departure country airport name " ).lower()

        for i in range(len(all_data)):

            if user_airport1_input == all_data[i]["airport_name"]:
                user_airport1_data.append(user_airport1_input)
                flag = False


    for i in range(len(all_data)):
        if user_airport1_input == all_data[i]["airport_name"]:
            print("you choose",user_airport1_input, "airport")
        user_airport1_data .append(user_airport1_input)

getting_country1(read_airport())
user_airport_1(read_airport())
# print(user_airport1_data)
user_airport1_data_given_to_function = user_airport1_data [0]

#first location from the user
def get_airport1(all_data  ):
    input_airport1 = user_airport1_data_given_to_function
    for i in range(len(all_data)):
        if all_data[i]["airport_name"]==input_airport1:

            return float(all_data[i]["x"]),float(all_data[i]["y"])
get_airport1(read_airport())
# second location from user
def getting_country2(all_data):
    flag = True
    while flag:
        input_country2 = input("please enter your Arrival country name ").lower()

        for i in range(len(all_data)):

            if input_country2 == all_data[i]["country_name"]:
                flag = False
        print("wroung country name please enter your country name corectly")
    for i in range(len(all_data)):

        if input_country2 == all_data[i]["country_name"]:
            print( all_data[i]["airport_name"])
    print("these are all " ,input_country2," avilabale airports choose one please")



# print(get_airport1(read_airport()))

getting_country2(read_airport())


user_airport2_data = []
def user_airport_2(all_data):
    flag = True
    while flag:
        user_airport2_input = input("please enter your departure country airport name ").lower()

        for i in range(len(all_data)):

            if user_airport2_input == all_data[i]["airport_name"]:
                user_airport1_data.append(user_airport2_input)
                flag = False

        if flag == True:
            print("wroung airport name please enter your  name corectly")
    for i in range(len(all_data)):
        if user_airport2_input == all_data[i]["airport_name"]:
            print("you choose", user_airport2_input, "airport")
        user_airport2_data.append(user_airport2_input)


user_airport_2(read_airport())
# print(user_airport2_data)
user_airport2_data_given_to_function = user_airport2_data[0]
# print(user_airport2_data_given_to_function)



#second location taken from the user
def get_airport2(all_data  ):
    input_airport2= user_airport2_data_given_to_function
    for i in range(len(all_data)):
        if all_data[i]["airport_name"]==input_airport2:
            return float(all_data[i]["x"]),float(all_data[i]["y"])



user_selected_flight_class = []


def class_type():
    while True:
        class_type = input(
            "please choose between economy or Business \n economy  \n Business + 2000 EGP to upgrade \n ").lower()
        if class_type == "business" or class_type == "economy":

            k = class_type .lower()
            user_selected_flight_class.append(k)

            break


        elif class_type != "business" or class_type != "economy":
            print("please choose between the 2 options")


class_type()

for_input_to_function = user_selected_flight_class[0]
# print(for_input_to_function)

list_of_choosen_meal_in_bussinees = []


def bussnies():
    z = for_input_to_function

    if z == "business":
        print(
            "oh you selected bussnies you will be charged 0.00 egp for any meal choose between meals from meal 1 to meal 3")
        print(" meal 1 : smoked salamon ")
        print(" meal 2 : steak ")
        print(" meal 3 : cordon blue")

        for i in range(0, no_of_travellers_from_user):

            while True:

                user_input = input("please enter traveler " f"{i + 1} meal is ")
                if  user_input == "meal 1" or user_input == "meal 2" or user_input == "meal 3":
                    list_of_choosen_meal_in_bussinees.append(user_input)
                    break
                else:
                    print("please leave a space between the meal and the number as displayed")

        # print(list_of_choosen_meal_in_bussinees)

list_of_choosen_meal_in_Economy = []

def economy():
    z = for_input_to_function

    if z == "economy":
        print(
            "oh you selected economy you will be charged 300 egp for any meal choose between meals from meal 1 to meal 3")


        print(" meal 1 : fish ")
        print(" meal 2 : meat ")
        print(" meal 3 : Chicken")

        for i in range(0, no_of_travellers_from_user):

            while True:

                user_input = input("please enter traveler " f"{i + 1} meal is ")
                if  user_input == "meal 1" or user_input == "meal 2" or user_input == "meal 3":
                    list_of_choosen_meal_in_Economy.append(user_input)
                    break
                else:
                    print("wrong input")

        # print(list_of_choosen_meal_in_Economy)


bussnies()
economy()


pearsons_who_willnot_travel = []
def see_if_user_is_vaccinated():
    for i in range(0, no_of_travellers_from_user):
        user_vaccinted = False
        while True:
            user_vaccinted = input("is passenger"f"{i + 1} vacinated enter yes if vaccinated and no for not vaccinated ")
            if user_vaccinted == "yes":
                print("passenger "f"{i + 1}  can travel ")
                user_vaccinted = True
                break
            elif user_vaccinted== "no":

                pearsons_who_willnot_travel . append("passenger"f"{i + 1} ")
                user_vaccinted = False
                break
            else:print("wrong input")

    # print(user_vaccinted)
have_health_problem = []
see_if_user_is_vaccinated()
def see_if_user_has_any_posbale_threat():


    for i in range(0, no_of_travellers_from_user):
        there_is_a_user_health_condition = False
        while True:
            there_is_a_user_health_condition = input("is passenger"f"{i + 1}  have any health condition enter yes if he/she has health problem and no for no health problem ")
            if there_is_a_user_health_condition == "yes":
                print("passenger "f"{i + 1}  can travel ")
                there_is_a_user_health_condition = True
                have_health_problem .append( "passenger " f"{i + 1} ")

                break
            elif there_is_a_user_health_condition== "no":
                print("passenger"f"{i + 1}  is elligabale to travel")
                there_is_a_user_health_condition = False
                break
            else:print("wrong input please choose between yes or no")
        # print(have_health_problem)
see_if_user_has_any_posbale_threat()

distance_of_flight = []

def get_the_distance_between_2points():
    distance = hs.haversine(get_airport1(read_airport()  ), get_airport2(read_airport())  )
    distance_of_flight .append(distance)
    return distance
get_the_distance_between_2points()

get_the_distance_between_2points()
# print(get_the_distance_between_2points())



for i in range(len(distance_of_flight)):
    distance_of_flight_in_int = distance_of_flight[0]


print( "your coverd distance is : ",distance_of_flight_in_int ,"km")


price_for_flight_in_global = []

def distance_prossecing():
    if distance_of_flight_in_int > 3000:
        price_for_flight_in_global.append(6.5)
    elif 2000<=distance_of_flight_in_int <=3000 :
        price_for_flight_in_global.append(9.6)
    elif distance_of_flight_in_int <1000:
        price_for_flight_in_global .append(12.8)
distance_prossecing()

for i in range(len(price_for_flight_in_global)):
    price_of_km = price_for_flight_in_global[0]
 # print(price_of_km)


def avg_price_of_flight():
    price= price_of_km * get_the_distance_between_2points()   #avarage price of km is 2.58

    return price.__floor__()

# print("your ticket price avg is",avg_price_of_flight(),"EGP")


# print(list_of_choosen_meal_in_bussinees)


def user_selection_calculationsif_bussines():
    bussnies_total = 0

    if 'business' in user_selected_flight_class:
        # print(user_selected_flight_class)
        # print(len(list_of_choosen_meal_in_Economy))
        bussnies_total = len(list_of_choosen_meal_in_bussinees) * 2000
        # print(economy_total)
    return bussnies_total

user_selection_calculationsif_bussines()

# print(list_of_choosen_meal_in_bussinees)
# print(len(list_of_choosen_meal_in_Economy))
def user_selection_calculationsif_economy():
    economy_total =0
    if 'economy' in user_selected_flight_class:
        # print(len(list_of_choosen_meal_in_Economy))
        economy_total = len(list_of_choosen_meal_in_Economy) * 300
        # print(economy_total)
    return economy_total



def after_avg_price_of_flight():
    if "economy" in user_selected_flight_class:

        print("your flight price covering the distance only is",avg_price_of_flight(),  "EGP" , "your meals price is" , user_selection_calculationsif_economy() , "for",no_of_travellers_from_user )
        new_priceof_economy = avg_price_of_flight() + user_selection_calculationsif_economy()
        print("your total trip price is " ,new_priceof_economy)
    elif "business" in user_selected_flight_class:
        print("your flight price covering the distance only is", avg_price_of_flight() , "EGP" ,"your meals price is free but you are charged for ",user_selection_calculationsif_bussines(),"for",no_of_travellers_from_user,"traveler")
        new_priceof_bussines = user_selection_calculationsif_bussines() + avg_price_of_flight()
        print("your total price of trip is ", new_priceof_bussines)
#
after_avg_price_of_flight()
