class AffineCipher:
    def __init__(self,alpha_size = 26):
        self.alpha_size = alpha_size

    def mod_inv(self, a):
        inv_a = None
        for i in range(self.alpha_size + 1):
            if(a * i) % self.alpha_size == 1: #does this a have to be local? IDK
                inv_a = i
                break
        
        return inv_a
        
    def validate_a(self, a):
        if a.isdigit() and int(a) % 2 != 0 and int(a) != 13 and int(a) in range(self.alpha_size):
            return True
        else:
            print('!!ERROR!! Invalid input for "A" !!')
            print('!!"A" must be coprime with 26 and in the range 1-26!!')
            return False

    def validate_b(self, b):
        if b.isdigit() and int(b) in range(self.alpha_size):
            return True
        else:
            print('!!ERROR!! Invalid input for "B"!!')
            print('!!"B" must be in the range 1-26!!')
            return False

    def validate_a_quiet(self, a):
        if a % 2 != 0 and a != 13 and a in range(self.alpha_size):
            return True

    def validate_b_quiet(self, b):
        if b in range(self.alpha_size):
            return True

    def encrypt(self, plaintext):
        a = input('A value: ')
        b = input('B value: ')

        ciphertext = ""

        if self.validate_a(a) is True and self.validate_b(b) is True:
            a = int(a)
            b = int(b)

            for char in plaintext:
                if char.islower():
                    x = (ord(char) - ord('a')) % self.alpha_size
                    new_char = (a * x + b) % self.alpha_size
                    ciphertext += chr(int(new_char) + ord('a'))
                elif char.isupper():
                    x = (ord(char) - ord('A')) % self.alpha_size
                    new_char = (a * x + b) % self.alpha_size
                    ciphertext += chr(int(new_char) + ord('A'))
                else:
                    ciphertext += char
            
        print(f'Ciphertext: {ciphertext}')
    
    def decrypt(self, ciphertext):

        for a in range(self.alpha_size):
            if self.validate_a_quiet(a) is True:
                inv_a = self.mod_inv(a)
                for b in range(self.alpha_size):
                    if self.validate_b_quiet(b) is True:  
                        plaintext = "" 
                        for char in ciphertext:
                            if char.islower():
                                x = (ord(char) - ord('a')) % self.alpha_size
                                new_char = (inv_a * (x - b)) % self.alpha_size
                                plaintext += chr(new_char + ord('a'))
                            elif char.isupper():
                                x = (ord(char) - ord('A')) % self.alpha_size
                                new_char = (inv_a * (x - b)) % self.alpha_size
                                plaintext += chr(new_char + ord('A'))
                            else:
                                plaintext += char
                    
                    print(f"Encryption Key 'A':{a} | 'B':{b} | Decription Key 'Inverse A': {inv_a} | Text: {plaintext} \n")