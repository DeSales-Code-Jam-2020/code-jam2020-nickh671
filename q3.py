import math

def main(int1, int2):
    result = ''
    gcd = math.gcd(int1, int2)
    top = int1 / gcd
    bottom = int2 / gcd
    result = 'The reduced fraction is: {:.0f}/{:.0f}'.format(top, bottom)
    return result

if __name__ == "__main__":
    print(
        main(
            int(input("Enter numerator: ")),
            int(input("Enter denominator: "))
        )
    )