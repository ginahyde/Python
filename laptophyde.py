#build dictionary of robots and base prices

import os, time

computers={'a':600, 'b': 650, 'c':720, 'd':750, 'e':800}

def menu(): #created a function for my menu so I wouldn't have to copy and paste.
    print('\t*******************************************************')
    print('\t**                    SCC Book Inn                   **')
    print('\t**                                                   **')
    print('\t**  Computers             Enter            Price     **')
    print('\t**  Acer Aspire..........[  a  ]..........$600.00    **')
    print('\t**  Lenovo Idea Pad......[  b  ]..........$650.00    **')
    print('\t**  Asus ZenBook.........[  c  ]..........$720.00    **')
    print('\t**  Dell Lattitude.......[  d  ]..........$750.00    **')
    print('\t**  HP Pavilion..........[  e  ]..........$800.00    **')
    print('\t**                                                   **')
    print('\t*******************************************************')


#prompt user for which computer to purchase

while True:
    menu()
    print ('Please enter the code of the computer you would like to purchase(Enter blank to end.)')
    compchoice=input()
    if compchoice=='':
        break

    if compchoice in computers:
        print('The price of the computer is ' ,format(computers[compchoice],',.2f'))
        print()
    else:
        print ('We do not carry that computer. See menu.')
        continue

# ask about discounts.
#ask if a veteran
    veteran= input('Are you a veteran?(y or n)\n')
    
#ask if technical scholar
    tech=input('Are you a technical scholar? (y or n)\n')

#ask if member of TRIO
    trio= input('Are you a member of the TRIO program? (y or n)\n')
    
    protect=input('Would you like to add a protection plan for $150.00. (y or n) \n')
    
    

#determine add on prices and discounts
    if veteran=='y':
        vet_price=.30
    else:
        vet_price=0
        
    if tech =='y':
        tech_price=.50
    else:
        tech_price=0

    if trio=='y':
        trio_price=.20
    else:
        trio_price=0

    if protect=='y':
        protect_price=150
    else:
        protect_price=0




#calculate total price of computer substracting discounts and add tax.
    totaldiscount= vet_price+tech_price+trio_price
    disctosub=(computers[compchoice]) * totaldiscount
    comptotal=(computers[compchoice])-disctosub
    protecttotal=comptotal+protect_price
    total=protecttotal*1.07
    print ('\n Your total price is $', format(total, ',.2f'))
    print()
    print()

print('Thank you and have a nice day!')
time.sleep(5)
