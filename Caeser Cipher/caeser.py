def ceaser_cipher():
    print("""##INSTRUCTIONS##
==============================================
Encryption and decryption follow the same process:
1.) Paste your string into the prompt
2.) Pick an option out of the 25 possibilities

NOTE: Decryption is done via brute force, you do not need the shift amount if you know what you are looking for
          """)

    original_text = input("Paste string here: ")
    
    for x in range(26):
        new_text = ""

        for char in original_text:

            if(char.islower()):
                new_char = chr((ord(char)-ord('a')+x)%26+ord('a'))
                new_text += new_char
            elif(char.isupper()):
                new_char = chr((ord(char)-ord('A')+x)%26+ord('A'))
                new_text += new_char
            else:
                new_char = char
                new_text += new_char

        print(f"+{x}: {new_text}\n")      
        
ceaser_cipher()