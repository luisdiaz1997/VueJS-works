from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("form.html")


@app.route("/form_data", methods=['GET', 'POST'])
def process_data():
    if request.method == 'POST':
        print("-----------------------------------------")
        print(request.form)
        data = request.form
        address_list = [data['street'], data['city'] ,data['state'], data['country'], data['area']]
        address = " ".join(address_list)
        address_q = "+".join(address.split())

        print(address)
        print(address_q)
        return render_template("validation2.html", result=data, address_q=address_q)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
