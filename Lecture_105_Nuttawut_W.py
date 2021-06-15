class Vehicle :
    license_nunber = ""
    serial_code = ""
    def turn_on_air (self) :
        print("Turn On : Air")

class Cars (Vehicle):
    pass

class PickUp (Vehicle):
    pass

class Van (Vehicle):
    pass

class EstateCars (Vehicle):
    pass

pickup_1 = PickUp()
car_1 = Cars()
van_1 = Van()
estatecar_1 = EstateCars()

pickup_1.turn_on_air()
car_1.turn_on_air()
van_1.turn_on_air()
estatecar_1.turn_on_air()
