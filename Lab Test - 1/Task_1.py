def convert_currency():
    # Example exchange rates: 1 riyal = 23 INR
    exchange_rates = {
        ('riyal', 'indian rupees'): 23,
        ('indian rupees', 'riyal'): 1/23
    }

    amount = float(input("Enter the amount: "))
    from_currency = input("Enter the source currency (e.g., riyal): ").strip().lower()
    to_currency = input("Enter the target currency (e.g., indian rupees): ").strip().lower()

    key = (from_currency, to_currency)
    if key in exchange_rates:
        converted = amount * exchange_rates[key]
        print(f"{amount} {from_currency} = {converted} {to_currency}")
    else:
        print("Exchange rate not available for the given currencies.")

if __name__ == "__main__":
    convert_currency()