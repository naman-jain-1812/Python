try:
    file = open('newfile.txt','r')
    print('Reading file content:')
    reading_file1 = file.readline()
    print ("Line1: ",reading_file1)
    reading_file2 = file.readline()
    print ("Line2: ",reading_file2)
    file.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")