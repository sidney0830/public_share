def consist_count():
    count=0
    i=1
    N=int(input(">> input n="))

    while i<=N :    
        temp=i
        while temp>=10 :
            if (temp%10) == 7 :
                count=count+1
#                 print("temp==",temp)
            temp=temp//10
        if (temp%10) == 7 :
            count=count+1
#             print(temp)
        i=i+1
    print("f(N)====",count)
    
while (True):
    consist_count()