from find_single_number import find_single_number

def test_invalid_no_single():
    test_data = [7, 7, 7]
    assert find_single_number(test_data) == "Invalid Input"