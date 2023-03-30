from shared.connection import db

class MyntraProducts(db.Model):
    __tablename__ = 'myntra_products'

    product_id = db.Column(db.Integer, primary_key=True, nullable=False)
    product_name = db.Column(db.String, nullable=True)
    product_brand = db.Column(db.String, nullable=True)
    gender = db.Column(db.String, nullable=True)
    price = db.Column(db.Integer, nullable=True)
    num_images = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String, nullable=True)
    color = db.Column(db.String, nullable=True)

    def to_json(self):
        res = {}
        for k, v in self.__dict__.items():
            if k.startswith("_"):
                continue
            res[k] = v
        return res