a=input()
i=0
j=len(a)-1
while(i<j):
    if(a[i]!=a[j]):
        print("it is not a palindrome")
        break
    i=i+1
    j=j-1
else:
    print("It is a palindrome")