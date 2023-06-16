from find_single_number import find_single_number

def test_invalid_list():
    test_data = {}
    assert find_single_number(test_data) == "Invalid Input"