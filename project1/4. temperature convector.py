def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

def c_to_k(c):
    return c + 273.15

def k_to_c(k):
    return k - 273.15

def f_to_k(f):
    return (f - 32) * 5/9 + 273.15

def k_to_f(k):
    return (k - 273.15) * 9/5 + 32


print("Temperature Converter")
print("----------------------")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")
print("5. Fahrenheit to Kelvin")
print("6. Kelvin to Fahrenheit")

choice = int(input("Choose an option (1–6): "))

temp = float(input("Enter the temperature value: "))

if choice == 1:
    print(f"{temp}°C = {c_to_f(temp):.2f}°F")
elif choice == 2:
    print(f"{temp}°F = {f_to_c(temp):.2f}°C")
elif choice == 3:
    print(f"{temp}°C = {c_to_k(temp):.2f}K")
elif choice == 4:
    print(f"{temp}K = {k_to_c(temp):.2f}°C")
elif choice == 5:
    print(f"{temp}°F = {f_to_k(temp):.2f}K")
elif choice == 6:
    print(f"{temp}K = {k_to_f(temp):.2f}°F")
else:
    print("Invalid option!")