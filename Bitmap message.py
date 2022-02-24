import sys

bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""











print('Bitmap Message, by Thomas Amick (adapted from a program by Al Swiegart')
print('Enter the message to display with the bitmap.')
message = input('> ')
if message == '':
    print("You dun goofed. Make sure to enter some kind of message")
    sys.exit()
# Loop over each line in the bitmap:
for line in bitmap.splitlines():
    # Loop over each character in the line:
    for i, bit in enumerate(line):
        if bit == ' ':
            #Print an empty space since there's a space in the bitmap:
            print(' ', end='')
        else:
            #Print a character from the message:
            print(message[i % len(message)], end='')
    print() #Print a newline
