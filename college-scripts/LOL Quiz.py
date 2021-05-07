#Quiz

#Setup Question Answers
Answer1="138"
Answer2="21"
Answer3="diamond"
Answer4="false"
Answer5="no"

#Asking The Question
Score=0
Question1=input("How many Champions are in Legaue of Legends")
if str.lower(Question1)==Answer1:
    print("Correct!")
    Score=Score+1
else:
    print("Incorrect!")

Question2=input("How many Marksmen are in League of Legends")
if str.lower(Question2)==Answer2:
    print("Correct!")
    Score=Score+1
else:
    print("Incorrect!")

Question3=input("What division is higher, Diamond or Platinum?")
if str.lower(Question3)==Answer3:
    print("Correct!")
    Score=Score+1
else:
    print("Incorrect!")

Question4=input("Is Forest a Role in League of Legends? (Answer true or False)")
if str.lower(Question4)==Answer4:
    print("Correct!")
    Score=Score+1
else:
    print("Incorrect!")

Question5=input("Is League of Legends Over 10 Years Old? (Yes or No)")
if str.lower(Question5)==Answer5:
    print("Correct!")
    Score=Score+1
else:
    print("Incorrect!")


#Displaying The Score
print("Well Done you Got ", Score, " Points!")
