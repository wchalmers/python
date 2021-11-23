#Ticket Sales
no_of_tickets = 0
ticket_price = 5
price = 0

no_of_tickets = int(input("How many tickets have you bought?"))
price = no_of_tickets*ticket_price

if no_of_tickets >= 3:
    print("You qualify for the 10% discount")
    price = price - (price/10)
else:
        print("You do not qualify for the 10% discount")
        print("The cost for the tickets is ", price)
