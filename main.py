user_input = input("You are currently using the XY bank. If you don't have an account yet, you can create one by pressing the 1 key. Please enter your password: ")

if user_input == "1":
    new_password = input("Please enter your new password: ")
    with open('passwords.txt', 'a') as file:
        file.write(new_password + '\n')
    
    try:
        with open('balances.txt', 'r') as file:
            balances = dict(line.strip().split(':') for line in file)
    except FileNotFoundError:
        balances = {}

    balances[new_password] = '500'  # Initialize new account with $500 balance

    with open('balances.txt', 'w') as file:
        for user, balance in balances.items():
            file.write(f"{user}:{balance}\n")

    print("You have successfully created a new account. Your balance is $500.")
    user_input = new_password

with open('passwords.txt', 'r') as file:
    passwords = file.read().splitlines()

if user_input in passwords:
    print("You have successfully logged into the XY bank system")
else:
    print("Incorrect password! Please try again.")
    exit()

try:
    with open('balances.txt', 'r') as file:
        balances = dict(line.strip().split(':') for line in file)
except FileNotFoundError:
    balances = {}

if user_input not in balances:
    balances[user_input] = '500'  # Initialize balance for a new user

balance = int(balances[user_input])

choice = input("Would you like to calculate interest or check your balance? (I interest, B balance) ").upper()

if choice == "I":
    print("Currently calculating interest")
    
    while True:
        try:
            principle = float(input("Enter the principal amount: "))
            if principle < 0:
                print("Principal can't be less than 0")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            rate = float(input("Enter the rate amount: "))
            if rate < 0:
                print("Rate can't be less than 0")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            time = int(input("Enter the time in years: "))
            if time <= 0:
                print("Time can't be 0 or less")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    final_amount = principle * (1 + rate / 100) ** time
    print(f"Balance after {time} years: ${final_amount:.2f}")
    exit()

elif choice == "B":
    print(f"Currently checking balance. Your balance is: ${balance}")

    balance_action = input("Would you like to withdraw or deposit? (W withdraw, D deposit) ").upper()

    if balance_action == "W":
        print("Withdrawing money")
        amount = int(input("How much would you like to withdraw? "))
        if amount > balance:
            print("Insufficient funds.")
            exit()
        else:
            balance -= amount
    elif balance_action == "D":
        print("Depositing money")
        amount = int(input("How much would you like to deposit? "))
        balance += amount
    else:
        print("Invalid choice! Please try again.")
        exit()

    balances[user_input] = str(balance)

    with open('balances.txt', 'w') as file:
        for user, balance in balances.items():
            file.write(f"{user}:{balance}\n")

    print(f"Your current balance is ${balance}")

exit_prompt = input("Press E to exit: ")

if exit_prompt.upper() == "E":
    exit()
else:
    exit()
