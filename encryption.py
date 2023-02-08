import random
text = input("enter text: ")
charstr = text
fingerprint = []
chars = []
encrypted_text = []
for i in range(len(charstr)):
    if not charstr[i] in chars: 
        chars.append(charstr[i])
for tr in range(len(chars)):
        rnum = random.random()
        fingerprint.append(rnum)
        fingerprint.append(chars[tr])
for ind in range(len(text)):
    encrypted_text.append(fingerprint[fingerprint.index(text[ind]) - 1])
print("\n"+ "decryption key (dont give this to anyone! (sensitive info may be leaked)):\n\n", str(fingerprint) + "\n\nencrypted text:\n\n" + str(encrypted_text) + "\n")
