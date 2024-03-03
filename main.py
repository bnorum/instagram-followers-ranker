from followersgrab import getfollowers


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        print(left[left_index], "vs", right[right_index])
        choice = input(": ")
        if choice == '1':
            result.append(left[left_index])
            left_index += 1
        elif choice == '2':
            result.append(right[right_index])
            right_index += 1
            
    while left_index < len(left):
        result.append(left[left_index])
       
    
        left_index += 1
    
    while right_index < len(right):
        result.append(right[right_index])
        
    
        right_index += 1
    
    return result



def read_file(filename):
    with open(filename, "r") as file:
        lines = file.read().splitlines()
    return lines

getfollowers()
arr = [3, 6, 8, 10, 1, 2, 1]
filename = "followersunsorted.txt"
numbers = read_file(filename)
sorted_numbers = merge_sort(numbers)
output_filename = "followerssorted.txt"
print(sorted_numbers)
with open(output_filename, "w") as file:
    for number in sorted_numbers:
        file.write(str(number) + "\n")

