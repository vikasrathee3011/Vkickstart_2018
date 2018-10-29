def Sum_of_Sums():
    T = int(input())
    for i in range(T):
        N,Q = map(int, input().split())
        A = list(map(int,input().split()))
        a = 1
        c = 0
        B = list()
        while a <= N:
            for j in range(N-c):
                b = sum(A[j:j+a])
                B.append(b)
            a += 1
            c += 1
        B.sort()
        C = list()
        for j in range(Q):
            L,R = map(int, input().split())
            d = sum(B[L-1:R])
            C.append(d)
        print("Case #{}:\n{}".format(i+1, '\n'.join(str(j) for j in C)))
Sum_of_Sums()
