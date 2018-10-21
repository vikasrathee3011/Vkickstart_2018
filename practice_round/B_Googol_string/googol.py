# please read the readme file to fully understand this programm
# don't care about unfruit-full names of the varialbe, they are as it is as in question


def string(K):                                  # this function contain the main algorithm taking argument K
    n = 1                                       # n is element through which we define the len of the string and checking our variable K belongs from where
    while n*2 <= K:                             # we will increase n as a power of 2 because the string is always in a pattern which is '2^n - 1'
        n *= 2
    if n == K:                                  #  whenever n become K the answer is 0 because in string 2^n is the middle element and it is always zero act as a sperator
        return 0
    return(1 - string(n*2 - K))                 # the key part of algotrithm: we are substracting K from n*2 because we need to reduce the value upto its base case
                                                # and make K as small as posiible
def Googol_string():
    T = int(input())
    for i in range(T):                          # getting T test cases and iterate them through the loop
        print("Case #{}: {}".format(i+1, string(int(input()))))
Googol_string()


#   few important things are:
#       the key part for this code is to find the correct pattern and possible recursion in the string
#       here the time complexcity is order of n^2, "O(n^2)" if you can find the technique to decrease its time than you are welcome.
#       have you seen the size of the code is really small and it can be more if have better ideas, the program cna be done also by creating a list, in which first you have to append all the element of K in a list and later on traverse them using a for loop
#       but this cozy made your program clear and comapct as possible.
