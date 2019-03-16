#define a variable f and it will open our data txt file for reading
f = open('data.txt', 'r')

#Then we're going to call the readlines() method and put that in the variable lines.
#the readlines() method put 1 string for each line, while the read () method put everythong in 1 string
#lines = f.readlines()
lines =f.read()

#We'll close our file handle 
f.close()

#and then we'll print the results to screen.
print(lines)
