#----- Exercise 1:  Write a program to read through a file and print the contents of the file ( line by line ) all in upper case.
    # Answer: 
file = open(r'C:\Users\maria\Desktop\Programming\Python\python-freeCodeCamp\clown.txt') 

# or: file = open('c:\\Users\\maria\\Desktop\\Programming\\Python\\python-freeCodeCamp\\clown.txt')

for lineX in file :
    lineX = lineX.rstrip();
    print(lineX.upper());

# Output: 
    # THE CLOWN RAN AFTER THE CAR AND THE CAR RAN INTO THE TENT AND THE TENT FELL DOWN ON THE CLOWN AND THE CAR
    

#----- Question: What does the word 'continue' do in the middle of a loop?
    # Answer: Skips to the next iteration of the loop.