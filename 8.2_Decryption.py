'''
DECRYPTION PROGRAM
------------------
An ENCRYPTION program was used to generate the following secret code. The encryption program converted each character 
of the string into its ASCII decimal number, applied a +/-20 algorithm to it and then converted it back to
characters. Your task is to write a DECRYPTION program to decipher the following secret code. Don't waste time changing 
your program 40 times. Use a FOR loop from -20 to +20 to generate all the possibilities in one run of your program.

Extra Challenge: Instead of printing out 41 lines of text to look at, can you determine a way to just print out the
decrypted line only along with the shift number?
'''
# chr() gives ascii character
# ord() gives number
counter = -20
Secret_Message = "Lxwp{j}~uj}rxw|*)bx~)l{jltnm)}qn)lxmn7)]qn)ox{ln)r|)\][XWP)r}q)x~*"
for x in range(-20, 20):
    decrypt = ""
    for char in Secret_Message:
        letter = ord(char) + x
        temp = chr(letter)
        decrypt += temp
    if decrypt == "Congratulations! You cracked the code. The force is STRONG with you!":
        print("The secret message was:", decrypt)
        print("The shift number was {}.".format(counter))
    else:
        counter += 1
