"""
        Question 3: This program will take an array and sort it from
                    least to greatest
"""

List = [20, 68, 41, 88, 16, 40, 65, 97, 85]
Sorted = []

while List:
    min = List[0]
    for num in List:
        if num < min:
            min = num
    Sorted.append(min)
    List.remove(min)

print(Sorted)
