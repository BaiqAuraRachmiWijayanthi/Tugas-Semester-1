def calculate_discount(purchase_amount, has_member_card):
  """Calculates the discount based on the purchase amount and member card status."""
  discount = 0
  if has_member_card:
    if purchase_amount > 500000:
      discount = 0.20 
    elif purchase_amount >= 500000:
      discount = 0.10
  else:
    if purchase_amount > 500000:
      discount = 0.05
  return discount

def calculate_total_price(purchase_amount, discount):
  """Calculates the total price after applying the discount."""
  discount_amount = purchase_amount * discount
  total_price = purchase_amount - discount_amount
  return total_price

# Get user input
purchase_amount = float(input("Enter the total amount of your purchase: "))
has_member_card = input("Do you have a member card? (yes/no): ").lower() == 'yes'

# Calculate the discount and total price
discount = calculate_discount(purchase_amount, has_member_card)
total_price = calculate_total_price(purchase_amount, discount)

# Print the output
print("Total purchase amount:", purchase_amount)
print("Discount percentage:", discount * 100, "%")
print("Total price:",)