import random
small_letters="abcdefghijklmnopqrstuvwxyz"
capital_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
all_letters=small_letters+capital_letters
n="1234567890"
special_char="!@#$%^&*~_=?/"
pass_list=[]
password=""
s='''

                                            _                                   _             
                                           | |                                 | |            
  _ __   __ _ ___ _____      _____  _ __ __| |   __ _  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 | '_ \ / _` / __/ __\ \ /\ / / _ \| '__/ _` |  / _` |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | |_) | (_| \__ \__ \ V  V /  (_) | | | (_| | | (_| |  __/ | | |  __/ | | (_| | || (_) | |   
 | .__/ \__,_|___/___/ \_/\_/ \___/|_|  \__,_|  \__, |\___|_| |_|\___|_|  \__,_|\__\___/|_|   
 | |                                             __/ |                                        
 |_|                                            |___/                                     
 '''
print(s)
l=int(input("Enter the no of characters you want in your password"))

if l>=8:
    n_alphabets=int(input("Enter the no of alphabets you want in your password"))
    n_numbers=int(input("Enter the no of digits you want in your password"))
    n_special=int(input("Enter the no of special characters you want in your password"))
    for i in range(1):
        pass_list.append(random.choice(capital_letters))
    for i in range(n_alphabets-1):
        pass_list.append(random.choice(all_letters))
    for i in range(n_numbers):
        pass_list.append(random.choice(n))
    for i in range(n_special):
        pass_list.append(random.choice(special_char))
    random.shuffle(pass_list)
    for i in range(l):
        password=password+str(pass_list[i])
    print(password)
else:
    print("Please make sure your password has 8 or more than 8 characters in it")
    
