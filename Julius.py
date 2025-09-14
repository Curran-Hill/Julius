import argparse

from CaesarCipher.caeser import CaesarCipher
from AffineCipher.affine import AffineCipher

parser = argparse.ArgumentParser()

function_group = parser.add_argument_group(title='Functionality')
cipher_group = parser.add_argument_group(title='Cipher Options')

function_group_exclusive = function_group.add_mutually_exclusive_group(required=True)
cipher_group_exclusive = cipher_group.add_mutually_exclusive_group(required=True)

function_group_exclusive.add_argument('-E', '--encrypt', help='Option for encryption', action='store_true')
function_group_exclusive.add_argument('-D', '--decrypt', help='Option for decryption', action='store_true')

cipher_group_exclusive.add_argument('-c', '--Caesar', help='Caesar cipher', action='store_true')
cipher_group_exclusive.add_argument('-a', '--Affine', help='Affine cipher', action='store_true') 

parser.add_argument('INPUT', type=str, help='Ciphertext/Plaintext input') 

args = parser.parse_args()

if args.encrypt:
    if args.Caesar:
        plain = CaesarCipher()
        plain.encrypt(args.INPUT)

    elif args.Affine:
        plain = AffineCipher()
        plain.encrypt(args.INPUT)

elif args.decrypt:
    if args.Caesar:
        cipher = CaesarCipher()
        cipher.decrypt(args.INPUT)
    
    if args.Affine:
        cipher = AffineCipher()
        cipher.decrypt(args.INPUT)