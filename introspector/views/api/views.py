# pylint: disable=missing-docstring
""" Views module
"""

import requests
from flask import (
    Blueprint,
    current_app,
    jsonify,
    request,
    Response,
    url_for,
)


BP = Blueprint('api', __name__, url_prefix='/api')


@BP.route('/introspect', methods=['POST'])
def api_fhir_metadata():
    fhir_base = current_app.config['API_SERVER']
    token = request.form['token']
    patient = request.form['patient']

    patient_fhir = requests.get(fhir_base + '/Patient/' + patient, headers={
        'Accept': 'application/fhir+json',
        'Authorization': 'Bearer ' + token
    })

    if patient_fhir.status_code == 200:
        return jsonify({
            'introspected': fhir_base,
            'active': True,
            'patient': patient
        })
    else:
        return jsonify({
            'introspected': fhir_base,
            'active': False
        })
