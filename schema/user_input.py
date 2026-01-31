from pydantic import BaseModel,Field
from config.team_map import TEAM_MAP

def format_team(team: str) -> str:
    team = team.strip().lower()
    return TEAM_MAP.get(team, team.title())

def format_city(city: str) -> str:
    return city.strip().title()



class MatchInput(BaseModel):
    batting_team: str
    bowling_team: str
    city: str
    target: int = Field(..., gt=0)
    score: int = Field(..., ge=0)
    over: float = Field(..., ge=0, le=20)
    wickets: int = Field(..., ge=0, le=10)
