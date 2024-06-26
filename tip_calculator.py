print("Welcome to the Tip Calculator!\n")

bill = float(input("What was the total bill?\n$"))
tip = int(input("How much tip would you like to give? 10%, 12%, 15%?\n"))
number_people = int(input("How many people to split the bill?\n"))

fina_value = round(((bill / numberPeople) * (1 + tip/100)),2)

#This step is just to make sure there is to values after the comma
final_amount = "{:.2f}".format(final_value)

print(f"Cada pessoa vai pagar: ${final_amount}")
