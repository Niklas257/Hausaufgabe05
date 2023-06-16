from find_single_number import find_single_number


def test_invalid_nums():
    test_data = [5.0, 7.0, 9.0, 9.0, 7.0]
    assert find_single_number(test_data) == "Invalid Input"
