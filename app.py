from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load model and scaler
model = pickle.load(open('brute_force_detector.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        try:
            # Get form values and convert to float
            features = [
                float(request.form['Destination_Port']),
                float(request.form['Flow_Duration']),
                float(request.form['Total_Fwd_Packets']),
                float(request.form['Fwd_Packet_Length_Mean'])
            ]

            # Reshape and scale
            input_data = np.array(features).reshape(1, -1)
            input_scaled = scaler.transform(input_data)

            # Predict
            pred = model.predict(input_scaled)[0]
            prediction = "Brute Force Attack Detected!" if pred == 1 else "No Attack Detected"
        except Exception as e:
            prediction = f"Error: {str(e)}"
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
