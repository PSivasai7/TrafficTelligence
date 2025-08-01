import numpy as np
import pickle
import pandas as pd
from flask import Flask, request, render_template

app = Flask(__name__)

# Load model, scaler, and encoder
model = pickle.load(open('model.pkl', 'rb'))
scale = pickle.load(open('scale.pkl', 'rb'))
encoder = pickle.load(open('encoder.pkl', 'rb'))

# Mapping from integer option value in dropdown to holiday name used during training
holiday_mapping = {
    0: "Christmas Day",
    1: "Columbus Day",
    2: "New Years Day",
    3: "State Fair",
    4: "Martin Luther King Jr Day",
    5: "Memorial Day",
    8: "Labor Day",
    11: "Washingtons Birthday",
    12: "Independence Day",
    18: "Veterans Day",
    19: "Thanksgiving Day",
    7: "None"
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        fields = ['is_holiday', 'temp', 'rain', 'snow', 'weather', 'year', 'month', 'day', 'hours', 'minutes', 'seconds']
        input_values = [request.form.get(f) for f in fields]

        if not all(input_values) or any(v.strip() == "" for v in input_values):
            return render_template("index.html", prediction_text="❌ Please fill in all fields!")

        # Convert holiday integer value to string label
        holiday_label = request.form['is_holiday'].strip()
        valid_holidays = [
                "Christmas Day", "Columbus Day", "New Years Day", "State Fair",
                "Martin Luther King Jr Day", "Memorial Day", "Labor Day", 
                "Washingtons Birthday", "Independence Day", "Veterans Day", 
                "Thanksgiving Day", "None"
                    ]
        if holiday_label not in valid_holidays:
            return render_template("index.html", prediction_text="❌ Invalid holiday selected.")
        
        encoded_holiday = encoder.transform([[holiday_label]]).toarray()

        # Process other fields
        rest_features = [float(x) for x in input_values[1:]]
        rest_features_array = np.array(rest_features).reshape(1, -1)

        # Combine all features
        full_features = np.concatenate([encoded_holiday, rest_features_array], axis=1)
        scaled_features = scale.transform(full_features)

        prediction = model.predict(scaled_features)[0]
        return render_template("index.html", prediction_text=f"🚦 Estimated Traffic Volume: {int(prediction)} vehicles")

    except Exception as e:
        return render_template("index.html", prediction_text=f"❌ Error: {str(e)}")

if __name__ == "__main__":
    app.run(port=5000, debug=True, use_reloader=False)
