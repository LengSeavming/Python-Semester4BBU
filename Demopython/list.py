n = int(input("Enter the number of elements: "))
data = []

for _ in range(n):
    item = input(f"Enter element {_+1}: ")
    data.append(item)

print("List:", data)
