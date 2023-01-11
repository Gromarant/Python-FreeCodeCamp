#----- Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a funtion called computepay which takes two parameters ( hours and rate)

# Output: 
    # Enter Hours: 45
    # Enter Rate: 10
    # pay: 475.0

    # Answer: 
def computepay( hours, rate ) :
    if hours > 40 :
        regPay = rate * hours 
        otp = ( hours - 40.0 ) * ( rate * 0.5 )
        pay = regPay + otp
    else : 
        pay = hours * rate
    return pay

hours = input( 'Enter Hours: ' )
rate = input( 'Enter Rate: ' )
floatHours = float( hours )
floatRate = float( rate )
extraPay = computepay( floatHours, floatRate )

print( 'Pay: ', extraPay )


#----- Question: What will the following Python program print out?:
def fred():
    print("Zap")

def jane():
    print("ABC")

jane()
fred()
jane()
    # Answer: 
        # ABC
        # Zap
        # ABC