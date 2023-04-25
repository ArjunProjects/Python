# Format variables using a string.format() method.

quantity = 3
total_money = 1000
price = 300

statement = "I have {1} dollars so I can buy {0} football for the price {2:.2f}"
print(statement.format(quantity, total_money, price))
