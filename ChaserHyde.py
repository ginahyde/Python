# program to create dictionary and tally bill for produce stand customer
import os, time

merch = {'key tag':4.99,'magnet':3.99,'tote bag':19.99,'cup':10.95,'decal':5.99,'pencil':.65,'coaster':.75}

def menu(): #created a function for my menu so I wouldn't have to copy and paste.
    print('\t***************************************')
    print('\t**        Chaser Merchandise         **')
    print('\t**                                   **')
    print('\t**  Item                      Price  **')
    print('\t**  key tag...................$4.99  **')
    print('\t**  magnet....................$3.99  **')
    print('\t**  tote bag..................$19.99 **')
    print('\t**  cup.......................$10.95 **')
    print('\t**  decal.....................$5.99  **')
    print('\t**  pencil....................$0.65  **')
    print('\t**  coaster...................$0.75  **')
    print('\t**                                   **')
    print('\t***************************************')

while True:    #outer loop for every customer
        
    #ask customer to begin order    
    name=input('What is your name?(enter "999" to end). ')

    if name=='999':
        break
    total=0
    
# begin tally of items to order
    
    while True:         #inner loop for items order per customer
        print('Please enter the Chaser Merchandise you would like to purchase. Enter blank to end order. ')
        items = input()
        if items == '':
            break
        
        if items in merch:
            print('That item will cost $ ', format(merch[items],'.2f'))
            qty = input('How many would you like to buy? ')
            total=total + merch[items]*int(qty)
            
        else:
            print('I do not have that item, ' + name)
            menu()
            continue


    trio= input(name + ', are you in the TRIO program(yes or no)? ')

    if trio=='yes':
        discount= total * .4
        triotot= total - discount
        print()
        print('Your TRIO discount: $' + str(format(discount, '.2f')))
        print()
        print('Your total after your TRIO discount: $' + str(format(triotot, '.2f')))
        print()
        tax1 = triotot * .07
        complete = triotot + tax1
        print(name + ', your total cost with TRIO discount and tax: $ ' + str(format(complete, '.2f')))
        print()
        
    if trio=='no':
        tax2=total *.07
        complete=total + tax2
        print()
        print( name + ', your total cost with tax: $ ' + str(format(complete, '.2f')))
        print()
        
    print ('Have a nice day')
    time.sleep(5)
    os.system('cls')





        
