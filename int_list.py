# Take input of integers list
num_list = list(map(int, input("Enter a list of integers: ").split()))
# Sort the list
num_list.sort()
# Take input of a new number to add
new_num = int(input("Enter a new number to add: "))
# Find the sorted position for the new number
position = 0
while position < len(num_list) and new_num > num_list[position]:
    position += 1

# Insert the new number into the list at its sorted position
num_list.insert(position, new_num)

# Print the sorted list with the new number added
print("Sorted list with new number added:", num_list)
