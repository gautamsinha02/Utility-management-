import csv
import os
import prettytable


def Display():
#pt = PrettyTable()

#pt.setfiel
#def Display() :

#x = PrettyTable()
print("      ----------  Menu ---------- ")
print("\n\n1. Display all the products ")
print("2. Display specifics of a product")
#x.add_column ('Product Id', 'Product Name', 'Product Stock', 'Product Price')

print("Enter your option : ")
menu_option = input()

Sample_Space = open('test.csv', 'r')
Sample_Space_Reader = csv.DictReader(Sample_Space)

if(int(menu_option) == 1):
    keys = ('Product Id', 'Product Name', 'Product Stock', 'Product Price')
    #with open('test.csv', 'r') as Sample_Space:
     #   Sample_Space_Reader = csv.DictReader(Sample_Space)

      #  print("The products in the store are : ")
    #for k in Sample_Space_Reader.keys():
     #   print (k)
    print (keys)
    #len=0
    for row in Sample_Space_Reader :
        #print (row['id'],row['product'],row['stock'],row['price'])
        #print(Sample_Space.keys())
        #print(key)
        #print(row.keys())
        #print ('{:02x}'.format(row))
        print (row['id'] + ' ' + row['product'] + ' ' + row['stock'] + ' ' + row['price'])
        #x.add_row (row['id'], row['product'], row['stock'], row['price'])
        #if(int(row['id']) > int(len)):

elif(int(menu_option) == 2) :
    print("Enter product ID of the utility : ")
    Product_id = input()
    for row in Sample_Space_Reader:
        if(Product_id == row['id']):
            print("The name of the utility : ", row['product'])
            print("The remaining stock of the utility : ", row['stock'])
            print("The price of the utility is : ", row['price'])
            break

#print (x.get_string(start=0,end=int(len)))
Sample_Space.close()

