from flask import Flask, request, jsonify, redirect
from flask.logging import create_logger
import logging
from flasgger import Swagger

import pandas as pd
from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
Swagger(app)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)


def scale(payload):
    """Scales Payload"""
    
    LOG.info(f"Scaling Payload: \n{payload}")
    scaler = StandardScaler().fit(payload.astype(float))
    scaled_adhoc_predict = scaler.transform(payload.astype(float))
    return scaled_adhoc_predict

@app.route("/")
def home():
    """/ Route will redirect to API Docs: /apidocs"""

#    html = "<h3>Sklearn Prediction Home</h3>"
#    return html.format(format)
    return redirect("/apidocs")

@app.route("/predict", methods=['POST'])
def predict():
    """Performs an sklearn prediction using Boston Housing Price dataset
    ---
    consumes:
    - application/json
    parameters:
    - in: body
      name: payload
      description: JSON object 
      required: true
      schema:
            type: object
            properties:
                chas:
                    type: number
                    description: "Charles River dummy variable (1 if tract bounds river; else 0)"
                rm:
                    type: number
                    description: "Average number of rooms per dwelling"
                tax:
                    type: number
                    description: "Full-value property-tax rate per $10,000"
                ptratio:
                    type: number
                    description: "Pupil-teacher ratio by town"
                b:
                    type: number
                    description: "1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town"
                lstat:
                    type: number
                    description: "percent lower status of the population'"
    produces:
    - application/json
    responses:
        200:
            description: Ok
            schema:
                type: object
                properties:
                    prediction:
                        type: array
                        items:
                            type: number
        
    """
    
    # Logging the input payload
    json_payload = request.json
    LOG.info(f"JSON payload: \n{json_payload}")
    inference_payload = pd.DataFrame(json_payload)
    LOG.info(f"Inference payload DataFrame: \n{inference_payload}")
    # scale the input
    scaled_payload = scale(inference_payload)
    # get an output prediction from the pretrained model, clf
    prediction = list(clf.predict(scaled_payload))
    LOG.info(f"Prediction: {prediction}")
    return jsonify({'prediction': prediction})

if __name__ == "__main__":
    # load pretrained model as clf
    clf = joblib.load("./model_data/boston_housing_prediction.joblib")
    app.run(host='0.0.0.0', port=80, debug=True) # specify port=80
