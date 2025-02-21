import pytest
from product_module import add_product
from order_module import calculate_total_price

# Fixture for setting up test products
@pytest.fixture
def setup_products():
    # Adding some products to the inventory
    add_product(1, "Laptop", 1200)  # Laptop for 1200
    add_product(2, "Mouse", 20)     # Mouse for 20
    add_product(3, "Keyboard", 50)  # Keyboard for 50

# Test 1: Order without discount (Total price <= 500)
def test_order_without_discount(setup_products):
    order_items = [(2, 3)]  # 3x Mouse (20 * 3 = 60)
    total_price = calculate_total_price(order_items)
    assert total_price == 60  # No discount

# Test 2: Order with multiple products (Total price > 500 but <= 1000) and 5% discount
def test_order_with_multiple_products_5_percent_discount(setup_products):
    order_items = [(1, 1), (2, 2)]  # 1x Laptop (1200) + 2x Mouse (20 * 2 = 40) = 1240
    total_price = calculate_total_price(order_items)
    expected_price = 1240 * 0.95  # Applying 5% discount
    assert total_price == expected_price

# Test 3: Order with price exactly 500 (No discount)
def test_order_with_exactly_500(setup_products):
    order_items = [(2, 25)]  # 25x Mouse (20 * 25 = 500)
    total_price = calculate_total_price(order_items)
    assert total_price == 500  # No discount

# Test 4: Order with price exactly 1000 (5% discount should be applied)
def test_order_with_exactly_1000(setup_products):
    order_items = [(2, 50)]  # 50x Mouse (20 * 50 = 1000)
    total_price = calculate_total_price(order_items)
    expected_price = 1000 * 0.95  # Applying 5% discount
    assert total_price == expected_price

# Test 5: Order with price just over 1000 (10% discount should be applied)
def test_order_with_over_1000(setup_products):
    order_items = [(1, 1), (2, 1)]  # 1x Laptop (1200) + 1x Mouse (20) = 1220
    total_price = calculate_total_price(order_items)
    expected_price = 1220 * 0.9  # Applying 10% discount
    assert total_price == expected_price

# Test 6: Edge case with product prices near the discount thresholds
def test_edge_case_discount_thresholds(setup_products):
    # Test price just below 500 (no discount)
    order_items = [(2, 24)]  # 24x Mouse (20 * 24 = 480)
    total_price = calculate_total_price(order_items)
    assert total_price == 480  # No discount
    
    # Test price just above 500 (5% discount)
    order_items = [(2, 26)]  # 26x Mouse (20 * 26 = 520)
    total_price = calculate_total_price(order_items)
    expected_price = 520 * 0.95  # 5% discount
    assert total_price == expected_price

    # Test price exactly 1001 (10% discount)
    order_items = [(1, 1), (2, 1)]  # 1x Laptop (1200) + 1x Mouse (20) = 1220
    total_price = calculate_total_price(order_items)
    expected_price = 1220 * 0.9  # Applying 10% discount
    assert total_price == expected_price

# Test 7: Order with invalid product (non-existent product)
def test_order_with_invalid_product(setup_products):
    order_items = [(99, 1)]  # Non-existent product
    total_price = calculate_total_price(order_items)
    assert total_price == 0  # No such product, price should be 0
