from flask import Flask, request, jsonify
import util
app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'Locations': util.get_location_names()
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
    util.load_saved_artifacts()
    app.run(debug=True)