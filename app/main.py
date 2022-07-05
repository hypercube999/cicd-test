from uvicorn import Server, Config

from app import app

Server(
    Config(
        app=app,
        host="0.0.0.0"
    )
).run()
