"""
        Question 4: This program will take an array and create two new arrays
                    of the even and odd numbers of the array while calculating
                    the sum of all 3
"""

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
listEven = []
listOdd = []
num = 0
sum = 0
sumEven = 0
sumOdd = 0
for i in range (0, len(list)):
    sum = sum + list[i]
for num in range (0, len(list)):
    if list[num] % 2 == 0:
        listEven.append(list[num])
    else:
        listOdd.append(list[num])

for i in range (0, len(listEven)):
    sumEven = sumEven + listEven[i]

for i in range (0, len(listOdd)):
    sumOdd = sumOdd + listOdd[i]
print(list, "Sum of full array =",sum)
print(listEven, "Sum of even array =",sumEven)
print(listOdd, "Sum of odd array =",sumOdd)
