#!/usr/bin/python

def get_valid_input(prompt, min_value, max_value, value_type=float):
    while True:
        try:
            value = value_type(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Invalid input. Value must be between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_offer_details(offer_name):
    print(f"Please provide the following for {offer_name}:")
    supply_rate = get_valid_input("Enter Daily Supply rate (cents per day, 0-1000): ", 0, 1000)
    usage_rate = get_valid_input("Enter General Usage rate (cents per kWh, 0-100): ", 0, 100)
    print()
    return supply_rate, usage_rate


def calculate_total_cost(supply_rate, usage_rate, avg_usage, month_length=31):
    supply_charges = supply_rate * month_length
    usage_charges = usage_rate * avg_usage
    return (supply_charges + usage_charges) / 100.0


def main():
    avg_usage = get_valid_input(
        "Please enter avg. usage per month in kWh (can be a decimal value): ", 0, 10000, float)

    supply_rate = []
    usage_rate = []

    # Collect details for Offer A and Offer B
    for offer in ["Offer A", "Offer B"]:
        s_rate, u_rate = get_offer_details(offer)
        supply_rate.append(s_rate)
        usage_rate.append(u_rate)

    # Calculate total charges for each offer
    total_charges = [calculate_total_cost(supply_rate[i], usage_rate[i], avg_usage) for i in range(len(supply_rate))]

    # Display results
    print(f"Total charges for Offer A: ${round(total_charges[0], 2)}")
    print(f"Total charges for Offer B: ${round(total_charges[1], 2)}")


if __name__ == "__main__":
    main()
