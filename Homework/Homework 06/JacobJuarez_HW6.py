# 1. Basic Lambda Function
even_or_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
print("Basic Lambda Function: ")
print(even_or_odd(4))  # Output: Even
print(even_or_odd(7))  # Output: Odd

# 2. Advanced Lambda Function
sum_of_list = lambda lst: sum(lst)
print("\nAdvanced Lambda Function: ")
print(sum_of_list([5, 6, 7, 8, 9, 10, 11])) # Sum is 56

# 3. Sorting with Lambda
list_of_tuples = [(1, 2, 3), (2, 7, 1),(5, 8, 4), (4, 6, 1)]
sorted_list = sorted(list_of_tuples, key=lambda x: x[2])    # Sort list by third element
print("\nSorting tuple list with lambda: ")
print(sorted_list)

# 4. Filtering with Lambda
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

filtered_triples = list(filter(lambda x: x % 3 == 0, numbers))
print("\nFiltering with Lambda (numbers divisible by 3): ")
print(filtered_triples)

# 5. Mapping with Lambda
cubed_numbers = list(map(lambda x: x ** 3, numbers))
print("\nMapping with /lambda (cubes): ")
print(cubed_numbers)

# 6. Reducing with Lambda
from functools import reduce

product_of_numbers = reduce(lambda x, y: x* y, numbers)
print("\nReducing with Lambda (product): ")
print(product_of_numbers)

# 7. Enumerate with or without Lambda
    #With Lambda
enumerated_list_lambda = list(map(lambda x: (x[0], x[1]), enumerate(numbers)))
print("\nEnumerate with Lambda: ")
print(enumerated_list_lambda)

    #Without Lambda
enumerated_list = list(enumerate(numbers))
print("\nEnumerate without Lambda: ")
print(enumerated_list)

# 8. Zip with or without Lambda
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']   
   
    #With Lambda
zipped_lists_lambda = list(map(lambda x: (x[0], x[1]), zip(list1, list2)))
print("\nZip with Lambda: ")
print(zipped_lists_lambda)

    #Without Lambda
zipped_lists = list(zip(list1, list2))
print("\nZip without Lambda: ")
print(zipped_lists)
