
def get_total_items(set1):
    print(len(set1))


def display_all_items(set1):
    for items in set1:
        print(items, end=' ')
    print()


def add_item(set1):
    set1.add("cantaloupe")
    print("Added", set1)


def remove_item(set1):
    set1.remove("cantaloupe")
    print(set1)


def get_the_union_of(set1, set2):
    print(set1.union(set2))
