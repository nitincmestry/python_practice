'''
Exercise 2: Print the sum of the current number and the previous number
Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.
'''

print("Printing current and previous number sum in a range(10)")
#initialize previous_num variable to 1st index value in range
previous_num = 0

for i in range(10):
    #sum of previous and current num
    x_sum = previous_num + i
    print("Current Number", i, "Previous Number", previous_num, "Sum:", x_sum)
    #once iterated change previous_num to current
    previous_num = i