import utilities_sets
import utilities_dict


def main():
    pass


set1 = {"apple", "banana", "orange", "peach"}
set2 = {"banana", "pineapple", "peach", "watermelon"}

utilities_sets.get_total_items(set1)
utilities_sets.display_all_items(set1)
utilities_sets.add_item(set1)
utilities_sets.remove_item(set1)
utilities_sets.get_the_union_of(set1, set2)

# nested dictionaries for part b
this_dict = {"Ontario": {"capital": "Toronto", "largest": "Toronto", "population": "14734014"},
             "Quebec": {"capital": "Quebec City", "largest": "Montreal", "population": "8574571"},
             "Nova Scotia": {"capital": "Halifax", "largest": "Halifax", "population": "979351"},
             "New Brunswick": {"capital": "Fredericton", "largest": "Moncton", "population": "781476"},
             "Manitoba": {"capital": "Winnipeg", "largest": "Winnipeg", "population": "1379263"},
             "British Columbia": {"capital": "Victoria", "largest": "Vancouver", "population": "5147712"},
             "Prince Edward Island": {"capital": "Charlottetown", "largest": "Charlottetown", "population": "159625"},
             "Saskatchewan": {"capital": "Regina", "largest": "Saskatoon", "population": "1178681"},
             "Alberta": {"capital": "Edmonton", "largest": "Calgary", "population": "4421876"},
             "Newfoundland and Labrador": {"capital": "St. John's", "largest": "St. John's", "population": "522103"}

             }

# part b
utilities_dict.display_all(this_dict)
utilities_dict.get_capital_city()
utilities_dict.add_element()
utilities_dict.remove_item()

# part c
utilities_dict.get_another_capital_city()
utilities.dict.get_largest_city()
utilities.dict.get_smallest_province()
utilities.dict.get_largest_province()

if __name__ == '__main__':
    main()
