class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        print(f'the restaurant name is {self.restaurant_name} and cuisine type is {self.cuisine_type}')

    def open_restaurant(self):
        print(f'the restaurant {self.restaurant_name} is open')