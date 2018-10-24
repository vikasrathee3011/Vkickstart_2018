# please read the readme file to fully understand this programm
# don't care about unfruit-full names of the varialbe, they are as it is as in question

def Scrambled():
    T = int(input())                                # T test case happens
    for i in range(T):
        N = int(input())                            # N number of flights taken
        A = []                                      # list A contains Departature stations
        B = []                                      # list B contains Arrivals stations
        series = {}                                 # dict series contains both list A as value and B as its keys
        result = ""                                 # the final result
        for j in range(N):
            A.append(input())
            B.append(input())
            series[A[-1]] = B[-1]                   # appending the A as the value and B as the key in dict series
        for a in A:
            if a not in B:
                start = a                           # getting the first stattion of the trip from where the trip has been started
        for j in range(N):
            result += start+"-"+series[start]+" "   # getting all stations in series [the main algorithm]
            start = series[start]
        print(result)
Scrambled()


#   few important things are:
#       here the time complexcity is order of TN, "O(TN)" if you can find the technique to decrease its time than you are welcome.
#       as I have written this code for beginners, but have you think a little beyond it, here I have created a dictonary do you really need this,
#       think of it. the solution is:

# now start form the first:
#                           when we are inputing the stations we have taken them in A and B as described above here the length of each element is 1 and there are total 10 elements,
#                           now make pairs of stations onthe behalf of theirs 'comming' and 'gone' and then make a final list called 'result' now the lengh is 2 means one pair and the total elements are 10 again,
#                           again take each pair and check its first element by the last element of all others in the list, then make new pairs now the there are 2 pairs together in a group as a new elemens and total elements are 9
#                           do so on... and updating every time the list and getting elements decrease finally you will one element in the list
#                           which elements takes all paris together and is final result in the required order
#     check out this solution in your code and post it here
