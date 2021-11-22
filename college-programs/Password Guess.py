#Password Guess

#Store Passwords

Password1="1111"
Password2="2222"
Password3="3333"

#Input Guess's From User
Guess1=input("What is the first password?")
Guess2=input("What is the second password?")
Guess3=input("What is the third password?")

#Make Sure Passowrds Match

if Guess1==Password1 and Guess2==Password2 and Guess3==Password3:
    print("Access Granted = You may now access the mainframe")
else:
    print("Sorry, on of more of your passwords were wrong.")
