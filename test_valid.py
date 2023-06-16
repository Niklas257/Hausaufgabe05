from find_single_number import find_single_number


def test_valid():
    test_data = [20, 25, 40, 40, 20, 25, 8, 121, 34, 121, 34]
    assert find_single_number(test_data) == 8
