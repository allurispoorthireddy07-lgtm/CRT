#count even numbers using filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

#find second largest number using sorted()
numbers = [10, 20, 5, 15, 25]   
sorted_numbers = sorted(numbers, reverse=True)
second_largest = sorted_numbers[1]
print(second_largest)