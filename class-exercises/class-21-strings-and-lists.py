handle = open('mbox-short.txt')
print( handle )

for line in handle : 
    line = line.rstrip()
    words = line.split()
    if len(words) < 3 or words[0] != 'From' :
        continue
    print( words[2] )


#----- Question: What does n equal in this code?
words = 'His e-mail is q-lar@freecodecamp.org'
pieces = words.split()
parts = pieces[3].split('-')
n = parts[1]
    # Answer: lar@freecodecamp.org