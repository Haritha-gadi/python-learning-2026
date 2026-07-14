# Day 9 - Multiple Elif Statements

amount = 6500

print("Discount Calculator")

if amount >= 10000:
    print("30% Discount")
elif amount >= 5000:
    print("20% Discount")
elif amount >= 2000:
    print("10% Discount")
else:
    print("No Discount")