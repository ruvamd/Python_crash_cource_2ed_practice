class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        print(f'the restaurant name is {self.restaurant_name} and cuisine type is {self.cuisine_type}')

restaurant=Restaurant('la placinte','moldavian')
restaurant_n_two=Restaurant('burger king','impossible')
restaurant_n_three=Restaurant('mcdonald','big mac')

restaurant.describe_restaurant()
restaurant_n_two.describe_restaurant()
restaurant_n_three.describe_restaurant()