def num_check(question):

    error = "Please enter a number that is more than zero\n"
    while True:

        try:
            # ask the user for a number
            response = float(input(question))

            # check that the number is more than zero
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)



keep_going = ""
while keep_going =="":

    # Get width and height
    width = num_check("Width: ")
    length = num_check("Length: ")
    costpermeter = num_check("Cost per meter: ")

    # Calculate perimeter
    perimeter = 2 * (width + length)

    # Calculate cost
    Cost = perimeter*costpermeter

    # Display output
    print()
    print(f"perimeter: {perimeter} meters")
    print("$",Cost)

    # Ask user if they want to keep going
    keep_going = input("Press enter to keep going or any key to quit: ")
    print()

print("Thank you for using the calculator")