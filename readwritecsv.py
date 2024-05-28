import csv

def writecsv(data):
    #data = ['john' ,14 ,500]
    with open('Test.csv' ,'a' ,newline='' ,encoding='utf-8') as file:
        #mode w = writerows a = append
        fw = csv.writer(file) # fw = file writer
        fw.writerow(data)

# ถ้า Error
# filename = 'D:\\Denchai users not delete and not move folder\\Desktop\\Python\\Test.csv'
# with open('Test.csv' ,'a' ,newline='' ,encoding='utf-8') as file:
       
def readcsv():
    with open('Test.csv' ,newline='' ,encoding='utf-8') as file:
        fr = csv.reader(file) # fw = file read
        data = list(fr)
        print(data)

readcsv()

# d = ['lisa' ,16 ,500]
# writecsv(d)