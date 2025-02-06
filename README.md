IPL Win Predictor
This project uses machine learning to predict the winner of an IPL match. By analyzing historical match data, the model predicts match outcomes based on key statistics such as runs left, wickets remaining, current run rate (CRR), and required run rate (RRR).

The app is built using Streamlit to provide an interactive interface for real-time predictions.

Files in this repository:
app.py: Streamlit app to interactively predict the winner of an IPL match.
IPL_win_prediction.ipynb: Jupyter Notebook that explains and implements the model training process.
file.pkl: Pickled logistic regression model used for prediction.
How to Run the App:
Prerequisites:
Install the required dependencies:
bash
Copy
Edit
pip install -r requirements.txt
To run the Streamlit app:
Run the following command to start the Streamlit app:
bash
Copy
Edit
streamlit run app.py
Once the app is running, open the URL provided in the terminal (usually http://localhost:8501) to interact with the IPL win predictor.
How It Works:
Data Preprocessing:

Merged IPL match and delivery data.
Calculated key match statistics like runs left, wickets, CRR, and RRR.
Cleaned the data and applied one-hot encoding to categorical variables.
Model Training:

A logistic regression model was trained to predict the winner of a match based on the engineered features.
The model's performance was evaluated, and it was saved using pickle (file.pkl).
Streamlit App:

The app uses the trained model to predict the winner based on user input, including match details such as runs left, wickets, and overs remaining.
Project Setup:
Clone this repository to your local machine:

bash
Copy
Edit
git clone https://github.com/Shehzad25/ipl-win-predictor.git
