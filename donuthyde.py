#Program checks customer order with dictionary, adds order to a list, and totals list and adds in .09% tax.
import time
import os
bfast={'Speciality Donut':1.50,'Bagel':3.15,'Croissant':2.98,'English Muffin':1.75,'Coffee':2.99,'Juice':1.99}
total=0.0
tax=0.0
cust_order=[]
cost=0.0
def menu(): #created a function for my menu so I wouldn't have to copy and paste.
    print('\t***************************************')
    print('\t**    Welcome to SCC Student Hub     **')
    print('\t**                                   **')
    print('\t**          Breakfast Items          **')
    print('\t**                                   **')
    print('\t**  Item                      Price  **')
    print('\t**  Speciality Donut..........$1.50  **')
    print('\t**  Bagel.....................$3.15  **')
    print('\t**  Croissant.................$2.98  **')
    print('\t**  English Muffin............$1.75  **')
    print('\t**  Coffee....................$2.99  **')
    print('\t**  Juice.....................$1.99  **')
    print('\t**                                   **')
    print('\t***************************************')

    
while True: #starts the while loop, no breaks this loop.
    menu()
    total=0.00
    print ("\n\n Would you like to place an order? ('yes' to place order, 'no' to end) ")
    answer=input()
    if answer =='no':
        break
    
    if answer=='yes':
        while True: #starts another while loop, 999 breaks this loop.
    
            order= input("\n\n Please enter your breakfast selection or '999' when you are finished with your order. ")
            if order not in bfast:
                print ('\n\n We do not currently carry that item. See menu below. ')
                menu()
                continue
            if order =='':
                print('\n\n That is not a valid selection. Please choose an item from the menu. ')
                menu()              
                continue
            if order =='999':
                break
                
            while True:
                cust_order = cust_order +[bfast.get(order)]
                order = input("\n\n Please enter another breakfast selection or '999' when you are finished with your order. ")
                if order =='':
                    print()
                    menu()                   
                        
                if order not in bfast:
                    if order =='999':
                        break
                    if order =='':
                        print ('\n\n That is not a valid selection. Please choose item from the menu. ')
                        print()           
                    else:
                        print ('\n\n We do not currently carry that item. See menu below. ')
                        menu()
                        print()
                        continue
 
                else:
                    continue
                            
        
            else:
                continue
                
    

            
           
            filtered_list=list(filter(None, cust_order))#filtered list so that python could total the numbers from the list.
            
            cost = sum(filtered_list)
            total= ((cost *.09) + cost)
            print('\n\n Your total including tax: $ ' + str(format(total, '.2f')))
            print()
            an= input('\n\n Would you like to place a new order? (y or n) ')
            #both y&n clear screen. n is as if a new customer is walking up,
            #y is as if it is the same customer doing multiple orders.

            if an=='y':
                print()
                print('Thank you!!')
                print()
                time.sleep(3)
                os.system('cls')
                cust_order.clear()
                menu()
                continue
            if an=='n':
                print()
                print ('Thank you!! Your order will be ready soon! ')
                print()
                time.sleep(5)
                os.system('cls')
                cust_order.clear()
                menu()
        else:
            print('Invalid response')
            continue

time.sleep(5)



