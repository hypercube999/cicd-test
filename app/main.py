import uvicorn

from app import app

uvicorn.run(app=app, host="0.0.0.0", port=8010)
