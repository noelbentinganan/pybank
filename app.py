print(35 * "*")
print("** \t \t \t \t **")
print("** \t Welcome to PyBank \t **")
print("** \t \t \t \t **")
print(35 * "*")
print("\n")


# Funds
available_funds = 10000
print(f"Funds Available: {available_funds}")

# withdraw fn
def withdraw(amount):
  return available_funds - amount

print("\n")

print("What would you like to do? \n [1] - Withdraw \n [2] - Deposit \n")
choice = int(input(""))

if(choice == 1):
  amount = float(input("Amount: "))
  print(withdraw(amount))
  available_funds = amount
  print(available_funds)
elif(choice == 2):
  print("")
  

