# please read the readme file to fully understand this programm
# don't care about unfruit-full names of the varialbe, they are as it is as in question
def Gbus_Count():
    T = int(input())                            # T test cases to entered
    for i in range(T):
        if i == 0:
            N = int(input())                    # N number of gbuses available
        else:
            input()                             # taking the blank line input after the first test cases
            N = int(input())
        A = list(map(int, input().split()))     # taking input of all the reanges of gbuses and store them in a list
        P = int(input())                        # P number of cities are to be monitored
        C = list()  
        D = dict()
        for k in range(P):
            C.append(int(input()))              # getting all the cities to be monitored in a C list
        for m in range(P):
            for n in range(N):
                if A[2*n]<=C[m]<=A[2*n+1]:
                    if C[m] not in D:
                        D[C[m]] = 1
                    else:
                        D[C[m]] += 1            # storing all the results in a dictonary D
        print("Case #{}: {}".format(i+1, ' '.join(str(x) for x in D.values())))
Gbus_Count()


#   few important things are:
#       here the time complexcity is order of n^2, "O(n^2)" if you can find the technique to decrease its time than you are welcome.
#       as I have written this code for beginners, but have you think a little beyond it, here I have created a dictonary do you really need this,
#       think of it. the solution is:

#       D = list(), result = 0                              instead of dict we created a list and variable name result = 0
#       for m in range(P):
#           for in range(N):
#               if A[2*n]<=C[m]<=A[2*n+1]:
#                   result += 1
#               D.append(result)
#       print("Case #{}: {}".format(i+1, *D)
