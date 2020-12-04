# Write your function below:
def get_evens(my_list):
    even_elem = []
    for item in my_list:
        if item % 2 == 0:
            even_elem.append(my_list)
    return my_list


# This is some code you can use to test:

# Example 1, should print [6, 10[]
my_list = [6, 1, -1, 10]
result = get_evens(my_list)
print("Example 1:", result)

# Example 2, should print [-100, 500, 204, 213, -11, 240, 31]
my_list = [-100, 500, 204, 213, -11, 240, 31]
result = get_evens(my_list)
print("Example 2:", result)