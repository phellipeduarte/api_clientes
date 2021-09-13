from db import db


class ClienteModel(db.Model):
    __tablename__ = "clientes"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    razao_social = db.Column(db.String(150), nullable=False)
    cnpj = db.Column(db.String(14), nullable=False)
    data_inclusao = db.Column(db.DateTime, nullable=False)

    def __init__(self, nome, razao_social, cnpj, data_inclusao):
        self.nome = nome
        self.razao_social = razao_social
        self.cnpj = cnpj
        self.data_inclusao = data_inclusao

    def __repr__(self):
        return f"ClienteModel(nome = {self.nome}, razão social = {self.razao_social}, CNPJ = {self.cnpj}, data de inclusão = {self.data_inclusao}"

    def json(self):
        return {
            "nome": self.nome,
            "razao_social": self.razao_social,
            "cnpj": self.cnpj,
            "data_inclusao": self.data_inclusao,
        }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def list_all(cls):
        return cls.query.all()

    def save_cliente_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_cliente_from_db(self):
        db.session.delete(self)
        db.session.commit()
