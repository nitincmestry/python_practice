'''
Exercise 1: Calculate the multiplication and sum of two numbers
Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
'''
# create function with 2 arguments and perform multiplication and sum operation
def mul_sum(num1, num2):
    product=num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2

result=mul_sum(20, 30)
print("The result is", result)

result=mul_sum(40, 30)
print("The result is", result)