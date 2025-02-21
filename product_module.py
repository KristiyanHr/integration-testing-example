# product_module.py

# База данни с продукти (речник)
products = {}

def add_product(product_id, name, price):
    """
    Добавя продукт в базата данни.
    """
    products[product_id] = {"name": name, "price": price}

def get_product(product_id):
    """
    Връща продукт по ID.
    """
    return products.get(product_id, None)
