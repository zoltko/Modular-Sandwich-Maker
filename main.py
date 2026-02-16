import cashier
import data
from sandwich_maker import SandwichMaker
from cashier import Cashier
import sandwich_maker


def main():
    """
    Main function to run the Sandwich Maker Machine.
    """
    # Import resources and recipes from data module
    resources = data.resources
    recipes = data.recipes
    
    # Create instances of SandwichMaker and Cashier classes
    sandwich_maker_instance = sandwich_maker.SandwichMaker(resources)
    cashier_instance = cashier.Cashier()
    
    
    is_on = True
    
    print("=" * 50)
    print("welcome to the Sandwich Maker Machine!")
    print("=" * 50)
    
    while is_on:
        
        choice = input("\nwhat would you like? (small/medium/large/off/report): ").lower()
        
        if choice == "off":
            print("turning off the machine. goodbye!")
            is_on = False
        
        elif choice == "report":
           
            sandwich_maker_instance.show_resources()
        
        elif choice in recipes:
            
            sandwich = recipes[choice]
            
            
            if sandwich_maker_instance.check_resources(sandwich["ingredients"]):
                # Process payment
                print(f"\nThe cost of a {choice} sandwich is ${sandwich['cost']:.2f}")
                payment = cashier_instance.process_coins()
                
                
                if cashier_instance.transaction_result(payment, sandwich["cost"]):
                    # Make the sandwich
                    sandwich_maker_instance.make_sandwich(choice, sandwich["ingredients"])
        
        else:
            print("bad choice. Please select small, medium, large, report, or off.")


if __name__ == "__main__":
    main()
