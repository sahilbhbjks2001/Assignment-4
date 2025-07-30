file = open('Sample.txt','r')
file1 = file.read()
print(file1)
file.close()
try:
    file2 = open('Sample1.txt','r')
    file3 = file2.read()
    print(file3)
    file2.close()
except:
    FileNotFoundError
finally:
    print("Error: The file 'Sample1.text' not found")