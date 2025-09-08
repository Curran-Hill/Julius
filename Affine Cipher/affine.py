def encode():

    plaintext = input("Paste plain text here: ")

    a = input("A: ")
    while a.isdigit() == False or int(a) % 2 == 0 or int(a) == 13 or int(a) not in range(1,26):
        print('ERROR! Invalid input for "A"')
        a = input("Please retry: ")
            
    b = input("B: ")
    while b.isdigit() == False or int(b) not in range(1,26):
        print('ERROR! Invalid input for "B"')
        b = input("Please retry: ")

    x_arr = []

    for char in plaintext:
        x_arr.append(ord(char))

    ciphertext = ""

    for x in x_arr:
        if x in range(97,123): #Unicode range for lowercase letters
            x = x-ord('a')%26
            new_char = (int(a)*x+int(b))%26
            ciphertext += chr(int(new_char)+ord('a'))
        elif x in range(65,90): #Unicode range for uppercase letters
            x = x-ord('A')%26
            new_char = (int(a)*x+int(b))%26
            ciphertext += chr(int(new_char)+ord('A'))
        else:
            new_char = chr(x)
            ciphertext += new_char
        
    print(ciphertext)

encode()