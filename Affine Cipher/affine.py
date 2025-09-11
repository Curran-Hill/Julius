def encode():

    plaintext = input("Paste plain text here: ")

    while True:
        a = input("A: ")
        if a.isdigit() and int(a) % 2 != 0 and int(a) != 13 and int(a) in range(1, 26):
            a = int(a)
            break
        else:
            print('ERROR! Invalid input for "A"')
            
    while True:
        b = input("B: ")
        if b.isdigit() and int(b) in range(1, 26):
            b = int(b)
            break
        else:
            print('ERROR! Invalid input for "B"')

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
        
    return ciphertext

#print(encode())

def decode():

    ciphertext = input("Paste your ciphertext here: ")

    x_arr = []

    for char in ciphertext:
        x_arr.append(ord(char))

    for a in range (1,26):
        if a % 2 != 0 and a != 13:
            inv_a = 27 / a
            for b in range (1,26):
                #inv_a (x-b)%26

decode()