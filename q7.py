def main(str1):
    openbracket = 0
    closebracket = 0
    lastOpen = False
    balance = False
    illegal = False

    for char in str1:
        if char not in ['[', ']']:
            illegal = True
            break
        else:
            if char == '[':
                openbracket += 1 
            if char == ']':
                closebracket += 1

    if illegal:
        return 'Invalid character.'
    elif closebracket == openbracket:
        return 'Balanced.'
    else:
        return 'Not Balanced.'
        
if __name__ == "__main__":
    print(
        main(
            input("Enter string: ")
        )
    )