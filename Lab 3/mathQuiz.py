from random import randint
# take user input for amt of questions
x = input("How many questions would you like to solve? ")
x = int(x)
# take user input for level
y = input("Would you like beginner, intermediate, or advanced questions? ")
y = y.upper()
# set correct = to zero
correct = 0
# create cylce to count to
for i in range(x):
    n1 = randint(1, 10)
    n2 = randint(1, 10)
    n3 = randint(1, 25)
    n4 = randint(1, 25)
    n5 = randint(1, 10)
    n6 = randint(1, 3)
# Start beginner loop
    if y == "BEGINNER":
        add = n1 + n2
        ans = input("What is %d + %d? " % (n1, n2))
        if int(ans) == add:
            print("That's right -- well done.\n")
            correct = correct + 1
        else:
            print("No, I'm afraid the answer is %d.\n" % add)
# start intermediate loop
    elif y == "INTERMEDIATE":
        prod = n3 * n4

        ans = input("What is %d * %d? " % (n3, n4))
        if int(ans) == prod:
            print("That's right -- Well done.\n")
            correct = correct + 1
        else:
            print("No, Im afraid the answer is %d.\n" % prod)
# start advanced loop
    elif y == "ADVANCED":
        exp = n5 ** n6
        ans = input("What is %d ** %d? " % (n5, n6))
        if int(ans) == exp:
            print("That's right -- Well done.\n")
            correct = correct + 1
        else:
            print("No, I'm afraid the answer is %d.\n" % exp)
    else:
        print("You didn't enter a valid parameter.")
# find out how many they got right.
if correct >= (2*x)/3:
    print("Well done!")
elif correct >= x/3:
    print("You need more practice!")
else:
    print("Please ask your math teacher for help!")
