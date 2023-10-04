#Create new file
f=open("test.txt","r")
f.write("Hello, I am writing this using open function in w(write) mode.")
f.write("\n Line2:Hello, I am writing this using open function in w(write) mode.")
print(f.readline())

z=open("numbers.txt","w")
for i in range(1,100):
    z.write(str(i)+ "\n")

#Open existing file for read purpose
f=open("test.txt","r")
file=f.read()
print(file)

f.close()  #close open files

# 'r' (Read Mode):
with open('example.txt', 'r') as file:
    content = file.read()

# 'w' (Write Mode):
with open('new_file.txt', 'w') as file:
    file.write('This is a new file.')

# 'a' (Append Mode);
with open('existing_file.txt', 'a') as file:
    file.write('Appending more data.')

# 'b' (Binary Mode):
#Used in conjunction with 'r', 'w', or 'a' to handle binary files like images, audio, etc.
#For example, 'rb' is read binary, 'wb' is write binary.
with open('image.jpg', 'rb') as binary_file:
    image_data = binary_file.read()

#'x' (Exclusive Creation Mode):
#Used for creating a new file but raises an error if the file already exists.
with open('new_file.txt', 'x') as file:
    file.write('This is a new exclusive file.')

# '+' (Read and Write Mode):
# Used in conjunction with 'r', 'w', or 'a' to open the file for both reading and writing.
with open('example.txt', 'r+') as file:
    content = file.read()
    file.write('Appending data to the file.')

# The with statement is used to ensure that the file is properly closed after reading.
