# sum of the n first element of this series  x -  x**3/3! + x**5/5! - x**7/7!... for given x
# and display the detail of the series as string (displaying the value of each term of the series).


from math import factorial

x = int(input("Input the value of x: "))
n = int(input("Input the value of n: "))
output = str(x)
k = 3
s = int(x)

for i in range(1,n):
    sign = (-1)**i
    term = x ** k / factorial(k)
    element = " + " + str(round(abs(term), 2))
    if term*sign < 0 :
        element = " - " + str(round(abs(term),2))
    output += element
    s += term * sign
    k += 2
    
output += " = " + str(round(s,2))
print('The sum of the series are:')
print(output)

# Example of x = 7, n = 6:

Input the value of x: 7
Input the value of n: 6
The sum of the series are:
7 - 57.17 + 140.06 - 163.4 + 111.2 - 49.54 = -11.84
