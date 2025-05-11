import pytest
from booking import calc_price

@pytest.mark.parametrize("base,discount,count,expected", [
    (100.0, 0.1, 2, 180.0),
    (50.0, 0.2, 4, 160.0),
])
def test_calc_price_positive(base, discount, count, expected):
    assert calc_price(base, discount, count) == expected

@pytest.mark.parametrize("base,discount,count", [
    (-10.0, 0.1, 1),
    (100.0, -0.2, 2),
    (100.0, 1.5, 2),
    (100.0, 0.1, 0),
])
def test_calc_price_negative(base, discount, count):
    with pytest.raises(ValueError):
        calc_price(base, discount, count)