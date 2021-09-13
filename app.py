from ma import ma
from db import db

from server.instance import server

from controllers.cliente import Cliente, ClienteList

api = server.api
app = server.app


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Cliente, "/clientes/<int:id>")
api.add_resource(ClienteList, "/clientes")


if __name__ == "__main__":
    db.init_app(app)
    ma.init_app(app)
    server.run()
