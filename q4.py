def main(str1):
    result = ''
    shift = ''
    start = 0
    for i in range(len(str1)):
        if str1[i] not in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            shift += str1[i]
        else:
            start += i
            break

    if start == 0:
        result += str1
        result += 'ay'
        return result
    else:

        while start < len(str1):
            result += str1[start]
            start += 1


        result += shift
        result += 'ay'
        return result

if __name__ == "__main__":
    print(
        main(
            input("Enter a word: ")
        )
    )