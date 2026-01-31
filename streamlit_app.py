import streamlit as st
import requests

API_URL = "http://16.171.140.102:8000/predict"  
# change to EC2 public IP later

teams = [
    'Sunrisers Hyderabad',
    'Mumbai Indians',
    'Royal Challengers Bangalore',
    'Kolkata Knight Riders',
    'Kings XI Punjab',
    'Chennai Super Kings',
    'Rajasthan Royals',
    'Delhi Capitals'
]

cities = [
    'Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
    'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
    'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
    'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
    'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
    'Sharjah', 'Mohali', 'Bengaluru'
]

st.title("🏏 IPL Win Predictor")

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox("Batting Team", sorted(teams))

with col2:
    bowling_team = st.selectbox("Bowling Team", sorted(teams))

city = st.selectbox("City", sorted(cities))
target = st.number_input("Target", min_value=1)

col3, col4, col5 = st.columns(3)

with col3:
    score = st.number_input("Current Score", min_value=0)

with col4:
    overs = st.number_input("Overs Completed", min_value=0.1)

with col5:
    wickets = st.number_input("Wickets Out", min_value=0, max_value=10)

if st.button("Predict Win Probability"):
    payload = {
        "batting_team": batting_team,
        "bowling_team": bowling_team,
        "city": city,
        "target": int(target),
        "score": int(score),
        "overs": float(overs),
        "wickets": int(wickets)
    }

    try:
        response = requests.post(API_URL, json=payload)
        result = response.json()

        if response.status_code == 200:
            st.success(f"{result['batting_team']} Win Probability: {result['win_probability']}%")
            st.error(f"{result['bowling_team']} Win Probability: {result['loss_probability']}%")
        else:
            st.warning(result["detail"])

    except Exception as e:
        st.error("FastAPI server not reachable")
