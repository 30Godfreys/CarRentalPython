"""Car rental unittests"""
import unittest
try:
    import pandas
except ImportError:
    print("ERROR: Pandas lib not installed!")

from car import Car, CarFleet, ElectricCar

class TestCar(unittest.TestCase):
    """Test Car and ElectricCar functionality"""
    def test_car_mileage(self):
        self.car = Car()
        self.assertEqual(0, self.car.getMileage())
        self.car.move(15)
        self.assertEqual(15, self.car.getMileage())
        self.car.setMileage(45)
        self.assertEqual(45, self.car.getMileage())

    def test_car_make(self):
        self.car = Car()
        self.assertEqual(None, self.car.getMake())
        self.car.setMake('Ferrari')
        self.assertEqual('Ferrari', self.car.getMake())

    def test_car_colour(self):
        self.car = Car()
        self.assertEqual(None, self.car.getColour())
        self.car.paint('red')
        self.assertEqual('red', self.car.getColour())
        self.car.setColour('yellow')
        self.assertEqual('yellow', self.car.getColour())

    def test_car_engine_size(self):
        self.car = Car()
        self.assertEqual(None, self.car.getEngineSize())
        self.car.setEngineSize('2.0tdi')
        self.assertEqual('2.0tdi', self.car.getEngineSize())

    def test_electric_car_fuel_cells(self):
        electric_car = ElectricCar()
        self.assertEqual(1, electric_car.getNumberFuelCells())
        electric_car.setNumberFuelCells(4)
        self.assertEqual(4, electric_car.getNumberFuelCells())


class TestCarFleet(unittest.TestCase):
    """Test car fleet functionality"""
    def setUp(self):
        """TestCarFleet setup"""
        try:
            self.__data = pandas.read_csv('carstock.csv')
            # print(self.__data)

            self.__car_fleet = CarFleet();

            # print("Filling cars fleet")
            for car_data in self.__data.itertuples():
                # print car_data
                car = Car(car_data.Make, car_data.Model, car_data.Year, car_data.Size,
                            car_data.Body_Type, car_data.Door_No, car_data.Capacity,
                            car_data._8 , car_data._9)

                self.assertEqual(car_data.Make, car.getMake())
                self.assertEqual(car_data.Model, car.getModel())
                self.assertEqual(car_data.Year, car.getYear())
                self.assertEqual(car_data.Size, car.getSize())
                self.assertEqual(car_data.Body_Type, car.getBodyType())
                self.assertEqual(car_data.Door_No, car.getDoorNo())
                self.assertEqual(car_data.Capacity, car.getCapacity())
                self.assertEqual(car_data._8, car.getEngine())
                self.assertEqual(car_data._9, car.getTransmition())

                fleet_size = self.__car_fleet.getNumAvailable();
                self.__car_fleet.registerCar(car)
                self.assertEquals(fleet_size + 1, self.__car_fleet.getNumAvailable())

        except NameError as ex:
            print("\n")
            print("WARNING: pandas lib is required to load csv files")
            print("no cars data will be loaded!\n")
        except Exception:
            print("\n")
            print("WARNING: carstock.csv not found.")

            import os
            dir_path = os.path.dirname(os.path.realpath(__file__))

            print(" Make sure to coping it in: " + dir_path + os.path.sep + "carstock.csv")
            print("no cars data was loaded!\n")

        # print(self.__car_fleet)

    def test_rent_return_one_car(self):
        """Rent and return one car"""
        available = self.__car_fleet.getNumAvailable();
        rented = self.__car_fleet.getNumRented();
        profit = self.__car_fleet.getProfit();
        rent_index = self.__car_fleet.rentCar(0)
        self.assertEqual(available - 1, self.__car_fleet.getNumAvailable())
        self.assertEqual(rented + 1, self.__car_fleet.getNumRented())

        self.assertEqual(profit + 20, self.__car_fleet.getProfit())

        self.__car_fleet.returnCar(rent_index);

        self.assertEqual(available, self.__car_fleet.getNumAvailable())
        self.assertEqual(rented, self.__car_fleet.getNumRented())

    def test_rent_all_cars(self):
        """Rent all cars and one more"""
        while self.__car_fleet.getNumAvailable() > 0:
            available = self.__car_fleet.getNumAvailable();
            rented = self.__car_fleet.getNumRented();
            profit = self.__car_fleet.getProfit();
            self.__car_fleet.rentCar(0)
            self.assertEqual(available - 1, self.__car_fleet.getNumAvailable())
            self.assertEqual(rented + 1, self.__car_fleet.getNumRented())

            self.assertEqual(profit + 20, self.__car_fleet.getProfit())

        # and one more
        result = self.__car_fleet.rentCar(0)
        # print (result)
        self.assertEqual("I'm Sorry We Have Nothing Let to rent, please try again in an hour. Have a nice day", result)


if __name__ == '__main__':
    unittest.main()