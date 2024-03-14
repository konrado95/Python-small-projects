from Translator import letter_to_morse


def text_to_morse(text):
    result = ""
    for letter in text:
        if letter == " ":
            # 3 spaces will be added after every word
            result += "  "
        else:
            # 1 space will be added after every character
            result += letter_to_morse[letter.lower()] + " "
    return result


def morse_to_code(morse):
    raise NotImplementedError("Feature not implemented yet")


if __name__ == "__main__":
    print("Welcome to Text To Morse Converter")
    print("Converter supports only latin alphabet and digits")
    print("1. Text to Morse")
    print("2. Morse to Text")
    choice = int(input("Input a number of selected choice: "))

    if choice == 1:
        text = input("Insert a text to translate: ")
        print(text_to_morse(text))
    elif choice == 2:
        morse = input("Insert Morse Code to translate: ")
        print(morse_to_code(morse))
    else:
        print("Option not found")
