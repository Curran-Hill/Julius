def decode():
    ceaser_text = input("Paste string here: ")
    
    for x in range(26):
        new_text = ""

        for char in ceaser_text:
            new_char = chr((ord(char)-ord('a')+x)%26+ord('a'))
            new_text += new_char

        print(f"+{x}: {new_text}\n")      


decode()