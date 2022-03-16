
from flask import Flask, jsonify, request

from custom_exceptions.bad_account_info import BadAccountInfo
from custom_exceptions.id_not_found import IdNotFound
from dal_layer.account_dao.account_dao_imp import AccountDAOImp
from entities.account_class_information import Account
from service_layer.account_services.account_service_imp import AccountServiceImp


app: Flask = Flask(__name__)
Account_dao = AccountDAOImp()
account_service = AccountServiceImp(account_dao)

"""
To maintain a uniform interface, I will be using the path "/account" for all request to my application that have to do
with account data. I can use different verbs to determine WHAT I am doing with the account data, and that is how Flask 
will know what particular service method needs to be called
"""

@app.route("/accounts", methods=["POST"])
def create_account():
    try:
        account_data: dict = request.get_json()
        account = Account(account_data["accountId"], account_data["accountName"], account_data["City"])
        result = account_service.service_create_account(account)
        result_dictionary = result.convert_to_dictionary()
        result_json = jsonify(result_dictionary)
        return result_json, 201
    except BadAccountInfo as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400
    except IdNotFound as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400


@app.route("/accounts/<id>", methods=["GET"])
def get_account_by_id(id: str):
    try:
        result: Account = account_service.service_get_account_information_by_id(id)
        result_dictionary = result.convert_to_dictionary()
        return jsonify(result_dictionary), 200

    except BadAccountInfo as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400
    except IdNotFound as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400


app.run()