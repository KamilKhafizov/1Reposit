numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

count_of_numbers = len(numbers)
first_part_of_numbers = numbers[0:4:1]
second_part_of_numbers = numbers[5:20:1]

sum_all_list = (sum(first_part_of_numbers) + sum(second_part_of_numbers))


numbers[4] = sum_all_list / count_of_numbers

print("Измененный список:", numbers)