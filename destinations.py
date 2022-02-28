from distutils.sysconfig import customize_compiler
import random
from tkinter.messagebox import YES

destination_list = ["Kanas City", "Buffalo", "Portland", "Alanta", "Myrtle Beach"]    

destination = random.choice(destination_list)  
print(f'We have selected {destination} as your destination')
customer_verified = False
while customer_verified == False:
    yes = input ("If you want to confirm say Yes, if you want a new option say No ")
    if(yes == 'yes'):
        print( "Thank you for confirming") 
        customer_verified = True
    elif(yes =='no'):
        print('Sorry you dont like that. Please try again.')
        destination = random.choice(destination_list) 
        print(f'This is your new destination {destination}') 

dining_list = ["Texas Road House", "Red lobster", "Olive Garden", "Long Horn", 'Duffs"']

dining = random.choice(dining_list)
print(f'We have selected {dining} for your dining') 
customer_verified = False 
while customer_verified == False:
    yes = input ("If you want to confirm say yes, If you want a new one say No ")
    if(yes == 'yes'):
        print("Thank you for confirming")
        customer_verified = True
    elif(yes == 'no'):
         print('Sorry you dont like that. Please try again.')
         dining = random.choice(dining_list)
         print(f'This is your new dining choice {dining}')

transportation_list = ["Rental Car", "Plane", "Train", "Bus"]

transportation = random.choice(transportation_list)
print(f'We have selected {transportation} for your way of arriving')
customer_verified = False
while customer_verified == False:
    yes = input("If you want to confirm say Yes, If you want a new one say No ")
    if(yes == 'yes'):
        print("Thank you for confirming")
        customer_verified = True
    elif(yes == 'no'):
         print(f'Sorry you dont like that. Please try again.')
         transportation = random.choice(transportation_list)
         print(f'This is your new way to travel {transportation}')


entertainment_list = ["Clubs", "Concert", "Sky Diving","Movies", "Hockey Game"]

entertainment = random.choice(entertainment_list)
print(f'We have selected {entertainment} for your entertainment')
customer_verified = False
while customer_verified == False:
    yes = input("If you want to confirm say Yes, If you want a new one say No ")
    if(yes == 'yes'):
        print("Thank you for comfirming")
        customer_verified = True
    elif(yes == 'no'):
         print(f'Sorry you dont like that. Please try again.')
         entertainment = random.choice(entertainment_list)
         print(f'This your new entertianment {entertainment}')

print('Thank you for booking with us your trip is confirmed')