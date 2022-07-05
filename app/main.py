from uvicorn import Server, Config

from app import app

Server(
    Config(app=app)
).run()
