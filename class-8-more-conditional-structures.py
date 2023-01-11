#----- Exercise  2: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours

#----- Exercise  3: Rewrite your pay program usin try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program
    # Answer: 
inputHours = input('Enter Hours: ')
inputRate = input('Enter Rate: ')

try:
    floutHours = float( inputHours ) 
    floutRate = float( inputRate )
except:
    print('Error, please enter numeric input')
    quit()

if floutHours > 40 :
    print('Overtime')
    regularPay = floutRate * floutHours
    overtimePay = ( floutHours - 40.0 ) * ( floutRate * 0.5 )
    extraPay = regularPay + overtimePay
else:
    print('Regular')
    extraPay = floutHours * floutRate 
print('extra Pay:',extraPay)

# Output: 
    # Enter Hours: 40
    # Enter Rate: 10
    # Regular
    # extra Pay: 400.0

#----- Question: Given the following code:
temp = "5 degrees"
cel = 0
fahr = float(temp)
cel = (fahr - 32.0) * 5.0 / 9.0
print(cel)
# Which line/lines should be surrounded by try block?
    # Answer: 3,4