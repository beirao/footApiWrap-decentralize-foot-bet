# Foot API wrap for [backend-decentralize-foot-bet](https://github.com/beirao/backend-decentralize-foot-bet)

## This FastAPI API implement [Uvicorn](https://www.uvicorn.org/) as WSGI server

## Input Params

- `matchId`: The ID of the match you want the winner.

## Output

```
SCHEDULED | IN GAME => 0
HOME WIN            => 1
AWAY WIN            => 2
DRAW                => 3
MATCH CANCELLED     => 4
```

```json
{
  "ret": OUT
}
```

## Install Locally

Install dependencies:

```bash
pip install -m requirements.txt
```

### Launch the API with this command :

```bash
uvicorn app.main:app --reload --factory
```

## All GET requests

### Get all deployed contract

```url
http://127.0.0.1:8000/{match_id}
```

# Docker

## Build

```bash
sudo docker build -t slim-ea-dbet .
```

## Create image

## Run image

```bash
sudo docker run -p 80:80 slim-ea-dbet
```

## Save the image

```bash
sudo docker save -o slim-ea-dbet.tar slim-ea-dbet
```
