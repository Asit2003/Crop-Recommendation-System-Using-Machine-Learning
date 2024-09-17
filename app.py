from flask import Flask, request, render_template
import numpy as np
import pickle

# Load the pre-trained model and scalers
try:
    model = pickle.load(open('model.pkl', 'rb'))
    sc = pickle.load(open('standscaler.pkl', 'rb'))
    ms = pickle.load(open('minmaxscaler.pkl', 'rb'))
except FileNotFoundError as e:
    raise FileNotFoundError(f"Error loading model or scalers: {e}")

# Create a Flask app
app = Flask(__name__)

@app.route('/')
def index():
    # Render the main page
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predict():
    try:
        # Get input values from form
        N = float(request.form['Nitrogen'])
        P = float(request.form['Phosphorus'])
        K = float(request.form['Potassium'])
        temp = float(request.form['Temperature'])
        humidity = float(request.form['Humidity'])
        ph = float(request.form['Ph'])
        rainfall = float(request.form['Rainfall'])

        # Prepare the feature list for prediction
        feature_list = [N, P, K, temp, humidity, ph, rainfall]
        single_pred = np.array(feature_list).reshape(1, -1)

        # Scale the features
        scaled_features = ms.transform(single_pred)
        final_features = sc.transform(scaled_features)

        # Make a prediction
        prediction = model.predict(final_features)

        # Dictionary mapping prediction results to crop names
        crop_dict = {
            1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
            8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
            14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
            19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"
        }

        # Determine the crop and prepare the result
        crop = crop_dict.get(prediction[0], None)
        if crop:
            result = f"{crop} is the best crop to be cultivated right there."
        else:
            result = "Sorry, we could not determine the best crop to be cultivated with the provided data."

    except ValueError:
        # Handle invalid input error
        result = "Invalid input: Please ensure all fields are filled with numbers."
    except Exception as e:
        # General exception handling
        result = f"An error occurred: {e}"

    # Render the result on the main page
    return render_template('index.html', result=result)

if __name__ == "__main__":
    # Run the app in debug mode
    app.run(debug=True)
