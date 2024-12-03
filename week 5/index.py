# ACTIVITY 1
class Smartphone:
    """
    Represents a generic smartphone with basic attributes and methods.
    """
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def call(self, number):
        return f"{self.brand} {self.model} is calling {number}."

    def send_message(self, number, message):
        return f"Message to {number}: '{message}' sent from {self.brand} {self.model}."

class Smartwatch(Smartphone):
    """
    Represents a smartwatch, inheriting from Smartphone but with unique behavior.
    """
    def __init__(self, brand, model, price, strap_color):
        super().__init__(brand, model, price)
        self.strap_color = strap_color

    def track_steps(self, steps):
        return f"{self.brand} {self.model} tracked {steps} steps."

# Creating objects
phone = Smartphone("Apple", "iPhone 14", 999)
watch = Smartwatch("Samsung", "Galaxy Watch 5", 299, "Black")

# Using methods
print(phone.call("123-456-7890"))
print(phone.send_message("987-654-3210", "Hello!"))

print(watch.call("555-123-4567"))  # Inherited from Smartphone
print(watch.track_steps(5000))    # Unique to Smartwatch

# ACTIVITY 2
class Vehicle:
    """
    Base class for all vehicles.
    """
    def move(self):
        return "The vehicle is moving."

class Car(Vehicle):
    def move(self):
        return "The car is driving 🚗."

class Plane(Vehicle):
    def move(self):
        return "The plane is flying ✈️."

class Boat(Vehicle):
    def move(self):
        return "The boat is sailing 🚤."

# Using polymorphism
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    print(vehicle.move())
