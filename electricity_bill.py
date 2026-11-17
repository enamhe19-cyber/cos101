#Calculate a bill using fictional tiered classroom rates.
customer_name = input("Enter customer's name:")
energy_kwh = float(input("Enter energy consumed in kwh:"))
if energy_kwh < 0:
    print("invalid consumption. Energy cannot divude.")
else:
    if energy_kwh <= 50:
        bill = energy_kwh * 50
    elif energy_kwh <= 150:
        bill = (50 * 50) + ((energy_kwh - 50) * 75)
    else:
        bill = (
             (50 * 50)
             + (100 * 75)
             + ((energy_kwh - 150) * 100)
        )
    print()
    print("ELECTRICITY BILL")
    print("================")
    print(f"customer: {customer_name}")
    print(F"Energy consumed: {energy_kwh:.2f} kwh")
    print(f"Amount payable: NGN {bill:,.2f}")
    
