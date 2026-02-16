

class Cashier:
   

    def __init__(self):
        """
        Initialize the Cashier.
        """
        pass

    def process_coins(self):
       
        print("Please insert coins.")
        try:
            large_dollars = int(input("How many large dollars ($1)?: "))
            half_dollars = int(input("How many half dollars ($0.50)?: "))
            quarters = int(input("How many quarters ($0.25)?: "))
            nickels = int(input("How many nickels ($0.05)?: "))
            
            total = (large_dollars * 1.0) + (half_dollars * 0.5) + (quarters * 0.25) + (nickels * 0.05)
            return round(total, 2)
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            return 0.0

    def transaction_result(self, coins, cost):
        
        if coins >= cost:
            change = round(coins - cost, 2)
            if change > 0:
                print(f"Here is ${change} in change.")
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False
