import re

DATA_REGEX = r"(mul\(\d{1,3},\d{1,3}\))"
MUL_REGEX = r"(?:mul\((\d{1,3}),(\d{1,3})\))"


def get_data():
    if TEST and PART_TWO: 
        path = "part_two_test_data.txt"
    elif TEST:
        path = "test_data.txt"
    else:
        path = "data.txt"
    print(f"opening: {path}")
    with open(path, 'r') as file:
        data = file.readlines()
    return data

def append_items_to_array(result: list, array: list) -> list:
    for item in array:
        result.append(item)
    return result
        
def print_array(array: list):
    for item in array:
        print(item)

def parse_raw_data(data) -> list:
    """Takes the raw data from the file and uses the DATA_REGEX to find all 
    occurances of the mul(YYY,ZZZ) character sequence

    Args:
        data (_type_): raw string data

    Returns:
        list: list of all occurances of mul(YYY,ZZZ)
        int: count of all occurances
    """
    mul_array: list = list()
    if PART_TWO:
        # Check the line string for different
        init_do = True
        for line in data:
            print(line)
            # print(line)
            # split line at the don't words
            donts = line.split("don't")
            print(("-"*40) + "split don'ts" +("-"*40))
            print_array(donts)
            print("-"*90)
            for element in donts:
                print(("-"*20) + "element" +("-"*20))
                if init_do:
                    print("init_do")
                    print(("-"*40) + "init do" +("-"*40))
                    print(element)
                    print("-"*90)
                    # parse line
                    result = re.findall(DATA_REGEX, element)
                    # print(result)
                    mul_array = append_items_to_array(mul_array, result)
                    # print(mul_array)
                    init_do = False
                else:
                    # split at do
                    dos = element.split("do()")
                    print(("-"*40) + "split dos" +("-"*40))
                    print_array(dos)
                    print("-"*90)
                    if len(dos) > 1:
                        for do in dos[1:]:
                            init_do = True
                            print(do)
                            result = re.findall(DATA_REGEX, do)
                            # print(result)
                            mul_array = append_items_to_array(mul_array, result)
                    # print(mul_array)
    else:
        for line in data:
            result = re.findall(DATA_REGEX, line)
            mul_array = append_items_to_array(mul_array, result)
            print(mul_array)
    return mul_array

def get_product(mul_item: str) -> int:
    temp_array = re.search(MUL_REGEX, mul_item)
    # print(f"{temp_array.group(1)},{temp_array.group(2)}")
    return (int(temp_array.group(1)) * int(temp_array.group(2)))

def sum_mul_array(mul_array: list) -> int:
    sum = 0
    for item in mul_array:
        sum = sum + get_product(item)
    return sum

TEST = False
PART_TWO = True


if __name__ == "__main__":
    raw_data = get_data()
    mul_array = parse_raw_data(raw_data)
    print(sum_mul_array(mul_array))
    