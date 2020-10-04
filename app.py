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
    """Performs an sklearn prediction


    POST /predict
    ---
    responses:
        200:
            description: Successful prediction
        
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
