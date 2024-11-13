import streamlit as st


def get_valid_input(prompt, min_value, max_value, value_type=float, key=None):
    value = st.number_input(
        prompt, min_value=min_value, max_value=max_value, value=0.0, format="%.2f", key=key
    )
    return value


def get_offer_details(offer_name, offer_key):
    st.write(f"Please provide the following for {offer_name}:")
    supply_rate = get_valid_input(
        "Enter Daily Supply rate (cents per day, 0-1000):", 0.0, 1000.0, key=f"supply_rate_{offer_key}"
    )
    usage_rate = get_valid_input(
        "Enter General Usage rate (cents per kWh, 0-100):", 0.0, 100.0, key=f"usage_rate_{offer_key}"
    )
    return supply_rate, usage_rate


def calculate_total_cost(supply_rate, usage_rate, avg_usage, month_length=31):
    supply_charges = supply_rate * month_length
    usage_charges = usage_rate * avg_usage
    return (supply_charges + usage_charges) / 100.0


def main():
    st.title("Energy Cost Comparison Tool")
    avg_usage = st.number_input(
        "Please enter avg. usage per month in kWh (can be a decimal value):",
        min_value=0.0,
        max_value=10000.0,
        value=0.0,
        format="%.2f",
        key="avg_usage",
    )

    supply_rate = []
    usage_rate = []

    # Collect details for Offer A and Offer B
    for idx, offer in enumerate(["Offer A", "Offer B"]):
        s_rate, u_rate = get_offer_details(offer, offer_key=idx)
        supply_rate.append(s_rate)
        usage_rate.append(u_rate)

    # Calculate total charges for each offer
    total_charges = [
        calculate_total_cost(supply_rate[i], usage_rate[i], avg_usage)
        for i in range(len(supply_rate))
    ]

    # Display results with zero padding
    st.write(f"Total charges for Offer A: ${total_charges[0]:.2f}")
    st.write(f"Total charges for Offer B: ${total_charges[1]:.2f}")


if __name__ == "__main__":
    main()
