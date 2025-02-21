# main_app.py

from product_module import add_product
from order_module import calculate_total_price
from user_module import validate_user

def main():
    # Добавяне на продукти
    add_product(1, "Laptop", 1200)
    add_product(2, "Mouse", 20)

    # Валидиране на потребител
    if not validate_user("user@example.com", "password123"):
        print("Невалидни потребителски данни!")
        return

    # Създаване на поръчка
    order_items = [(1, 1), (2, 2)]  # 1x Laptop, 2x Mouse
    total_price = calculate_total_price(order_items)
    print(f"Обща цена на поръчката: ${total_price}")

if __name__ == "__main__":
    main()
