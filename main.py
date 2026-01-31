from fastapi import FastAPI, HTTPException
import pandas as pd
import pickle
from schema.user_input import format_team,format_city,MatchInput 


with open("file.pkl", "rb") as f:
    pipe = pickle.load(f)

app = FastAPI(title="IPL Win Predictor API")



@app.get("/")
def root():
    return {"status": "IPL Win Predictor API running"}

@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(data: MatchInput):
    batting_team = format_team(data.batting_team)
    bowling_team = format_team(data.bowling_team)
    city = format_city(data.city)

    if batting_team == bowling_team:
        raise HTTPException(status_code=400, detail="Batting and bowling team cannot be same")

    runs_left = data.target - data.score
    balls_left = 120 - int(data.overs * 6)
    wickets_left = 10 - data.wickets

    if data.overs <= 0 or balls_left <= 0:
        raise HTTPException(status_code=400, detail="Invalid overs")

    crr = data.score / data.overs
    rrr = (runs_left * 6) / balls_left

    input_df = pd.DataFrame({
        "batting_team": [batting_team],
        "bowling_team": [bowling_team],
        "city": [city],
        "runs_left": [runs_left],
        "balls_left": [balls_left],
        "wickets": [wickets_left],
        "total_runs_x": [data.target],
        "crr": [crr],
        "rrr": [rrr]
    })

    proba = pipe.predict_proba(input_df)[0]

    return {
        "batting_team": batting_team,
        "bowling_team": bowling_team,
        "city": city,
        "win_probability": round(proba[1] * 100, 2),
        "loss_probability": round(proba[0] * 100, 2)
    }
