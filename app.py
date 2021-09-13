from ma import ma
from db import db

from server.instance import server

api = server.api
app = server.app

if __name__ == "__main__":
    db.init_app(app)
    ma.init_app(app)
    server.run()
