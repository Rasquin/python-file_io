""" 
# Here a new file will be created. the w is fro write. 
f=open('newfile.txt', 'w')
f.write("Hello\n") #/n for new line
f.close()

#If we change the "w" for an "a"(apendice), it will add whatever your put on write to the newfile.txt already existing.
f=open('newfile.txt', 'a')
f.write("World")
f.close()
"""

f=open('newfile.txt', 'a')
lines=['Hello', 'World', 'Welcome', 'To', 'File IO']
text='\n'.join(lines)
f.writelines(text)
f.close()