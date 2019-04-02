""" 
# Here a new file will be created. the w is for write. 
#The 'w'mode only allows you to write to a file and if that file doesn't exist, then a new one will be created. 
f=open('newfile.txt', 'w')
f.write("Hello\n") #/n for new line
f.close()

#If we change the "w" for an "a"(apendice), it will add whatever your put on write to the newfile.txt already existing.
# The 'a' allows you to append to a file, which means to write new content after the existing content. Again, if it doesn't exist a new file will be created. 
f=open('newfile.txt', 'a')
f.write("World")
f.close()
"""

f=open('newfile.txt', 'a')
lines=['Hello', 'World', 'Welcome', 'To', 'File IO']
text='\n'.join(lines)
f.writelines(text)
f.close()

"""
'r+' mode is for read and write. This allows you to read and write to a file. If it doesn't exist
it will throw an error. If it does exist, then its contents will be overwritten.

'w+' for read and write again is the same as 'r+', but a new file will be created if it
doesn't exist instead of an error being thrown. 

 'a+' is for read and append. This is the same as 'w+', but the file is opened for append, so the existing content won't
be overwritten. 

'rb', 'wb' and 'ab' are exactly the same as 'r', 'w' and 'a', but for binary data
instead of text. Now, you'll normally use 'r', 'w' and 'a', but since 'r' is used most
"""