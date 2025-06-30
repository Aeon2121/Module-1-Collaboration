'''
Gage Lipman
SDEV220 - M03 Lab Case Study
This program takes user input to create a vehicle type entry through the use of parent classes and attributes
'''
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

    def display_info(self):
        print(f"Vehicle type: {self.vehicle_type}")

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        # Initialize the parent class
        super().__init__(vehicle_type)
        # Initialize the attributes for the Automobile class
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_info(self):
        # Call the parent class's display_info method
        super().display_info()
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")

def main():
    # Accept user input
    print("Let's create your car!")

    vehicle_type = input("Enter the type of vehicle (car, truck, plane, boat, broomstick): ").lower()
    
    # Make sure the vehicle type is 'car'
    if vehicle_type != "car":
        print("This app only handles cars. Exiting...")
        return

    year = input("Enter the year of the car: ")
    make = input("Enter the make of the car: ")
    model = input("Enter the model of the car: ")
    doors = input("Enter the number of doors (2 or 4): ")
    
    # Validate doors input
    while doors not in ['2', '4']:
        print("Invalid input. Please enter 2 or 4 for the number of doors.")
        doors = input("Enter the number of doors (2 or 4): ")
    
    roof = input("Enter the type of roof (solid or sun roof): ").lower()

    # Validate roof input
    while roof not in ['solid', 'sun roof']:
        print("Invalid input. Please enter 'solid' or 'sun roof' for the type of roof.")
        roof = input("Enter the type of roof (solid or sun roof): ").lower()

    # Create an Automobile object
    car = Automobile(vehicle_type, year, make, model, doors, roof)

    # Display the car details
    print("\nHere is the information you entered:")
    car.display_info()

if __name__ == "__main__":
    main()
