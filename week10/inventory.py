# Reflection

# 1.  I didn't expect .sort() and .append() to change the original list. I
# thought they would hand me a new one. Slices also stop one before the
# end number, which threw me off at first.

# 2.  At my job at Publix, I'd sometimes go through long lists of items one by
# one to check prices. A list and a loop could do that in seconds, and I
# could rerun it every week without redoing the work.
 
# -- Exercise 1: --
print("Exercise 1")
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))
 
# -- Exercise 2: --
print("\nExercise 2")
print(inventory[0])
print(inventory[-1])
middle = len(inventory) // 2
print(inventory[middle])
 
# -- Exercise 3: --
print("\nExercise 3")
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])
 
# -- Exercise 4: --
print("\nExercise 4")
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)
 
# -- Exercise 5: --
print("\nExercise 5")
coords = (40.7128, -74.0060)
try:
    coords[0] = 99
except TypeError as error:
    print(f"TypeError caught: {error}")
    print("Tuples are useful for coordinates because a location should not "
          "change by accident once it is set.")
print(coords)
 
# -- Exercise 6: --
print("\nExercise 6")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average}")
print(f"Best: {max(sales)}")
print(f"Worst: {min(sales)}")
 
# -- Exercise 7: --
print("\nExercise 7")
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
    discounted.append(round(price * 0.90, 2))
print(prices)
print(discounted)
 
# -- Exercise 8: --
print("\nExercise 8")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for day in sales:
    if day > 300:
        high_sales.append(day)
print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Avg: {sum(high_sales) / len(high_sales):.2f}")