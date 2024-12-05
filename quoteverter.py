def convert_quotes():
    print("Where do you wanna start:")
    print("1. Straight quote")
    print("2. Curly quote")
    
    choice = input("Choose (1 or 2): ").strip()
    
    if choice == "1":
        text = input("Input text with straight quotes: ")
        converted = text.replace('"', '“').replace('"', '”').replace("'", "‘").replace("'", "’")
        print("Output:", converted)
    elif choice == "2":
        text = input("Input text with curly quotes: ")
        converted = text.replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
        print("Output:", converted)
    else:
        print("Invalid choice! Please enter 1 or 2.")
        
convert_quotes()
