from flask import Flask
from flask import render_template
from flask import request
import twocheckout
from twocheckout import TwocheckoutError

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/order', methods=['POST'])
def order():
    # Setup credentials and environment
    twocheckout.Api.auth_credentials({
        'private_key': 'sandbox-private-key',
        'seller_id': 'sandbox-seller-id',
        'mode': 'sandbox'
    })

    # Setup arguments for authorization request
    args = {
        'merchantOrderId': '123',
        'token': request.form["token"],
        'currency': 'USD',
        'total': '1.00',
        'billingAddr': {
            'name': 'Testing Tester',
            'addrLine1': '123 Test St',
            'city': 'Columbus',
            'state': 'OH',
            'zipCode': '43123',
            'country': 'USA',
            'email': 'example@2co.com',
            'phoneNumber': '555-555-5555'
        }
    }

    # Make authorization request
    try:
        result = twocheckout.Charge.authorize(args)
        return result.responseMsg
    except TwocheckoutError as error:
        return error.msg


if __name__ == '__main__':
    app.run()
