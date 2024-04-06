def hex_char_decode(digit):
    if (digit == '0'):
        return 0
    elif (digit == '1'):
        return 1
    elif (digit == '2'):
        return 2
    elif (digit == '3'):
        return 3
    if (digit == '4'):
        return 4
    elif (digit == '5'):
        return 5
    elif (digit == '6'):
        return 6
    elif (digit == '7'):
        return 7
    elif (digit == '8'):
        return 8
    elif (digit == '9'):
        return 9
    elif (digit == 'A' or digit == 'a'):
        return 10
    elif (digit == 'B' or digit == 'b'):
        return 11
    elif (digit == 'C' or digit == 'c'):
        return 12
    elif (digit == 'D' or digit == 'd'):
        return 13
    elif (digit == 'E' or digit == 'e'):
        return 14
    elif (digit == 'F' or digit == 'f'):
        return 15
    else:
        return 0

def hex_string_decode(hex):
    sum = 0
    for i in range(len(hex)):
        sum += hex_char_decode(hex[i])*(16**(len(hex)-i-1))
    return sum

'''def decodeHex(string):
    hex = string
    hexCode = 0
    for i in range(len(hex)):
        numbers = "0123456789"
        for j in range (len(hex)):
            if numbers[j] == hex[i]:
                hexCode += int(hex[i])*(16**(len(hex)-i-1))
                break

        if(hex[i] == 'A' or hex[i] == 'a'):
            hexCode += 10*(16**(len(hex)-1 - i))
        elif(hex[i] == 'B' or hex[i] == 'b'):
            hexCode += 11*(16**(len(hex)-1 - i))
        elif(hex[i] == 'C' or hex[i] == 'c'):
            hexCode += 12*(16**(len(hex)-1 - i))
        elif(hex[i] == 'D' or hex[i] == 'd'):
            hexCode += 13*(16**(len(hex)-1 - i))
        elif(hex[i] == 'E' or hex[i] == 'e'):
            hexCode += 14*(16**(len(hex)-1 - i))
        elif(hex[i] == 'F' or hex[i] == 'f'):
            hexCode += 15*(16**(len(hex)-i-1))
        else:
            hexCode += 0
    return hexCode'''

def binary_string_decode(binary):
    adding = 0
    binaryCode = 0
    numbers = "0123456789"
    for i in range(len(binary)):
        for j in range(len(numbers)):
            if(binary[i] == numbers[j]):

                adding = ((2*(int(binary[i]))) ** (len(binary)-i-1))
                if((2*(int(binary[i]))) == 0 and (len(binary)-i-1) == 0):
                    adding -= 1
                binaryCode += adding

                break
    return binaryCode
def binary_to_hex(num):
    translatedCode = []
    hex = ""
    placement = 0
    number = 0
    decimal = binary_string_decode(num)
    while decimal > 0:
        number = decimal%16
        if(number >= 0 and number <= 9):
            translatedCode.append(str(number))
        elif (number == 10):
            translatedCode.append('A')
        elif (number == 11):
            translatedCode.append('B')
        elif (number == 12):
            translatedCode.append('C')
        elif (number == 13):
            translatedCode.append('D')
        elif (number == 14):
            translatedCode.append('E')
        elif (number == 15):
            translatedCode.append('F')

        decimal = decimal//16
        placement += 1

    return hex.join(translatedCode)[::-1]

def main():
    check = True

    while check:
        print("Decoding Menu\n-------------\n1. Decode hexadecimal\n2. Decode binary\n3. Convert binary to hexadecimal\n4. Quit")
        choice = int(input("Please enter an option: "))

        if choice == 1:
            code = input(("Please enter the numeric string to convert: "))
            print("Result:", str(hex_string_decode(code)))
        elif choice == 2:
            code = input(("Please enter the numeric string to convert: "))
            print("Result:", str(binary_string_decode(code)))
        elif choice == 3:
            code = input(("Please enter the numeric string to convert: "))
            print("Result:", binary_to_hex(code))
        elif choice == 4:
            
            check = False


if __name__ == "__main__":
    main()