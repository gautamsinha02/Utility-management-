import csv
import os
import prettytable

#pt = PrettyTable()

#pt.setfiel
#def Display() :

#x = PrettyTable()

#x.add_column ('Product Id', 'Product Name', 'Product Stock', 'Product Price')
keys = ('Product Id', 'Product Name', 'Product Stock', 'Product Price')
Sample_Space = open('test.csv', 'r')
Sample_Space_Reader = csv.DictReader(Sample_Space)
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
    print (row['id'] + fill + row['product'] + ' ' + row['stock'] + ' ' + row['price'])
    #x.add_row (row['id'], row['product'], row['stock'], row['price'])
    #if(int(row['id']) > int(len)):


#print (x.get_string(start=0,end=int(len)))
Sample_Space.close()

