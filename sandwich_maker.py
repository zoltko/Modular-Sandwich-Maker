

class SandwichMaker:
   

    def __init__(self, resources):
       
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        #####
       
        for item, amount in ingredients.items():
            if self.machine_resources.get(item, 0) < amount:
                print(f"sorry, there is not enough {item}.")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        
        for item, amount in order_ingredients.items():
            self.machine_resources[item] -= amount
        print(f"{sandwich_size.capitalize()} sandwich is ready. enjoy!")

    def show_resources(self):
        
        print("\nCurrent resources:")
        for item, amount in self.machine_resources.items():
            print(f"{item.capitalize()}: {amount}")
        print()
