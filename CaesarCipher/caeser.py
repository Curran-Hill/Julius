class CaesarCipher:
    def __init__(self, alpha_size = 26):
        self.alpha_size = alpha_size

    def encrypt(self, plaintext):
        shift = input("Input shift amount: ")
        shift = int(shift)
        
        ciphertext = ""

        for char in plaintext:
            if(char.islower()):
                new_char = chr((ord(char) - ord('a') + shift) % self.alpha_size + ord('a'))
                ciphertext += new_char
            elif(char.isupper()):
                new_char = chr((ord(char) - ord('A') + shift) % self.alpha_size + ord('A'))
                ciphertext += new_char
            else:
                new_char = char
                ciphertext += new_char

        print(f'Ciphertext: {ciphertext}')
    
    def decrypt(self, ciphertext):

        for shift in range(self.alpha_size):
            plaintext = ""
            for char in ciphertext:
                if(char.islower()):
                    new_char = chr((ord(char) - ord('a') + shift) % self.alpha_size + ord('a'))
                    plaintext += new_char
                elif(char.isupper()):
                    new_char = chr((ord(char) - ord('A') + shift) % self.alpha_size + ord('A'))
                    plaintext += new_char
                else:
                    new_char = char
                    plaintext += new_char

            print(f'+{shift}: {plaintext}\n')