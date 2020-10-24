def main(str1, str2):
    same = True
    first = str1[0]
    for char in str1:
        if str1[1] != first:
            same = False
    
    if same == False:
        reverse = str1[::-1]
        count = str1.count(str2)
        count2 = reverse.count(str2)
        return count + count2
    else:
        count = len(str1) + len(str2) - 1
        return count

if __name__ == "__main__":
    print(
        main(
            input("Input string: "),
            input("Input substring: ")
        )
    )