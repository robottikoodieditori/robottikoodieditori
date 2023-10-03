# Import flask and datetime module for showing date and time
import datetime
from flask import Flask, request
import json

import uselogomotion

x = datetime.datetime.now().strftime("%H:%M:%S")

# Initializing flask app
app = Flask(__name__)


# Route for seeing a data
@app.route('/data')
def get_time():

    # Returning an api for showing in  reactjs
    return {
        "Date": x,
    }


@app.route('/send/compiler', methods=['POST'])
def send_to_compiler():
    data = request.data
    data = data.decode('UTF-8').replace("'", '"')
    data = json.loads(data)
    #print(data['data'])
    #print(f"{data['data']}, | {str(data['data'])}")
    uselogomotion.main(data['data'], 'eetvartti/ompi')
    return data


# Running app
if __name__ == '__main__':
    app.run(debug=True)
