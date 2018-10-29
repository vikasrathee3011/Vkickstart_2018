# please read the readme file to fully understand this programm and for this question readme is must
# this program is for small practice only for large practice there is another program
# don't care about unfruit-full names of the varialbe, they are as it is as in question

def Sum_of_Sums():
    T = int(input())                                            # T test cases to entered
    for i in range(T):
        N,Q = map(int, input().split())                         # taking two input in 'int' for array and querry
        A = list(map(int,input().split()))                      # maping int elements of array in A
        a = 1
        c = 0
        B = list()
        while a <= N:
            for j in range(N-c):                                # check out this 'N-c' step here
                b = sum(A[j:j+a])                               #this loop is important to understand because it creat a another array for
                B.append(b)                                     # all the elements of sub array                
            a += 1
            c += 1
        B.sort()
        C = list()
        for j in range(Q):
            L,R = map(int, input().split())
            d = sum(B[L-1:R])                                   # another important loop is here getting querry and making a new array of
            C.append(d)                                         # the sums of the requested querries
        print("Case #{}:\n{}".format(i+1, '\n'.join(str(j) for j in C)))            # the desired format
Sum_of_Sums()


 
#few important things are:
#       here the time complexcity is order of iaj, "O(iaj)" if you can find the technique to decrease its time than you are welcome.
#       as I have written this code for beginners, but have you think a little beyond it, here I have created a another list B why we need it
#       and also you might have guess the pattern of new created array and loop execution, remeber that 'N-c' logic
#       in this program I have made it a havier by integratiing map and taking two inputs at a time
#       but if you see my series than you can easily understand it
