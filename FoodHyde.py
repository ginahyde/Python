#Program to assist Hendrix Food Truck tally the total bill for customers
#in their fast checkout

import time, os

#menu for user to choose from
while True:
    print ('Welcome to Hendrix Food Truck')
    print ('****************************************************')
    print ('*****1. Food Plate #1(wings)                $15*****')
    print ('*****2. Food Plate #2(chicken strips)       $10*****')
    print ('*****3. Food Plate #3(fish basket)          $12*****')
    print ('*****4. Food Plate #4(shrimp po boy)        $10*****')
    print ('*****5. Food Plate #5(pork chop basket)     $12*****')
    print ('****************************************************')
    print ()
    print ()
#prompts user for menu choice
    choice=input('Please enter the menu number of the food plate you would like to purchase or 999 to exit. ')
    choice=int(choice)

    if choice==1:
        cost=15
    elif choice==2:
        cost=10
    elif choice==3:
        cost=12
    elif choice==4:
        cost=10
    elif choice==5:
        cost=12
    else:
        choice==999
        break
    print ()
    print ()
#asks for tip amount
    tip=input('Would you like to leave a tip? If yes, enter amount. If no, enter 0. ')
    print('The tip amount you want to give is ' + str(tip))
#adds tax and calculates total with tip
    tax=float(cost *.09)
    total= float(cost + tax)+ float(tip)
    print('Please pay $ ' + format(total,'.2f'))
    print()
    time.sleep(5)

#thanks user upon exit
print ('Thank you!')
time.sleep(5)










