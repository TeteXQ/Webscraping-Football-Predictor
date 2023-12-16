from flask import Flask
from allpages import pages

# insert data for button "Home"

kraken = Flask(__name__)
kraken.register_blueprint(pages, url_prefix="/")


if __name__ =='__main__':
    kraken.run(debug=True)