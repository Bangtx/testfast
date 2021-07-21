from fastapi import FastAPI, Depends

app = FastAPI()

@app.get('/')
def getuser():
    return "ok"

