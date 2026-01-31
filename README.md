🏏 IPL Win Predictor API

A machine learning–powered REST API that predicts the probability of winning an IPL match in real time based on the current match situation.

The project is built using FastAPI, containerized with Docker, and deployed on AWS EC2, following production-style backend and ML engineering practices.

🚀 Tech Stack

Language: Python

Machine Learning: Logistic Regression

Backend Framework: FastAPI

Data Validation: Pydantic

Containerization: Docker

Deployment: AWS EC2

API Docs: Swagger (OpenAPI)

📌 Features

Predicts win probability using live match conditions

RESTful API with strict input validation

Normalized team and city names

Swagger UI for easy API testing

Dockerized for reproducible deployment

Cloud-hosted on AWS EC2

🏗 Project Structure
IPL Win predictor/
├── config/
│   └── team_map.py          # Team name normalization
├── model/
│   └── file.pkl             # Trained ML model
├── schema/
│   └── user_input.py        # Pydantic request schema
├── main.py                  # FastAPI application entry point
├── streamlit_app.py         # Optional UI client
├── Dockerfile
├── requirements.txt
└── IPL_win_predictor.ipynb  # Model training notebook

🔍 How It Works
1️⃣ Data Processing

Historical IPL match and ball-by-ball datasets were merged

Key features engineered:

Runs remaining

Wickets in hand

Overs completed

Target score

Team and city names normalized for consistency

2️⃣ Model Training

Logistic Regression model trained on engineered features

Model evaluated and serialized using pickle

Stored in model/file.pkl

3️⃣ API Prediction Flow

Client sends current match situation as JSON

Input validated using Pydantic schemas

Model returns winning probabilities for both teams

🔗 API Endpoints
✅ Health Check
GET /health


Response:

{
  "status": "ok"
}

🏏 Predict Match Outcome
POST /api/v1/predict


Request Body:

{
  "batting_team": "Royal Challengers Bangalore",
  "bowling_team": "Mumbai Indians",
  "city": "Mumbai",
  "target": 180,
  "score": 135,
  "over": 15.2,
  "wickets": 6
}


Response:

{
  "batting_team_win_probability": 0.71,
  "bowling_team_win_probability": 0.29
}

📘 Swagger API Documentation

After running the application, access Swagger UI at:

http://<EC2_PUBLIC_IP>:8000/docs

🐳 Run with Docker (Recommended)
Build Docker Image
docker build -t ipl-win-predictor .

Run Container
docker run -p 8000:8000 ipl-win-predictor

☁️ Deployment (AWS EC2)

Deployment steps:

Launch EC2 instance (Ubuntu)

Install Docker

Clone the repository

Build Docker image

Run container and expose port 8000 in security group

💻 Local Setup (Without Docker)
git clone https://github.com/Shehzad25/ipl-win-predictor.git
cd ipl-win-predictor
pip install -r requirements.txt
uvicorn main:app --reload

🔮 Future Improvements

Add venue and pitch conditions

Replace Logistic Regression with Gradient Boosting

Add CI/CD pipeline using GitHub Actions

Add request logging and monitoring

Secure endpoints with authentication

👤 Author

Shehzad Khan
Machine Learning & AI Engineer
GitHub: https://github.com/Shehzad25
