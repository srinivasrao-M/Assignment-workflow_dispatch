import os
nums = os.environ["number"]

num = int(nums)

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
