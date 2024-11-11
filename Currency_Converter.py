from flask import Flask, render_template, request
app = Flask(__name__)

# Predefined exchange rates for simplicity
exchange_rates = {
    "USD": {"INR": 82.5, "EUR": 0.94, "RUB": 100.5},
    "INR": {"USD": 0.012, "EUR": 0.011, "RUB": 1.22},
    "EUR": {"USD": 1.06, "INR": 88.0, "RUB": 107.2},
    "PND": {"USD": 0.010, "INR": 0.82, "EUR": 0.0093},
    "YEN": {"USD": 0.010, "INR": 0.82, "EUR": 0.0093},
    "CAD": {"USD": 0.010, "INR": 0.82, "EUR": 0.0093},
}

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    from_currency = "USD"
    to_currency = "INR"
    amount = 1

    if request.method == "POST":
        from_currency = request.form["from_currency"]
        to_currency = request.form["to_currency"]
        amount = float(request.form["amount"])
        
        # Calculate converted amount
        if from_currency in exchange_rates and to_currency in exchange_rates[from_currency]:
            converted_amount = amount * exchange_rates[from_currency][to_currency]
            result = f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}"
        else:
            result = "Conversion rate not available."

    currencies = list(exchange_rates.keys())
    return render_template("index.html", currencies=currencies, result=result,
                           from_currency=from_currency, to_currency=to_currency, amount=amount)

if __name__ == "__main__":
    app.run(debug=True)