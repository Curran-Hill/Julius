
def encrypt():

    plaintext = input("Paste plain text here: ")

    while True:
        a = input("A: ")
        if a.isdigit() and int(a) % 2 != 0 and int(a) != 13 and int(a) in range(1, 26):
            a = int(a)
            break
        else:
            print('!!ERROR!! Invalid input for "A"')
            
    while True:
        b = input("B: ")
        if b.isdigit() and int(b) in range(1, 26):
            b = int(b)
            break
        else:
            print('!!ERROR!! Invalid input for "B"')

    x_arr = []

    for char in plaintext:
        x_arr.append(ord(char))

    ciphertext = ""

    for x in x_arr:
        if x in range(ord('a'),ord('z')+1):
            x = (x-ord('a')) % 26
            new_char = (a * x + b) % 26
            ciphertext += chr(int(new_char)+ord('a'))
        elif x in range(ord('A'),ord('Z') + 1):
            x = (x-ord('A')) % 26
            new_char = (a * x + b) % 26
            ciphertext += chr(int(new_char) + ord('A'))
        else:
            new_char = chr(x)
            ciphertext += new_char
        
    print(ciphertext)

def decrypt():

    ciphertext = input("Paste ciphertext here: ")

    x_arr = []

    for char in ciphertext:
        x_arr.append(ord(char))

    for a in range(1,26):
        if a % 2 != 0 and a != 13:
            
            inv_a = None
            for i in range(1, 27):
                if(a * i) % 26 == 1:
                    inv_a = i
                    break
            if inv_a is None:
                continue
        
            for b in range(1,26):
                plaintext = ""
                for x in x_arr:
                    if x in range(ord('a'),ord('z')+1):
                        x_val = (x-ord('a')) % 26
                        new_char = (inv_a * (x_val - b)) % 26
                        plaintext += chr(new_char + ord('a'))
                    elif x in range(ord('A'),ord('Z') + 1):
                        x_val = (x-ord('A')) % 26
                        new_char = (inv_a * (x_val - b)) % 26
                        plaintext += chr(new_char + ord('A'))
                    else:
                        new_char = chr(x)
                        plaintext += new_char

                print(f"Encryption Key 'A':{a} | B:{b} | Decruption Key 'Inverse A': {inv_a} | Text: {plaintext} \n")
        else:
            pass


while True:
    user_choice = input("What are you doing? ENCRYPTION: 1 | DECRYPTION: 2\n")

    if user_choice == "1":
        print("""##INSTRUCTIONS##
==============================================
Encryption:
    1.) Paste your string into the prompt
    2.) Set values for 'A' and 'B'
      2a.) Value 'A' must be coprime with 26 (Cannot be even or 13) and must be a number 1-25
      2b.) Value 'B' must be a number 1-25
        """)
        encrypt()
        break
    elif user_choice == "2":
        print("""##INSTRUCTIONS##
==============================================
Decryption:
    1.) Paste your ciphertext into the prompt
    2.) Julius will brute force the decryption
    3.) Look for your expected plaintext    
        """)
        decrypt()
        break
    else:
        print("!!ERROR!! Please Select '1' or '2'")