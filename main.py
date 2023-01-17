import os
import uvicorn

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes.api import router as api_router

# from data.db_conn import init_connection  # MS SQL
from data import db_session
from data.users import User

app = FastAPI(title="MExcess")

origins = ['*']  # ["http://localhost:8008"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

app.mount("/static", StaticFiles(directory="static"), name="static")


def main():
    # init_connection('')
    db_exist = os.path.exists("db/excess_explorer.sqlite")
    db_session.global_init("db/excess_explorer.sqlite")

    with db_session.create_session() as session:
        pass


    uvicorn.run("main:app", host="0.0.0.0", port=8008,
                log_level="info", reload=True)
    print("running...")


if __name__ == '__main__':
    main()
