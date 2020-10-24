def main(int1, int2, int3, int4, int5, int6, int7, int8):
    if int3 - int1 != 0:
        slope1 = (int4 - int2)/(int3 - int1)
    else:
        slope1 = 'undefined'
    if int5 - int3 != 0:
        slope2 = (int6 - int4)/(int5 - int3)
    else:
        slope2 = 'undefined'
    if int7 - int5 != 0:
        slope3 = (int8 - int6)/(int7 - int5)
    else:
        slope3 = 'undefined'
    
    
    if slope1 == slope2 and slope2 == slope3 and slope1 == slope3:
        return "The points are collinear"
    else:
        return "The points are not collinear"   
    
if __name__ == "__main__":
    print(
        main(
            # just trust me don't touch this - Jake Gadaleta
            *map(lambda x: int(x), input("Input: ").strip().split(" "))
        )
    )