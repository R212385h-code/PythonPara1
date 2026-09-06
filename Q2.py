fruits = ["Apple", "Banana", "Mango", "Orange", "Strawberry"]

with open("fruits.txt", "w") as file:
    for fruit in fruits:
        file.write(fruit + "\n")

with open("fruits.txt", "r") as file:
    fruits = file.readlines()

for fruit in fruits:
    print(fruit.strip())
    