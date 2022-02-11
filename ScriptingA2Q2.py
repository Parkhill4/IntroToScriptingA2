"""
        Question 2: This function will take two numbers from the user
                    and will return this function n!/(r!*(n-r)) that also
                    calculates the factorials of the numbers
"""
def calculations():
    n = int(input("Enter a number n: "))
    counter_n = 1
    result_n = 1
    while counter_n  <= n:
        result_n = result_n * counter_n
        counter_n += 1
    print(result_n)

    r = int(input("Enter a number r: "))
    counter_r = 1
    result_r = 1
    while counter_r  <= r:
        result_r = result_r * counter_r
        counter_r += 1
    print(result_r)

    j = n - r
    counter_j = 1
    result_j = 1
    while counter_j  <= j:
        result_j = result_j * counter_j
        counter_j += 1
    calculation1 = result_n/(result_r*(n-r))
    print("The result of n!/(r!*(n-r)): ")
    print(calculation1)

calculations()
