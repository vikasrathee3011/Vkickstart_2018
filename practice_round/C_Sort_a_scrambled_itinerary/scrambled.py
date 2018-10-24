def Scrambled():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = []
        B = []
        series = {}
        result = ""
        for j in range(N):
            A.append(input())
            B.append(input())
            series[A[-1]] = B[-1]
        for a in A:
            if a not in B:
                start = a
        for j in range(N):
            result += start+"-"+series[start]+" "
            start = series[start]
        print(result)
Scrambled()            
