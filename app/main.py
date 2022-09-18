from fastapi import FastAPI
from dotenv import load_dotenv
import requests
import json, os

def app():
    load_dotenv()
    app = FastAPI()


    # /**
    #  *  null = 0               // en jeu ou programmé
    #  * 'HOME_TEAM' = 1         // home gagne
    #  * 'AWAY_TEAM' = 2         // away gagne
    #  * 'DRAW' = 3              // égalité
    #  *  MATCH CANCELLED = 4    // match annulé
    #  */
    @app.get("/")
    def root():
        return {"Working": 1}

    @app.get('/{match_id}') # http://127.0.0.1:8000/match_id
    def main(match_id:int):
        try :
            url = f"https://api.football-data.org/v4/matches/{match_id}"
            res = requests.request("GET", url, headers={ "X-Auth-Token":os.getenv('FOOT_API_KEY')}, data={})
            data = json.loads(res.text)

            matchStatus = data["status"]
            matchScore = data["score"]["winner"]

            print("matchStatus",matchStatus)
            print("matchScore",matchScore)

            if(matchStatus == "TIMED" or matchStatus == "SCHEDULED" or matchStatus == "LIVE" or matchStatus == "IN_PLAY" or matchStatus == "PAUSED" ) :
                winnerId = 0
            elif(matchStatus == "FINISHED") :
                if (matchScore == "HOME_TEAM"):
                    winnerId = 1
                elif (matchScore == "AWAY_TEAM"):
                    winnerId = 2                
                elif (matchScore == "DRAW"):
                    winnerId = 3
                else:
                    winnerId = 4
            else :
                winnerId = 4    

        except Exception as e :
            winnerId = 4    

        finally :
            data = {'ret': winnerId}
            return(data)

    return app
