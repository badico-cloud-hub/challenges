from flask import Blueprint, request, session
from challenge_b import app
from ..models import geo_model
import requests as req
import json
import datetime


geocoding = Blueprint('geocoding', __name__, url_prefix='/geo')

# utils
def join_and_replace_res(data: dict) -> str:
    txt = ','.join([str(e) for e in data.values()])
    return txt.replace(' ', '+')

def saveLatLongRes(content):
    content['created_at'] = str(datetime.datetime.utcnow())
    geo_model.create(content)
    
# routes
@geocoding.route('/get-latlong', methods=['POST'])
def getLatLongByAddress():
    body = json.loads(request.data)
    tr = join_and_replace_res(body)
    
    key = app.config['GOOGLE_API_KEY']
    
    payload = {'address':tr, 'key':key}

    res = req.get(app.config['GEOCODING_URI'], params=payload)
    content = json.loads(res.text)
    
    if content['status'] == 'OK':
        latlong = content['results'][0]['geometry']['location']
        
        body['lat'] = latlong['lat']
        body['lng'] = latlong['lng']
        saveLatLongRes(body)

        return latlong, 200
    
    return 'Google Geocoding API error', 400
