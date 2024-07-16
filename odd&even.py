def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

while True:
    try:
        user_input = int(input("Enter a number: "))
        result = check_even_odd(user_input)
        print(f"The number {user_input} is {result}.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

