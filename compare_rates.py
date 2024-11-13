#!/usr/bin/python


def main():

    avg_usage = int(input("Please enter avg. usage per month in kWh as a rounded number: "))

    print("Please provide following for Offer A : ")
    supply_rate = [float(input("Enter Daily Supply rate / day in cents: "))]
    gen_usage_rate = [float(input("Enter General Usage rate / kWh in cents: "))]

    print()

    print("Please provide following for Offer B : ")
    supply_rate.append(float(input("Enter Daily Supply rate / day in cents: ")))
    gen_usage_rate.append(float(input("Enter General Usage rate / kWh in cents: ")))

    print()

    for rate in supply_rate:
        if rate < 0 or rate > 1000:
            print(f"Invalid input {rate} , value must be between 0 and 1000")
            return

    for rate in gen_usage_rate:
        if rate < 0 or rate > 100:
            print(f"Invalid input {rate} , value must be between 0 and 100")
            return

    month_length = 31

    supply_charges = [rate * month_length for rate in supply_rate]
    gen_usage_charges = [rate * avg_usage for rate in gen_usage_rate]

    total_charges = [sum(t) / 100.0 for t in list(zip(supply_charges, gen_usage_charges))]

    print(f"Total charges for Offer A : ${round(total_charges[0], 2)}")
    print(f"Total charges for Offer B : ${round(total_charges[1], 2)}")


if __name__ == "__main__":
    main()
