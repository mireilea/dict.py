def display_all(this_dict):
    for key, value in this_dict.items():
        if value == value:
            print(key, "is the capital city of", value)


def get_capital_city():

    province_name = this_dict.get('Manitoba')
    print(province_name)


def add_element():
    this_dict["Yukon"] = "White Horse"
    print(this_dict)


def remove_item():
    del this_dict['Ontario']
    print(this_dict)


def get_another_capital_city():

    province_name = this_dict.get('New Brunswick')
    print(province_name)


def get_largest_city():

    max_city = max(this_dict.items(), key=lambda item: int(item[1]["population"]))
    return max_city[1]["capital"]

# another code
# max(this_dict, key=lambda k: int(this_dict[k]["population"]))

def get_smallest_province():

    min_province = min(this_dict.items(), key=lambda item: int(item[1]["population"]))
    return min_province[1]["capital"]

def get_largest_province():

    max_province = max(this_dict.items(), key=lambda item: int(item[1]["population"]))
    return max_province[1]["capital"]





