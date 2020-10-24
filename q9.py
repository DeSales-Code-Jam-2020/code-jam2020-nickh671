import collections

def main(str1, str2):
    word1 = collections.Counter(str1)
    word2 = collections.Counter(str2)

    if word1 == word2:
        return "The strings are anagrams."
    else:
        return "The strings are not anagrams."

if __name__ == "__main__":
    print(
        main(
            input("Enter first string: "),
            input("Enter second string: ")
        )
    )