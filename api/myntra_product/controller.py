from shared.db import likeify

def query(model):
    product_id = model.get('id', None)
    brand = model.get('brand',None)
    gender = model.get('gender',None)
    price_floor = model.get('price_floor',None)
    price_ceil = model.get('price_ceil',None)
    search = model.get('search',None) # name and description

    q = ['SELECT * FROM myntra_products WHERE 1=1']
    p = []
    
    if product_id:
        q.append('AND ProductID = ?')
        p.append(product_id)
    else:
        if brand:
            q.append('OR LOWER(ProductBrand) LIKE ?')
            p.append(likeify(brand.lower()))
        if gender: 
            q.append('OR LOWER(Gender) LIKE ?')
            p.append(likeify(gender.lower()))
        if price_floor and isinstance(price_floor, int):
            q.append('OR LOWER(Gender) LIKE ?')
            p.append(likeify(gender.lower()))
