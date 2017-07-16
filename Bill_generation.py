import csv
import os

def Bill_Generation():
Sample_Space = open('test.csv', 'r')
Sample_Space_Reader = csv.DictReader(Sample_Space)
print("Bill Generation : ")
print("Enter the products to be added : ")
Bill_total = 0
flag = 0
cart = 0
#y or Y uodate
while(1):
    print("Would you like to add another utility to the cart : ")
    print("Enter Y for Yes or N for NO : ")
    option = input()
    if(option == 'N' or option == 'n'):
        if (cart != 0):
            print("Plastic bags (Rupees 5) ?")
            print("Enter Y for Yes or N for NO : ")
            Plastic_opt = input()
            if (Plastic_opt == 'Y' or Plastic_opt == 'y'):
                print("How many would you require : ")
                Plastic_quantity = input()
                Bill_total += (5*int(Plastic_quantity))
        break
    elif(option == 'Y' or option == 'y'):
        Sample_Space.seek(0,0)
        print("Product name : ")
        Product_name = input()
        for row in Sample_Space_Reader:
            if(row['product'] == Product_name):
                print("Enter the number of pieces bought : ")
                Product_quantity = input()
                Bill_total += int(row['price'])*int(Product_quantity)
                cart+=int(Product_quantity)
                flag = 1
        if (flag == 0):
            print("Product not available!")
    flag = 0
print("         --------- Bill ---------   ")
print("Total number of utilities bought : ", cart)
print("Net total of the products purchased : ", Bill_total)
Sample_Space.close()
