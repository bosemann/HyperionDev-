# This is a program that continually asks a user to enter
# a number and once -1 has been entered the program stops and
# calculates the average of the numbers entered excluding the -1


# declare current number
CURRENT_NUM = 0
# declare counter
COUNTER = 0
# declare user input
USER_INPUT = 0

# while loop conditions
while USER_INPUT != -1:
    USER_INPUT = int(input("Enter a number "))
    CURRENT_NUM += USER_INPUT
    COUNTER += 1
# user enters -1 and average is calculated and printed
    if USER_INPUT == -1:
        average_num = (CURRENT_NUM + 1) / (COUNTER - 1)
        print("=========The average============")
        print(average_num)
