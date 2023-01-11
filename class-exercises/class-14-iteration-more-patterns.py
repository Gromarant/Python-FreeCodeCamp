#----- Exercise 1: Write a program which respeactly reads numbers until the user enters "done". Once "done" is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.
    # Answer: 
count : 0
sum: 0.0
while True:
    stringValue = input('Enter a number: ')
    if stringValue == 'done' :
        break
    try :
        floatNum = float(stringValue)
    except :
        print('Invalid input')
        continue
    print('Enter a number: ', floatNum)
    count += 1
    sum += floatNum
print('ALL DONE')
print(sum, count, sum/count)

# Output: 
    # Enter a number: 4
    # enter a number: 5
    # enter a number: bad Data
    # invalid input
    # enter a number: 7
    # enter a number: done
    # 16 3 5.333333333333333

#----- Question: Which of these evaluates to False?
    # Answer: 0 is 0.0