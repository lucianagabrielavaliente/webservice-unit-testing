import os
from flask import Flask, request
from google.cloud import bigquery
from data_receiver import DataReceiver

app = Flask(__name__)

DATASET_ID = "someDataset"
TABLE_ID = "someTable"

@app.route('/receive', methods = ['POST'])
def start():
     #get request
    _data = request.form

    try:
        service = DataReceiver(DATASET_ID, TABLE_ID)
        # check validity
        service.check_validity(_data)

        # drop fields
        data = service.clean_up_data(_data)
        
        # write to big query
        errors = service.write(bigquery.Client(project="someProject"), data)

        if not errors:
            return "Success", 200
        return 500
    
    except Exception as e:
        return str(e), 500
    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
