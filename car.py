# Define a class for my car
class Car(object):
    # implement the car object.

    def __init__(self, make=None, model=None, year=None, size=None,
                 body_type=None, door_no=None, capacity=None, engine=None,
                 transmition=None, colour=None, mileage=0, engine_size=None):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__size = size
        self.__body_type = body_type
        self.__door_no = door_no
        self.__capacity = capacity
        self.__engine = engine
        self.__transmition = transmition
        self.__colour = colour
        self.__mileage = mileage
        self.__engine_size = engine_size

        # TO DO: write GET and SET

    def getMake(self):
        return self.__make

    def getModel(self):
        return self.__model

    def getYear(self):
        return self.__year

    def getSize(self):
        return self.__size

    def getBodyType(self):
        return self.__body_type

    def getDoorNo(self):
        return self.__door_no

    def getCapacity(self):
        return self.__capacity

    def getEngine(self):
        return self.__engine

    def getTransmition(self):
        return self.__transmition

    def getColour(self):
        return self.__colour

    def getMileage(self):
        return self.__mileage

    def getEngineSize(self):
        return self.__engine_size

    def setColour(self, colour):
        self.__colour = colour

    def setMake(self, make):
        self.__make = make

    def setMileage(self, mileage):
        self.__mileage = mileage

    def setEngineSize(self, engine_size):
        self.__engine_size = engine_size

    def paint(self, colour):
        self.__colour = colour
        return self.__colour

    def move(self, distance):
        self.__mileage = self.__mileage + distance
        return self.__mileage

    def __str__(self):
        return "{0} {1} of {2} with {3} engine"\
            .format(self.__make, self.__model, self.__year, self.__engine)


class ElectricCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__numberFuelCells = 1

    def getNumberFuelCells(self):
        return self.__numberFuelCells

    def setNumberFuelCells(self, numberFuelCells):
        self.__numberFuelCells = numberFuelCells


class CarFleet(object):

    def __init__(self):
        self.__carsAvailable = []
        self.__carsRented = []
        self.__profit = 0.0

    def getProfit(self):
        return self.__profit

    def getNumAvailable(self):
        return len(self.__carsAvailable)

    def getNumRented(self):
        return len(self.__carsRented)

    def rentCar(self, index):
        if len(self.__carsAvailable) == 0:
            return "Sorry nothing to rent, please try again"

        if index < 0 or index >= len(self.__carsAvailable):
            return "Car not found!"

        car = self.__carsAvailable[index]
        rent_index = len(self.__carsRented)
        self.__carsAvailable.remove(car)
        self.__carsRented.append(car)

        self.__profit += 20

        # print('Car {0} rented with index: {1}'.format(car, rent_index))
        # print('Profit ' + str(self.__profit))
        # print('Now {0} cars available and {1} cars rented'.format(len(self.__carsAvailable), len(self.__carsRented)))

        return rent_index

    def returnCar(self, index):
        if index < 0 or index >= len(self.__carsRented):
            return "Car not found!"

        car = self.__carsRented[index]
        available_index = len(self.__carsAvailable)
        self.__carsRented.remove(car)
        self.__carsAvailable.append(car)

        # print('Car {0} returned, now available with index {1}'.format(car, available_index))
        # print('Now {0} cars available and {1} cars rented'.format(len(self.__carsAvailable), len(self.__carsRented)))
        return available_index

    def registerCar(self, car):
        self.__carsAvailable.append(car)

    def getAvailableCar(self, index):
        if index < 0 or index >= len(self.__carsAvailable):
            return "Car not found!"

        return self.__carsAvailable[index]

    def getRentedCar(self, index):
        if index < 0 or index >= len(self.__carsRented):
            return "Car not found!"

        return self.__carsRented[index]

    def __str__(self):
        return "Car Fleet, with {0} available cars and {1} rented"\
            .format(len(self.__carsAvailable), len(self.__carsRented))
