han = open(r'file-path')

for line in han : 
    line = line.rstrip()
    words = line.split()
    if len(words) < 2 or words[0] != '#' :
        continue
    print( words[1] )


#----- Question: What does n equal in this code?
words = 'His e-mail is q-lar@freecodecamp.org'
pieces = words.split()
parts = pieces[3].split('-')
n = parts[1]
    # Answer: lar@freecodecamp.org