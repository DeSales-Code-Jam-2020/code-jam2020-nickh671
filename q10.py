def main(str1, str2, int1):
    for i in range(len(str1)):
        if str1[i] == 'A':
            if str2[i].isdigit():
                return "Invalid plate number"
        elif str1[1] == 'N':
            if str2[i].isalpha():
                return "Invalid plate number"

    last = str2[len(str2)-1]

    result = str2[:-1]
    result += chr(ord(last) + int1)
    return result

if __name__ == "__main__":
    print(
        main(
            input("Input\n"),
            input(),
            int(input())
        )
    )