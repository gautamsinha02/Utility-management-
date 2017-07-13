import csv
import os
import rando

def Add_New():

    #receive input
    print("Enter the name of the product to be added : ")
    NewProduct = input();
    print("The product to be added is : ", NewProduct)

    #ensure input is correct
    print("Enter C for Confirm or N for No : ")
    Raw = input();
    if( Raw != C ):
        print("Renter the name of the product to be added : ")
        NewProduct = input();

    #writing into file by invoking update function
    Update( NewProduct );

    #closing file
    Sample_Space.close()
    return;
