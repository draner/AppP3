from flask import Flask, render_template, request, flash
import pickle

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'some_secret'
@app.route('/predict')

def index():
    flash("Inconnu")
    return render_template('index.html')

@app.route('/predicted', methods=['POST', 'GET'])
def predicted():
    if request.method == 'POST':
        energy = request.form['energy']
        fat = request.form['fat']
        saturated_fat = request.form['saturated-fat']
        carbohydrates = request.form['carbohydrates']
        sugars = request.form['sugars']
        proteins = request.form['proteins']
        salt = request.form['salt']
        flash(model.predict([[energy, fat, saturated_fat, carbohydrates, sugars, proteins, salt]]))
        return render_template('index.html')
