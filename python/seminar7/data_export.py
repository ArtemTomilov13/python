def open_file(n):
    data = open('file.txt', 'w')
    data.writelines(n)
    data.close()

