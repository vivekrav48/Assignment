while True:
    age = input("Enter your age (or 'q' to exit): ")

    if age.lower() == 'q':
        print("Thank you. Exiting the program.")
        break

    age = int(age)

    if age < 3:
        ticket_price = 0
    elif 3 <= age <= 12:
        ticket_price = 15
    else:
        ticket_price = 20

    print(f"The cost of your movie ticket is ${ticket_price}.")

