decryption_key = eval(input("\ndecryption key: "))
encrypted_text = eval(input("encrypted text: "))
decrypted_text = ""
for i in range(len(encrypted_text)):
    decrypted_text += str(decryption_key[decryption_key.index(encrypted_text[i]) + 1])
print(decrypted_text)