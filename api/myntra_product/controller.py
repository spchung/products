from shared.db_helpers import likeify
from shared.connection import db
from .model import MyntraProducts

def get_product(id):
    row = db.session.query(MyntraProducts).filter(MyntraProducts.product_id == id).first()
    if not row:
        return None, 404
    return row.to_json()


def query_products(payload):
    query = db.session.query(MyntraProducts)
    for key in payload:
        if key.startswith('_') or payload[key] in ('', None, 'price'):
            continue

        query = query.filter(getattr(MyntraProducts, key).ilike(likeify(payload[key])))
    
    limit = payload.get('_limit', 20)
    offset = payload.get('_offset', 0)
    
    rows = query.offset(offset).limit(limit).all()
    return [row.to_json() for row in rows]

