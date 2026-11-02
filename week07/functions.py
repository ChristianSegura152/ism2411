#Self Assessment questions
#1. The first Bug I spotted in exercise 5 was due to the traceback error that was given when I ran the code. This tells me about my current debugging skills because it shows that I am able to read and understand the error messages given by Python, which is an important skill in debugging.
#2.The apply_discount(price, tier) function explains the discount applied to a price based on the tier if the customer is is. Its inputs are the price of the item and the tier of the customer, it returns the discounted price based on the tier of the customer. Without reading the body, a colleague could understand it just by looking at the name of the function.
#AI disclosure: I used AI to help me better understand why the third bug in exercise 5 was happening and how to fix it.




# --- Exercise 1 ---

#Define calculate tax function

def calculate_tax(price, rate):
    return price * rate

#calling the function
tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}")
print(f"Tax on $250 at 8%: ${tax2:.2f}")


#--- Exercise 2 ---

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

#calling the function
price = 200 
tiers = ["gold", "silver", "bronze", "none"]

for tier in tiers:
    print(f"{tier}: ${apply_discount(price, tier):.2f}")


#--- Exercise 3 ---

#Write it out manually first, then refactor into a function

discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"After gold discount: ${discounted:.2f}")
print(f"After tax: ${after_tax:.2f}")

#refactor into a function

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')

# --- Exercise 4 ---

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price:,.2f}, Tier: {tier}, Final: ${total:.2f}")

# --- Exercise 5 ---

# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale #Adding the + allowed the total to be calculated correctly instead of the total being passed to the last sale in the list.
print(f"Total: ${total}")

count = 0
for sale in sales: # The error was a Syntax Error due to a missing semicolon at the end of the for loop.
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales): #The IndexError was caused by the index trying to acces a number that didnt exist in the sales list. Making it stop before it got to 5 fixed the bug.
    print(sales[i])
    i += 1




# --- Exercise 6 ---

x = 100     #Global variable

def double_it():
    x = 999     # Local variable - different from global x
    return x * 2

print(x)
print(double_it())
print(x)

# This output was because the local variable x inside the function double_it() does not affect the global variable x.
#The global variable x remains unchanged at 100, while the function returns 1998 (999 * 2).