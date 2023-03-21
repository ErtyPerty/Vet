import csv
from datetime import date

# Define constants for VAT and formatting
VAT_RATE = 0.2
CURRENCY_SYMBOL = '£'
DECIMAL_PLACES = 2

# Define function to display stored transactions
def display_transactions():
    filename = "invoices.csv"
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        print(f"{' | '.join(headers)}")
        print("-" * 40)
        for row in reader:
            print(f"{' | '.join(row)}")

# Main loop
while True:
    # Display menu and get user input
    print("\nMenu:")
    print("1. Create invoice")
    print("2. Display stored transactions")
    print("3. Quit")
    choice = input("Enter your choice (1, 2, or 3): ")

    # Process user choice
    if choice == "1":
        # Get user input for client and pet information
        client_name = input("Client name: ")
        pet_name = input("Pet name: ")
        pet_type = input("Pet type: ")

        # Get chargeable items from user
        charges = []
        while True:
            item = input("Chargeable item (or enter to finish): ")
            if not item:
                break
            try:
                price = float(input("Price: "))
            except ValueError:
                print("Invalid price, please enter a number.")
                continue
            charges.append((item, price))

        # Calculate subtotal, VAT and total
        subtotal = sum(price for _, price in charges)
        vat = subtotal * VAT_RATE
        total = subtotal + vat

        # Display invoice
        print(f"\nInvoice for {client_name}'s {pet_type} {pet_name}:")
        print("=" * 40)
        print(f"{'Item':<30}{'Price':>10}")
        print("-" * 40)
        for item, price in charges:
            print(f"{item:<30}{CURRENCY_SYMBOL}{price:>10.{DECIMAL_PLACES}f}")
        print("-" * 40)
        print(f"{'Subtotal':<30}{CURRENCY_SYMBOL}{subtotal:>10.{DECIMAL_PLACES}f}")
        print(f"{'VAT (20%)':<30}{CURRENCY_SYMBOL}{vat:>10.{DECIMAL_PLACES}f}")
        print(f"{'Total':<30}{CURRENCY_SYMBOL}{total:>10.{DECIMAL_PLACES}f}")

        # Write data to CSV file
        today = date.today()
        filename = "invoices.csv"
        with open(filename, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([today.strftime('%Y-%m-%d'), client_name, subtotal, vat, total])
        print(f"\nInvoice saved to {filename}")
        
    elif choice == "2":
        display_transactions()
        
    elif choice == "3":
        break
        
    else:
        print("Invalid choice, please enter 1, 2, or 3.")
