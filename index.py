# Made By: Sarthak Singhal - Year 1 - The Hong Kong University of Science and Technology
# Bachelor of Engineering
# Method Used: Recurssion and elimination
# Primary and the only Function as per requirement

def validate(array_nums, target_num, original_list):
    min_num = min(array_nums)  # find the minimum

    # print(min_num) Uncomment for debugging

    # Assumption: All numbers are whole numbers: i.e. including 0 but with no negative number in the array.

    # 3 Cases Available: -
    # 1. If the target number is in the array of integers.
    # 2. If the target number is less than the minimum number in the array of integers.
    # 3. If the target number is greater than the minimum number in the array of integers.

    # Case 1
    if target_num in array_nums:
        return "Solution: " + str(original_list.index(target_num))

    # Case 2
    elif target_num < min_num:
        return "No combination available"  # Recurssion Ender

    # Case 3
    elif target_num > min_num:
        residue = target_num - min_num
        # print(residue) Uncomment for debugging
        if residue in array_nums:
            # format output
            return "Solution [" + str(original_list.index(min_num)) + "," + str(original_list.index(residue)) + "]"
        else:
            array_nums.remove(min_num)  # eliminate
            # Recurse the validate function with minimum number removed.
            return validate(array_nums, target_num, original_list)


# Toggle between User and Sample Data: -

try:
    print("\n"*3 + "-- Press RETURN (Enter Key) on empty input to use sample data --" + "\n")
    array_nums = eval(input("Enter the integers in list form: "))
    target_num = int(input("Enter the target number: "))
    original_list = array_nums[:]

except:
    array_nums = [1, 2, 6, 3, 17, 82, 23, 234]
    target_num = 40
    original_list = array_nums[:]
    print("Array Used:", array_nums)
    print("Target Number:", target_num)

finally:
    print(validate(array_nums, target_num, original_list))
