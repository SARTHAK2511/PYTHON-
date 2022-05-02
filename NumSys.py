
#Sarthak2511
'''Given an integer, , print the following values for each integer  from 0  to n (given int) :
1-Decimal
2-Octal
3-Hexadecimal (capitalized)
4-Binary
'''
a=int(input())
b=1
c=len(bin(a))-2
print(bin(a))
print("C = ",c)
while b<a+1:
    result = f"{str(b).rjust(c)} {oct(b)[2:].rjust(c)} {hex(b)[2:].rjust(c)} {bin(b)[2:].rjust(c)}"
    print(result)
    b+=1
