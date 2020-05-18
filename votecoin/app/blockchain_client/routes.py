from flask import Blueprint, render_template, jsonify
from app.blockchain_client.forms import WalletGeneratorForm
from app.blockchain_server.objects.Transaction import Transaction
import Crypto
import Crypto.Random
from Crypto.PublicKey import RSA
import binascii
import json


client = Blueprint("blockchain_client", __name__)


@client.route('/wallet_generator', methods=["GET", "POST"])
def wallet_generator():
    form = WalletGeneratorForm()
    # file_name = '../../blockchain_server/objects/candidates'
    #
    # with open(file_name) as json_file:
    #     json_contents = json.load(json_file)
    #     new_wallet = {
    #         'name': form.name.data,
    #         'address': form.address.data,
    #         'city': form.city.data,
    #         'state': form.state.data,
    #         'zip_code': form.zip_code.data,
    #         'country': form.country.data,
    #         'phone_number': form.phone_number.data,
    #         'email': form.email.data,
    #         'password': form.password.data
    #     }
    #
    #     # appending data to emp_details
    #     json_contents.append(new_wallet)
    #
    # with open(file_name,'w') as f:
    #     json.dump(json_contents, f, indent=4)

    return render_template("wallet_generator.html", form=form)


@client.route('/', methods=["GET", "POST"])
def generation_successful():
    return render_template('index.html')


@client.route('/cast_vote', methods=["GET", "POST"])
def cast_vote():
    return render_template("cast_vote.html", candidates=candidates)


@client.route('/vote_successful', methods=["GET", "POST"])
def vote_successful():
    pass


@client.route('/view_transaction', methods=["GET", "POST"])
def view_transaction():
    return render_template("view_transaction.html")


@client.route('/wallet/new', methods=["GET", "POST"])
def new_wallet():
    random_gen = Crypto.Random.new().read
    private_key = RSA.generate(1024, random_gen)
    public_key = private_key.publickey()
    response = {
        'private_key': binascii.hexlify(private_key.export_key(format('DER'))).decode('ascii'),
        'public_key': binascii.hexlify(public_key.export_key(format('DER'))).decode('ascii')
    }

    return jsonify(response), 200
