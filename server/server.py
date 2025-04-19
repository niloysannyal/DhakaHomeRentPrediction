from flask import Flask, request, jsonify
from flask import send_from_directory
from server import util
import os

util.load_saved_artifacts()
location_names = util.get_location_names()

client_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../client'))
app = Flask(__name__, static_folder=client_path, template_folder=client_path)

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(os.path.join(app.static_folder), filename)

@app.route('/')
def home():
    return app.send_static_file("app.html")

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'Locations': location_names
    })
    print(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_rent', methods=['POST'])
def predict_home_rent():
    Location = request.form['Location']
    Area_sqft = float(request.form['Area_sqft'])
    Bed = int(request.form['Bed'])
    Bath = int(request.form['Bath'])

    response = jsonify({
        'estimated_rent': util.get_estimated_rent(Location, Area_sqft, Bed, Bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    print("Starting Python Flask Server For House Rent Prediction...")
    app.run()
