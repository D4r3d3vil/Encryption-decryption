import string, random
text = input("enter text: ")
charstr = text
fingerprint = []
chars = []
encrypted_text = []
for i in range(len(charstr)):
    chars.append(charstr[i])
for tr in range(len(charstr)):
        rnum = random.random()
        fingerprint.append(rnum)
        fingerprint.append(charstr[tr])
for ind in range(len(text)):
    encrypted_text.append(fingerprint[fingerprint.index(text[ind]) - 1])
print("\n"+ "decryption key (dont give this to anyone! (sensitive info may be leaked)):\n\n", str(fingerprint) + "\n\nencrypted text:\n\n" + str(encrypted_text) + "\n")