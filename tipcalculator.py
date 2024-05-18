print("Welcome to the tip calculator")
bill = float(input('What was the total bill: '))
tip = float(input('How much would you like to give as a tip 10,15,20(in percentage): '))
num = int(input('How many people were there: '))

tip_amt = bill * (tip / 100)
tot_bill = bill + tip_amt
per_person = tot_bill / num
round_amt = round(per_person, 2)

print(f"The amount to be paid per person: {round_amt}")

