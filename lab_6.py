#Antonio
def encode(password):
    encoded_password = ""
    for digit in password:
        new_digit = str((int(digit) + 3) % 10)
        encoded_password += new_digit
    return encoded_password

#Added by Cam
def decode(password):
    decoded_password = ""
    for digit in password:
        new_digit = str((int(digit) - 3) % 10)
        decoded_password += new_digit
    return decoded_password

def main():
    encoded_password = ""
    while True:
        print("\nMenu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        choice = input("\nPlease enter an option: ")

        if choice == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")

        elif choice == "2":
            if encoded_password == "":
                print("Please encode a password first.")
            else:
                password = decode(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {password}.")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()

