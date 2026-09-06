def main():
    while True:
        try:
            age = int(input("Enter your age: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    print("Your age is:", age)


if __name__ == "__main__":
    main()
