from fastapi import FastAPI
import routers.navwarnings
import routers.routeupload
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routers.navwarnings.router)
app.include_router(routers.routeupload.router)

if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=9000,reload=False)