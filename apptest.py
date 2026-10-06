#names = []
#for _ in range(3):
 #   names.append(input("Enter a name: "))

#for name in sorted(names):
 #   print(f"Hello, {name}!")
 
#name = input("What is your name? ")
#with open("names.txt", "a") as file:
#   file.write(f"{name}\n")

#with open("names.txt", "r") as file:
#    names = file.readlines()
#for line in names:
#    print(f"Hello, {line.strip()}")

names = []
with open("names.txt", "r") as file:
    for line in file:
        names.append(line.strip())
for name in sorted(names):
    print(f"Hello, {name}")