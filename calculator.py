print(" _______  ________  ___       ________  ___  ___  ___       ________  _________  ________  ________")
print("|\   ____\|\   __  \|\  \     |\   ____\|\  \|\  \|\  \     |\   __  \|\___   ___\\   __  \|\   __  \    ")
print("\ \  \___|\ \  \ \  \ \  \    \ \  \___|\ \  \\\  \ \  \    \ \  \ \  \|___ \  \_\ \  \|\  \ \  \ \  \   ")
print(" \ \  \    \ \   __  \ \  \    \ \  \    \ \  \\\  \ \  \    \ \   __  \   \ \  \ \ \  \\\  \ \   _  _\  ")
print("  \ \  \____\ \  \ \  \ \  \____\ \  \____\ \  \\\  \ \  \____\ \  \ \  \   \ \  \ \ \  \\\  \ \  \\  \| ")
print("   \ \_______\ \__\ \__\ \_______\ \_______\ \_______\ \_______\ \__\ \__\   \ \__\ \ \_______\ \__\\ _\ ")
print("    \|_______|\|__|\|__|\|_______|\|_______|\|_______|\|_______|\|__|\|__|    \|__|  \|_______|\|__|\|__|")
print("                                                                                                         ")
def divide(x, y):
   return x / y
import math
print("")
print("By Rodrigo, 10A ")
print("")
print("Select Operation:")
print("")
print("> 1: Addition")
print("> 2: Subtraction")
print("> 3: Multiplication")
print("> 4: Division")
print("")
choice = input("Choose action (1/2/3/4): ")


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print(num1 + num2)
    print("Done!")

elif choice == '2':
    print(num1 - num2)
    print("Done!")

elif choice == '3':
    print(num1 * num2)
    print("Done!")

elif choice == '4':
    print(num1 / num2)
    print("Done!")
else: ("Invalid Input")
print("")
input("Press enter to restart")


