price = 0
print("Welcome to the Pizza cost calculator!")
print("Please enter any of the options shown to you with correct spelling,")
print("otherwise this program will not work properly.")
print("Would you like a thin or thick crust?")
crust = input().lower()
if crust == "thin":
  price = price + 8
elif crust == "thick":
  price = price + 10
print("Would you like an 8, 10, 12, 14, or 18 inch crust?")
size = int(input())
if size == 8 or size == 10:
  price = price + 0
elif size == 12 or size == 14 or size == 18:
  price = price + 2
print("Would you like cheese on your pizza? Please enter yes or no.")
cheese = input().lower()
if cheese == "yes":
  price = price + 0
elif cheese == "no":
  price = price - 0.5
print("What type of pizza would you like? You can choose from margarita, vegetable, vegan, Hawaiian or meat feast.")
pizzatype = input().lower()
if pizzatype == "margarita":
  price = price + 0
elif pizzatype == "vegetable" or pizzatype == "vegan":
  price = price + 1
elif pizzatype == "hawaiian" or pizzatype == "meat feast":
  price = price + 2
if size == 18:
  print("Do you have a voucher code? Please enter yes or no.")
  voucher = input().lower()
  if voucher == "yes":
    print("Type in your voucher code here:")
    code = input()
    if code == "FunFriday":
      price = price - 2
print("The total cost for your pizza is:")
print(price)
print("pounds. Enjoy your pizza!")