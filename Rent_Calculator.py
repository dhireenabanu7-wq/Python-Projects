## Inputs we need from the user 
# Number of Persons living in flat 
# Total rent 
# Total cost spent on Groceries
# Electricity units Spent
# Charge per Units Spend

# Output 
# Total amount One person Has to Pay

persons = int(input("Number of persons Living in One Flat :"))
rent = int(input("Enter your flat rent : "))
groceries = int(input("Enter The amount spent on groceries : "))
electricity_spent = int(input("Enter The Total of electricity spend : "))
charge_per_unit = int(input("Enter the charge per unit : "))

total_amount = (rent + groceries + (electricity_spent * charge_per_unit))
amount_per_person = (total_amount)//persons

print(f"The Amount Has To be Paid By one person is : ",amount_per_person)