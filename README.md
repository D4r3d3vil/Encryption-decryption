<h2>Requirements:</h2><br>
python 3.0 or higher
<br>
<h2>usage</h2>
First run:<br>'python encryption.py'<br><br>and get your encrypted text and decryption code.<br><br>then, run:<br>'python decryption.py'<br><br>and supply the encrypted text and decryption code.
<br><h2>
how it wroks:
</h2>
<h4>Encryption.py:</h4><br>
generates a random number for every character that is supplied in the input and puts it in a list lets call this decryption key.<br>
then it takes the desired text and for each letter in that text it appends a value in a list which is the index of value of the letter in the previous list + 1.<br>
this is so because i refrained from using a dictionary by making a value the item after the random number lets call this encrypted text.<br><br>
<h4>Decryption.py:</h4><br>
asks for the randomly generated decryption key and the encrypted text and then replaces every item in the encrypted text list (all of them are random.random() numbers) and replaces it with the index of the value of the letter in the decryption key + 1 to get a letter to add that to a string, which is later printed on to the screen.
