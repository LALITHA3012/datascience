from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/problems')
def problems():
    return render_template('problems.html')

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

@app.route('/market')
def market():
    return render_template('market.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    
    # Dummy AI model - random prediction based on inputs
    base_yield = random.uniform(2.5, 8.5)
    
    # Simple logic to adjust yield based on inputs
    if data['soil_type'] == 'fertile':
        base_yield *= 1.2
    elif data['soil_type'] == 'sandy':
        base_yield *= 0.8
    
    if float(data['temperature']) > 30:
        base_yield *= 0.9
    elif float(data['temperature']) < 15:
        base_yield *= 0.7
    
    if float(data['rainfall']) > 100:
        base_yield *= 1.1
    elif float(data['rainfall']) < 50:
        base_yield *= 0.8
    
    if data['fertilizer'] == 'organic':
        base_yield *= 1.15
    elif data['fertilizer'] == 'chemical':
        base_yield *= 1.05
    
    predicted_yield = round(base_yield, 2)
    
    return jsonify({
        'yield': predicted_yield,
        'crop': data['crop_type'],
        'confidence': random.randint(85, 95)
    })

if __name__ == '__main__':
    app.run(debug=True)
