# The canteen follows these rules:
# - If the bill is Rs. 3,000 or more, the student receives a 
# 20% discount.
# - If the bill is Rs. 2,000 or more but less than Rs. 3,000, 
# the student receives a 10% discount.
# - If the bill is Rs. 1,000 or more but less than Rs. 2,000, 
# the student receives a 5% discount.
# - If the bill is less than Rs. 1,000, no discount is provided.
# - The program must display the original bill, discount amount,
# and final payable amount.

print("===== SMART CANTEEN =====")
bill_amount = float(input("Enter your total bill amount (Rs.): "))


if bill_amount <= 0:     # 1. If the bill is less than or equal to zero, display an invalid bill message.
    print("Invalid bill amount. Please enter a positive value.")
    exit() 
else: 


    if bill_amount >= 3000:
        discount_rate = 20
    elif bill_amount >= 2000:
        discount_rate = 10
    elif bill_amount >= 1000:
        discount_rate = 5
    else:
        discount_rate = 0

    membership = input("Do you have a membership card? (yes/no): ")   

    if membership.lower() == "yes":   # 2. If the student has a membership card, provide an additional 5% discount.
        discount_rate += 5


discount_amount = bill_amount * discount_rate / 100
final_amount = bill_amount - discount_amount

print("\n===== BILL SUMMARY =====")
print(f"Original Bill: Rs. {bill_amount:.2f}")
print(f"Discount Rate: {discount_rate}%")
print(f"Discount Amount: Rs. {discount_amount:.2f}")
print(f"Final Payable: Rs. {final_amount:.2f}")

if discount_amount > 0:    # 3. Display a message saying "Congratulations! You saved Rs. X" when a discount is applied.
    print(f"Congrats! you saved RS: {discount_amount:.2f}")
else:
    print("No discount applied. Thank you for your purchase!")


# Why do we use elif instead of writing several 
# independent if statements?

# Ans:  elif because it checks the next condition only when the previous condition is false.
