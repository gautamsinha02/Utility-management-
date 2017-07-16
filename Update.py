import csv
import os


def Update_Product():

    #opening file
    #@Sample_Space = open("test.csv", "r")
    #contents = csv.DictReader(Sample_Space)

    Sample_Space = open('test.csv', 'r')
    Sample_Space_Reader =  csv.DictReader(Sample_Space)
    Product = "dhal"
        #for row in contents:
        # if int(content['quantity']) > 100:
            #print(iterator("id"))

    print("Does the product exist? Enter y for yes or n for no ")
    opt = input();

    if(opt == 'y'):
            # updation of price
        print("Would you like to update the price? ")
        print("Enter Y for Yes or N for No ")
        option = input();
        if( option == 'Y' or option == 'y' ):
            print("Existing price : ")
            print(Sample_Space_Reader[Product]["price"])
            print("Enter the new price : ")
            opt = input();
            Sample_Space_Reader[Product]["price"] = opt
            Sample_Space_Writer = csv.DictWriter(open("test.csv", "w"))
            Sample_Space_Writer.writerow(Sample_Space)

            #updation of stock
            print("Would you like to update the stock ? ")
            print("Enter Y for Yes or N for No ")
            option = input()
            if (option == 'Y' or option == 'y'):

                option = input();
                if (option == 'Y' or option == 'y'):
                    print("Existing stock : ")
                    print(Sample_Space_Reader[Product]["stock"])
                    print("Enter the new stock : ")
                    opt = input();
                    Sample_Space_Reader[Product]["stock"] = opt
                    Sample_Space_Writer.writerow(Sample_Space)

    Sample_Space.close()
        #close whatever has to be closed


        #product is new, append
    if(opt == 'n'):
        Sample_Space = open('test.csv', 'r')
        print("Enter the ID of the stock : ")
        Product_Id = input();
        print("Enter product name : ")
        Product_name = input();
        print("Enter the stock of the product : ")
        Product_Stock = input();
        print("Enter the price of the product : ")
        Product_Price = input();

        New_row = {Product_Id, Product_name, Product_Stock, Product_Price}
        Sample_Space_Append = csv.writer(Sample_Space)

        Sample_Space_Append.write(New_row)
        Sample_Space.close()

