# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Assignment: Using Loops in Python
# author @pbarden
# 
# Instructions: You recently graduated college and you are applying for a
# programming job that requires the understanding of loops in Python. The
# manager you are interviewing with has asked you to take an assessment to
# prove your programming knowledge.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Take two integers from the user.
user_num_1 = int(input('Enter an integer value: '))
user_num_2 = int(input('Enter another integer value: '))

# Save the lower number as x; Save the largest integer as y.
if user_num_1 < user_num_2:
    x = user_num_1
    y = user_num_2
else:
    x = user_num_2
    y = user_num_1

print('Counting from x to y by 2:')
# Write a loop that counts from x to y by twos.
for n in range(x, y+1, 2):

    # Print out the values of that loop using the Print function in Python.
    print(n)

# Initialize z
z = int()

print('Sum of all previous values of x and y in each iteration:')
# Write another loop that adds x and y, and saves the value as Z.
for n in range(x, y+1, 2):

    # Sum of previous values at each iteration as it is being added by 2 (William Noffsinger, Personal Communication, 6/16/2019)
    z += n + y

    # Print out the values of Z using the Print function in Python.
    print(z)