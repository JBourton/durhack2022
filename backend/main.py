import os
import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS

# <strong >  # Set up Flaskstrong>:
app = Flask(__name__)
# <strong >  # Set up Flask to bypass CORSstrong>:
cors = CORS(app)
# Create the receiver API POST endpoint:


@app.route("/receiver", methods=["POST"])
def postME():
    data = request.get_json()
    data = jsonify(data)
    return data


if __name__ == "__main__":
    app.run(debug=True)


os.chdir("./graphs")
data = pd.read_csv("SensorHistory - Co2-58c40226-37b7-4298-a148-9a95197ce399.txt",
                   skiprows=1, sep='\s+', header=None)
data = pd.DataFrame(data)
