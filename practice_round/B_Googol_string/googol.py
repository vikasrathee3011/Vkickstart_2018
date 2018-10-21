def string(K):
    n = 1
    while n*2 <= K:
        n *= 2
    if n == K:
        return 0
    return(1 - string(n*2 - K))

def Googol_string():
    T = int(input())
    for i in range(T):
        print("Case #{}: {}".format(i+1, string(int(input()))))
Googol_string()
