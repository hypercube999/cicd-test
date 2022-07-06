import uvicorn

from app import app

import os
print(os.environ)

uvicorn.run(app=app, host="0.0.0.0", port=8000)
