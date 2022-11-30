'''
MONTHS PROGRAM
--------------
Write a user-input statement where a user enters a month number 1-12.
From the user input number, slice the string below in your program to print the three month abbreviation.
Keep repeating this until the user enters a non 1-12 number to quit.
Once the user quits, print "Goodbye!"
'''
done = False
while not done:
    number = int(input("Enter a number 1-12 for a corresponding month, or an invalid number to exit the program."))
    if number < 0 or number > 12:
        done = True
        break
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"
    a = (number - 1) * 3
    z = a + 3
    print(months[a:z])
print("You have exited.")

