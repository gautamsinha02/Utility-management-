import csv
import os


Sample_Space = open('test.csv', 'r')
Sample_Space_Reader = csv.DictReader(Sample_Space)
print("Bill Generation : ")
print("Enter the products to be added : ")
Bill_total = 0
while(1):
    print("Would you like to add something to the cart : ")
    print("Enter Y for Yes or N for NO : ")
    option = input()
    if(option == 'N'):
        print("Plastic bags (Rupees 5) ?")
        print("Enter Y for Yes or N for NO : ")
        Plastic_opt = input()
        if (Plastic_opt == 'Y'):
            Bill_total += 5
        break
    if(option == 'Y'):
        print("Product name : ")
        Product_name = input()
        for row in Sample_Space_Reader:
            if(row['product'] == Product_name):
                Bill_total += row['price']

print("Net total of the products purchased : ", Bill_total)
Sample_Space.close()