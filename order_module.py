from product_module import get_product
from disount_module import apply_discount
# order_module.py

from product_module import get_product

def calculate_total_price(order_items):
    """
    Изчислява общата цена на поръчка.
    order_items е списък от tuples (product_id, quantity).
    """
    total = 0
    for product_id, quantity in order_items:
        product = get_product(product_id)
        if product:
            total += product["price"] * quantity
    return apply_discount(total)
