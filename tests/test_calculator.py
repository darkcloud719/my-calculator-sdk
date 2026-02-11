# import pytest
# from my_calculator import Calculator

# @pytest.fixture
# def calculator():
#     """Create a Calculator instance for testing."""
#     return Calculator()


# def test_add(calculator):
#     assert calculator.add(2, 3) == 5
#     assert calculator.add(-1, 1) == 0
#     assert calculator.add(0, 0) == 0

# def test_subtract(calculator):
#     assert calculator.subtract(5, 3) == 2
#     assert calculator.subtract(3, 5) == -2
#     assert calculator.subtract(0, 0) == 0

# def test_multiply(calculator):
#     assert calculator.multiply(2, 3) == 6
#     assert calculator.multiply(-2, 3) == -6
#     assert calculator.multiply(0, 10) == 0

# def test_divide(calculator):
#     assert calculator.divide(10, 2) == 5
#     assert calculator.divide(9, 3) == 3
#     assert calculator.divide(-6, 2) == -3

# def test_divide_by_zero(calculator):
#     with pytest.raises(ValueError, match="Cannot divide by zero"):
#         calculator.divide(10, 0)



import pytest
from my_calculator import Calculator

@pytest.fixture
def calculator():
    return Calculator()

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0)
])
def test_add(calculator, a, b, expected):
    assert calculator.add(a, b) == expected


@pytest.mark.parametrize("a, b, expected",[
    (5, 3, 2),
    (3, 5, -2),
    (0, 0, 0)
])
def test_subtract(calculator, a, b, expected):
    assert calculator.subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-2, 3 , -6),
    (0, 10, 0)
])
def test_multiply(calculator, a, b, expected):
    assert calculator.multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (9, 3, 3),
    (-6, 2, -3)
])
def test_divide(calculator, a, b, expected):
    assert calculator.divide(a, b) == expected

@pytest.mark.parametrize("a, b", [
    (10, 0),
    (5, 0),
    (0, 0)
])
def test_divide_by_zero(calculator, a, b):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(a, b)