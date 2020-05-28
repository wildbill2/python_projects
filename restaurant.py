class Restaurant():
    """A class for describing a Restaurant."""

    def __init__(self, name, cuisine):
        """Initialize name and cuisine."""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        """Describes the restaurant with name and cuisine."""
        print("The name of this restaurant is " + self.name.title() + ".")
        print(self.name.title() + " serves " + self.cuisine + " food.")

    def open_restaurant(self):
        """Notifies that the restaurant is open."""
        print("The restaurant " + self.name.title() + " is open!")

    def get_number_served(self):
        """Get number of guests served"""
        print("The current number of guests served is " + str(self.number_served) + ".")

    def set_number_served(self, guests):
        """Update the number of guests served"""
        self.number_served = guests

    def increment_number_served(self, served):
        """Increases the number of guests served"""
        self.number_served += served


restaurant = Restaurant("popeyes", "fried")

restaurant.get_number_served()
restaurant.set_number_served(20)
restaurant.get_number_served()
restaurant.increment_number_served(150)
restaurant.get_number_served()






