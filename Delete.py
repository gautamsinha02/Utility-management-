import csv
import os

def Delete_Utility():
Sample_Space = open('test.csv', 'r')
Sample_Space_Reader = csv.reader(Sample_Space)


print ("Would you like to delete the utility using Product ID or Product name ?")
print("Enter 'ID' if you want to delete using ID or 'NAME' if you want to delete using Name : ")
Delete_var = input()

if(Delete_var == 'ID' or Delete_var == 'id'):
    print("Enter ID of the utility to be deleted: ")
    Product_id = input()

    for row in range(len(Sample_Space_Reader)):
        if(Product_id == row['id']):
            print("wowowow")
            del row
            #Delete_row = list(Sample_Space_Reader)[1:int(Product_id)]

            #for i in range(len(myList))
elif(Delete_var == 'NAME' or Delete_var == 'name'):
    print("Enter name of the utility to be deleted: ")
    Product_name = input()
    for row in range(len(Sample_Space_Reader)):
        if(Product_name == row['product']):
            del row
            #Delete_row = list(Sample_Space_Reader)[1:int(row['id'])]
else:
    print("Utility unidentified")
print("wowowwowo")
Sample_Space.seek(0,0)
for row in range(Sample_Space_Reader):
    #print(row['id'] + ' ' + row['product'] + ' ' + row['stock'] + ' ' + row['price'])
    print (row)







