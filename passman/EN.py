from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import binascii
from Crypto.Random import get_random_bytes

#iv = b"23456789"
key = input('Please enter a 8 byte key: ').encode('utf-8')
print('Please select option:\n1. Encryption\n2. Decryption\n3. Exit')


while True:
    user_choice = input("Choose a option: ")
    if user_choice == "1":
        data = input('Enter the text: ').encode('utf-8')  # 9 bytes
        cipher1 = AES.new(key, AES.MODE_ECB)
        ct = cipher1.encrypt(pad(data, 16)).hex()
        print(f'The cipher text is: {ct}.')

    elif user_choice == "2":
        hex_value = input('Enter the cipher text: ')
        cip_txt = binascii.unhexlify(hex_value) # #cip_txt = bytes.fromhex(f'{hex_value}')
        cipher2 = AES.new(key, AES.MODE_ECB)
        pt = unpad(cipher2.decrypt(cip_txt), 16)
        print(f"The decrypted text is: {pt.decode('utf-8')}")


    elif user_choice == "3":
        print("Quitting The Program....")
        break

    else:
        print("Please Choose a correct option")
