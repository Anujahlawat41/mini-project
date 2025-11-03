import requests

def currency_converter():
    print("💱 Currency Converter")
    from_curr = input("From currency (e.g., USD): ").upper()
    to_curr = input("To currency (e.g., INR): ").upper()
    amount = float(input("Enter amount: "))

    url = f"https://api.exchangerate.host/convert?from={from_curr}&to={to_curr}&amount={amount}"
    response = requests.get(url)
    data = response.json()

    if data.get("result"):
        print(f"{amount} {from_curr} = {data['result']} {to_curr}")
    else:
        print("Error fetching conversion rate.")

currency_converter()
