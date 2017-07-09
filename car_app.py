try:
    import pandas
except ImportError:
    print("\nERROR: pandas lib not installed!\n Install it  by running 'pip install pandas'\n")

from car import Car, CarFleet, ElectricCar

car_fleet = CarFleet()
# car_fleet.rentCar(5)
# car_fleet.returnCar(2)
# car_fleet.returnCar(3)
try:
    data = pandas.read_csv('carstock.csv')

    # print("Filling cars fleet")
    for car_data in data.itertuples():
        # print car_data
        car = Car(car_data.Make, car_data.Model, car_data.Year, car_data.Size,
                  car_data.Body_Type, car_data.Door_No, car_data.Capacity,
                  car_data._8, car_data._9)

        car_fleet.registerCar(car)
except NameError as ex:
    print("\n")
    print("WARNING: pandas lib is required to load csv files")
    print("No car data was loaded!\n")
except Exception:
    print("\n")
    print("WARNING: carstock.csv not found.")

    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))

    print("Be sure to coping it in: " + dir_path + os.path.sep + "carstock.csv")
    print("No cars data was loaded!\n")

print("Welcome to RentACar. Edel here, how can i help you?\n")
user_opt = -1;
while user_opt != 9:
    print(car_fleet)
    user_opt = raw_input(
        "Commands: \n"
          "\t1 - rent a car\n"
          "\t2 - return a car\n"
          "\t3 - list cars available\n"
          "\t4 - list cars rented\n"
          "\t9 - exit\n")
    user_opt = int(user_opt)
    if user_opt == 1:
        index = raw_input("Enter a number of choice from the list 1-41. When you have made your choice input the number: ")
        index = int(index)
        result = car_fleet.rentCar(index)
        if type(result) is int:
            car = car_fleet.getRentedCar(result)
            print ("A {0}, nice choice!".format(car))
            print ("Your RentACar choice is {0}, enjoy.".format(result))
        else:
            print (result)
    elif user_opt == 2:
        index = raw_input("Enter car number from the list provided: ")
        index = int(index)
        result = car_fleet.rentCar(index)
        print ("Thanks.")
    elif user_opt == 3:
        print ("Cars available\n")
        for i in range(1, car_fleet.getNumAvailable()):
            car = car_fleet.getAvailableCar(i)
            print (car)
    elif user_opt == 4:
        print ("Cars rented\n")
        for i in range(0, car_fleet.getNumRented()):
            car = car_fleet.getRentedCar(i)
            print (car)

print("Have a nice day")

