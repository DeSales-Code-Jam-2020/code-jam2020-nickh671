def main(int1):       
    while int1 > 0:

        if (int1 - 1) % 5 == 0:
            print('I take 1 stones.')
            int1 -= 1
        elif (int1 - 2) % 5 == 0:
            print('I take 2 stones.')
            int1 -= 2
        elif (int1 - 3) % 5 == 0:
            print('I take 3 stones.')
            int1 -= 3
        elif (int1 - 4) % 5 == 0:
            print('I take 4 stones.')
            int1 -= 4
        else:
            print('I take 1 stones.')
            int1 -= 1
        if int1 < 1:
            return 'I win!'
        else:
            print('There are {} stones'.format(int1))
        user = int(input('How many will you take? (1-4) '))
        int1 -= user
        if int1 < 1:
            return 'Congratulations -- you win!'
        else:
            print('That leaves {} stones.'.format(int1))

        
if __name__ == "__main__":
    print(
        main(
            int(input("Enter the initial number of stones: "))
        )
    )