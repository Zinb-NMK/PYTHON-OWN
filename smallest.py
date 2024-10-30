# you are given a number N. Your task is to write a program that reads N inputs and 
# prints the smallest number of them after each input, each on a new line.

def small_num(n):
    smallest_num  = float('inf')#  Using float('inf') ensures any input will be smaller. 
    for _ in range(n):
        number = int(input())
        if number < smallest_num:
            smallest_num = number
        print(smallest_num)
n = int(input())
small_num(n)