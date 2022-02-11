"""
    Question 2: This program uses a loop to print out a star half triangle
                pattern and then prints another one facing the other direction
"""
def pattern1():
    for i in range(0, 5):
        for j in range(0, i + 1):
            print("* ", end = "")
        print("\n")
pattern1()

def pattern2():
    for i in range(0, 5):
        for j in range(1 , 5 - i):
            print(" ", end=" ")
        for n in range(0, i + 1):
            print("* ", end = "")
        print("\n")
pattern2()
