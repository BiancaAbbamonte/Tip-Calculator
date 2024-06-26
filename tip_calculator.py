print("Welcome to the Tip Calculator!\n")

bill = float(input("What was the total bill?\n$"))
tip = int(input("How much tip would you like to give? 10%, 12%, 15%?\n"))
numberPeople = int(input("How many people to split the bill?\n"))

finalValue = round(((bill / numberPeople) * (1 + tip/100)),2)

#esse step é apenas para garantir as duas após a virgula
final_amount = "{:.2f}".format(finalValue)

print(f"Cada pessoa vai pagar: ${final_amount}")