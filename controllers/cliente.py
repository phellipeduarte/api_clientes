from flask import request
from flask_restplus import Resource, fields

from models.cliente import ClienteModel
from schemas.cliente import ClienteSchema

from server.instance import server

cliente_ns = server.cliente_ns
cliente_schema = ClienteSchema()
cliente_list_schema = ClienteSchema(many=True)

CLIENTE_NAO_ENCONTRADO = "Cliente não encontrado"


def resposta_padrao(status_code, mensagem, error):
    return {"status": status_code, "mensagem": mensagem, "error": error}


item = cliente_ns.model(
    "Cliente",
    {
        "nome": fields.String(description="Nome do cliente"),
        "razao_social": fields.String(description="Razão social do cliente"),
        "cnpj": fields.String(description="CNPJ do cliente"),
        "data_inclusao": fields.Date(),
    },
)


class Cliente(Resource):
    def get(self, id):
        cliente_data = ClienteModel.find_by_id(id)

        if cliente_data:
            return (
                resposta_padrao(
                    200,
                    f"Cliente encontrado {cliente_schema.dump(cliente_data)}",
                    "null",
                ),
                200,
            )

        return (
            resposta_padrao(
                404,
                CLIENTE_NAO_ENCONTRADO,
                "Not found",
            ),
            404,
        )


class ClienteList(Resource):
    def get(self):
        return (
            resposta_padrao(
                200,
                f"Lista de clientes {cliente_list_schema.dump(ClienteModel.list_all())}",
                "null",
            ),
            200,
        )
