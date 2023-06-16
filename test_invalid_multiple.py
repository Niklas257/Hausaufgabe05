from find_single_number import find_single_number


def test_invalid_multiple():
    test_data = [87, 87, 87, 87, 9]
    assert find_single_number(test_data) == "Invalid Input"
