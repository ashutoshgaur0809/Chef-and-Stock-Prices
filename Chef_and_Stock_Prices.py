for i in range(int(input())):
    S ,A,B, C = map(int,input().split())
    a = S * C/100
    b = S + a
    if b >= A and b < B:
        print("YES")
    else:
        print("NO")   