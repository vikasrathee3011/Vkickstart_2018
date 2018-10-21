in the link below full description of the quesiton is given:
https://codejam.withgoogle.com/codejam/contest/4374486/dashboard#s=p1

there are two fies realated to this code you can find them below there in the repository called "small-practice" and "large-practice" for testing this programm

use command given below to run this programm and the output file will generated in in same folder:
python googol.py < A-small-practice.txt > small-out.txt   for the small file
python googol.py < A_large_practice.txt > large-out.txt   for the large one

after running the  file and getting the output there below in the same repository you will find the answer for the both dataset and you can can tell them from there

now let us discuss the string pattern:
a = 001 and b = 011 the formula is: 'a'+'0'+'b'
now expand them further you will get;
a0b0a1b0a0b1a1b0a0b0a1b0a0b1a1b this string represnts '2^16-1' notice one thing if you extract all '0' and '1' then again you wil get

001 0 011 0 001 1 011 which again noting but:
a0b0a1b and so on you will always get this series

means our base cases are 'a' and 'b' and we have to reduce all the big terms to our base cases and than simply count:
1 = '0'
2 = '0'
3 = '1' and its reverse
