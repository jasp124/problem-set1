def CountOfNoOfBallsInPyramid(n):
    if n == 1:
        return 1
    else:
        print(n)
        return n + CountOfNoOfBallsInPyramid(n-1)

print(CountOfNoOfBallsInPyramid(5))