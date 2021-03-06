#define a variable f and it will open our data txt file for (r)reading
# 'r' or read mode only allows you to read from a file and if it doesn't exist, then it will throw an error
#f = open('data.txt', 'r') ----> case data in the same directory
#f = open('data.txt', 'r') == f = open('data.txt') because it will open only to be read.
# relative path--> it identifies the location of the data file relative to the script that's currently running.
#f = open('files/relative_data.txt', 'r')

#absolute path---> starts at the very top of the file system. An absolute path is not relative to the running program but rather it's a fully formed path to a specific file. 
#PWD command---> Print Working Directory give you the absolute path
#readlink -f---> absolute path of an individual file using the readlink command here with the -f switch. readlink -f relative_data.txt.
f = open('/home/ubuntu/workspace/files/relative_data.txt', 'r')

#Then we're going to call the readlines() method and put that in the variable lines.
#the readlines() method put 1 string for each line, while the read () method put everythong in 1 string
#lines = f.readlines()
lines =f.read()

#We'll close our file handle 
f.close()

#and then we'll print the results to screen.
print(lines)


#seek(offset, from_where)
# The offset, we are already familiar with. from_where is: 0 (default) offset
# from the beginning of the file; 1 offset from the current file pointer or
# 2 offset from the end of the file. So seek(0,2) moves us to the end of the file
