import pytest
from pages.orders import OrderOperations

def test_orders(authenticate):
    o = OrderOperations(authenticate)
    o.orders()
    o.place_order()
    o.get_order_details()
    o.update_order()
    o.del_order()