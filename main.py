#Sean Yang
def encode(originalString):
    finalString = ""
    for i in range(0, len(originalString)):
        tempInt = (int(originalString[i:i+1]) + 3) % 10
        finalString = finalString + str(tempInt)
    return finalString


def main():
    stillRunning = True
    encodedPassword = ""
    while stillRunning:
        selection = input("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n\nPlease enter an option: ")
        if selection == "1":
            passwordInput = input("Please enter your password to encode: ")
            encodedPassword = encode(passwordInput)
            print("Your password has been encoded and stored!")
        if selection == "3":
            stillRunning = False



if __name__ == '__main__':
    main()

