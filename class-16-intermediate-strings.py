#----- Exercise 6.5: Take the following Python code that storesa string:
str = 'X-DSPAM-Condidence: 0.8475 '
# Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number
    # Answer: 
pref = str.find(':')
suf = str[ pref+2: ]
numb = float(suf)

print(numb)

#----- Question: What is the value of i in the following code?
word = "bananana"
i = word.find("na")
    # Answer: 2