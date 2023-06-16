def find_single_number(data):
    single_num = ""
    if type(data) != list:
        return "Invalid Input"
    frequency = {}
    for num in data:
        if not isinstance(num, int):
            return "Invalid Input"
        frequency[num] = frequency.get(num, 0) + 1

    for num, count in frequency.items():
        if count == 1:
            single_num = num
        elif count > 2:
            return "Invalid Input"
    if single_num == "":
        return "Invalid Input"
    return single_num


if __name__ == "__main__":
    data = eval(input("List in form [x, y, z]: "))
    print("Single number in the list:", find_single_number(data))
