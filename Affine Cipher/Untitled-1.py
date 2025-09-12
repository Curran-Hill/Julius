class AffineCipher:
    def __init__(self, a, b, alpha_SIZE = 26):
        self.a = a
        self.b = b
        self.alpha_SIZE = alpha_SIZE

    def mod_inv(self):
        inv_a = None
        for i in range(1, 27):
            if(self.a * i) % self.alpha_SIZE == 1:
                inv_a = i
                break
            if inv_a is None:
                continue
        
    def validate_a(self):
        if self.a.isdigit() and int(self.a) % 2 != 0 and int(self.a) != 13 and int(self.a) in range(self.alpha_SIZE):
                self.a = int(self.a)
                return True
        else:
            print('!!ERROR!! Invalid input for "A"')
            return False

    def validate_b(self):
        if self.b.isdigit() and int(self.b) in range(self.alpha_SIZE):
            self.b = int(self.b)
            return True
        else:
            print('!!ERROR!! Invalid input for "B"')
            return False

    def encrypt(self, plaintext):

        ciphertext = ""

        for char in plaintext:
            if char.islower():
                x = ord(char) - ord('a') % self.alpha_SIZE
                new_char = (self.a * x + self.b) % self.alpha_SIZE
                ciphertext += chr(int(new_char) + ord('a'))
            elif char.isupper():
                x = ord(char) - ord('A') % self.alpha_SIZE
                new_char = (self.a * x + self.b) % self.alpha_SIZE
                ciphertext += chr(int(new_char) + ord('A'))
            else:
                new_char = chr(x)
                ciphertext += new_char
            
        return ciphertext

A1 = AffineCipher(23, 13)
print(A1.encrypt('abc'))

#works, idk how input would work