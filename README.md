## Crop Recommendation System 🌱

This is a web-based application that helps farmers and agricultural enthusiasts determine the best crop to cultivate based on specific environmental conditions. The application uses a machine learning model to predict the most suitable crop by considering factors such as Nitrogen, Phosphorus, Potassium levels, Temperature, Humidity, pH, and Rainfall.

### Features

- **User-Friendly Interface:** A clean and intuitive interface for entering environmental conditions.
- **Machine Learning Model:** Utilizes a pre-trained machine learning model for crop recommendation.
- **Real-Time Prediction:** Provides instant crop recommendations based on user input.
- **Scalable and Extendable:** Built using Python and Flask, making it easy to scale and extend.

### Technologies Used

- **Flask:** Python web framework for building the web server.
- **NumPy:** For numerical operations and data manipulation.
- **Scikit-Learn:** Machine learning library used to create and deploy the prediction model.
- **Bootstrap:** CSS framework for building a responsive and modern UI.
- **Jinja2:** Templating engine for rendering dynamic content on the web pages.
- **Pickle:** Used to load the pre-trained machine learning model and scalers.

### Prerequisites

Make sure you have the following installed on your system:

- Python 3.x
- Flask
- NumPy
- Scikit-Learn

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Asit2003/Crop-Recommendation-System-Using-Machine-Learning.git
   cd Crop-Recommendation-System-Using-Machine-Learning
   ```

2. **Install the required packages:**
- Python 3.x
- Flask
- NumPy
- Scikit-Learn

3. **Place the model files:**

   Make sure you have the following files in your project directory:
   - `model.pkl` - Pre-trained machine learning model.
   - `standscaler.pkl` - Standard scaler used for feature scaling.
   - `minmaxscaler.pkl` - MinMax scaler used for feature scaling.

4. **Run the Flask application:**
   ```bash
   python app.py
   ```

5. **Open the application in your web browser:**

   Visit `http://127.0.0.1:5000/` in your web browser to access the Crop Recommendation System.

### Usage

1. Enter the required environmental parameters:
   - **Nitrogen (N):** Amount of nitrogen in the soil.
   - **Phosphorus (P):** Amount of phosphorus in the soil.
   - **Potassium (K):** Amount of potassium in the soil.
   - **Temperature:** Current temperature in degrees Celsius.
   - **Humidity:** Humidity percentage.
   - **pH:** pH level of the soil.
   - **Rainfall:** Rainfall in millimeters.

2. Click on the **Get Recommendation** button.

3. The application will display the best crop to be cultivated under the given conditions.

### Project Structure

- `app.py`: Main Flask application file.
- `templates/index.html`: HTML template for the web interface.
- `model.pkl`, `standscaler.pkl`, `minmaxscaler.pkl`: Machine learning model and scalers.

### Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any suggestions or improvements.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

