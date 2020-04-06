def encryption(Str,shift_val):
    encrypt = ""
    for char in Str:
        if not char.isalpha():
            encrypt += char
            continue
        elif char == char.upper():
            code = ord(char)
            if code + shift_val<=90:
                code += shift_val 
                encrypt += chr(code)
            elif code + shift_val>90:
                code += shift_val
                code = code - 90
                code += 64
                encrypt += chr(code)
        elif char == char.lower():
            code = ord(char)
            if code + shift_val<=122:
                code += shift_val 
                encrypt += chr(code)
            elif code + shift_val>122:
                code += shift_val
                code = code - 122
                code += 96
                encrypt += chr(code)
                
            
    print(encrypt)


try:    
    Str = input("Enter the string you need to encrypt : ")
    shift_val = int(input("Enter the shift-value between range (1-25) : "))
    assert shift_val>=1
    assert shift_val<=25
    encryption(Str,shift_val)
except ValueError:
    print("<<<<<========================================>>>>>")
    print("You entered invalid values. Use only integer values.")
except:
    print("<<<<<========================================>>>>>")
    print("Entered shift value is out of range")
    

    
