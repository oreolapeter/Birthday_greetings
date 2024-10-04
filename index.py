month = ('January','February','March','April','May','June','July','August','September','October','November','December')

import random # import random module
import time as t # import time module


time_list = []
for item in t.localtime():
    time_list.append(item)
print(time_list)

today = [str(time_list[2]),month[time_list[1]-1]]


response = input('thank you for your interest, please type yes to continue')
database = []
while response == 'yes':
    name = input('What is your full name: ')
    Day_month_of_birth = input('What is your Day and Month of Birth DDMM: ')
    gender = input('What is your gender: ')
    
    dayOB = Day_month_of_birth[0:2]
    Months = int(Day_month_of_birth[2:])-1

    monthOB = month[Months]
    birthday = dayOB
    birthmonth = monthOB
    bio =  {'Full_name': name, 'birthday':[dayOB,monthOB],'gender':gender}
    database.append(bio)
    


    response = input('thank you for your responses,please type no to terminate otherwise type yes to continue')
print(database)

bio =  {'Full_name': name, 'birthday':[dayOB,monthOB],'gender':gender,'birthday_bio':[name,bio['birthday']] }

the_birthay = []

for bio in database:
    if bio['birthday'] == today:
        the_birthay.append(bio)
the_birthay

the_name = []

for the_list in the_birthay:
    the_name.append(the_list['Full_name'])

the_name

for name in the_name:
    msg_list =[
    "Wishing you a year filled with adventure, joy, and endless possibilities. Happy Birthday!",
    "May your birthday be as sweet and beautiful as the joy you bring to everyone around you.",
    "Cheers to another year of laughter, love, and all the things that make life worth living! Happy Birthday!",
    "On your special day, may happiness surround you like sunshine and love fill your heart to the brim.",
    "To an amazing person who deserves nothing but the best—here’s to celebrating you today and always!",
    "May this year bring you success, peace, and all the good vibes you need. Happy Birthday!",
    "Sending you love, laughter, and warm wishes for a fantastic birthday filled with unforgettable moments.",
    "Wishing you a day filled with smiles, fun, and every happiness your heart desires. Have a fabulous birthday!",
    "Your birthday is a reminder of how much joy you bring to the world. May today be as wonderful as you are!",
    "Happy Birthday! May every moment of your special day be filled with joy, laughter, and cherished memories.",
    "Another trip around the sun and you're shining brighter than ever. Here's to a magical year ahead!",
    "On your special day, may you be surrounded by love, laughter, and endless happiness. Happy Birthday!",
    "May this year bring you even closer to your dreams. Wishing you a truly spectacular birthday celebration!",
    "To someone who makes the world a brighter place, happy birthday! May your day be full of love and joy.",
    "Your energy and spirit inspire everyone around you. Here's to another year of greatness! Happy Birthday!",
    "Hope your birthday is filled with as much fun and laughter as you bsring to those around you. Cheers to you!",
    "Wishing you a birthday as spectacular and unforgettable as you are. Have an amazing year ahead!",
    "On your special day, I hope all your dreams come true and the year ahead is filled with happiness and success.",
    "Here’s to another year of making memories, growing stronger, and achieving greatness. Happy Birthday!",
    "Wishing you the happiest of birthdays! May this year be filled with laughter, love, and everything you desire."
]

    msg_index = random.randint(0,len(msg_list)-1)
    random_msg = msg_list[msg_index]
    print(f'{name}, {random_msg}, from Me to you')




