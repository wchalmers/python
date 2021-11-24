def hello_world(): # Creates a function called hello_world.
    print("Hello, world!")

hello_world() # Calls the hello world function that will run any code inside of it.




def add_two(num): # Creates a function with a local variable in it named num.
    return num + 2

add_two(5) # Calls the function add_two and inputs the num local variable.




def contact_card(name, age, car_model): # Creates function with multiple local variables.
    return f"{name} is {age} and drives a {car_model}" # Will return some text with the local variables substituted in.

contact_card("William", 20, "Honda Civic Type R") # Calls function and pupulates variables.
contact_card(age=20, name="William" car_model="Honda Civic Type R") # Another way of pupulating variables, by specifying them then the value (dont need to be in order this way).




def can_drive(age, driving_age=17): # Creates function where one variable has a default value.
    return age >= driving_age

can_drive(20) # Calling function but only passing one variable as the other one has default value (can optionally be specifed though).