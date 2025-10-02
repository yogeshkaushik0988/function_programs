data = [('apple', 3), ('banana', 1), ('cherry', 5), ('date', 2)]

# Using lambda with map to square numbers in a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(f"Squared numbers: {squared_numbers}")

# Using lambda with filter to get even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

# Using lambda with sorted to sort a list of tuples by the second element
sorted_data = sorted(data, key=lambda item: item[1])
print(f"Sorted data by value: {sorted_data}")