from flask import Flask, Blueprint
from flask_restplus import Api

class Server:
    def __init__(self):
        self.app = Flask(__name__)
        self.blueprint = Blueprint("api", __name__, url_prefix="/api")
        self.api = Api(self.blueprint, doc="/doc", title="Flask-SQLAlchemy CRUD - Clientes")
        self.app.register_blueprint(self.blueprint)

        self.app.config[
            "SQLALCHEMY_DATABASE_URI"
        ] = "postgresql://phellipe:3010Phellipe@localhost:5400/clientes_db"
        self.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        self.app.config["PROPAGATE_EXCEPTIONS"] = True

        self.cliente_ns = self.cliente_ns()

    def cliente_ns(self):
        return self.api.namespace(name = "Clientes", description="Operações realizadas acerca de clientes", path="/")
    
    def run(self):
        self.app.run(
            port=5000,
            debug=True,
            host="0.0.0.0",
        )

server = Server()