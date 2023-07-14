for x in range(int(input())):
    n=int(input())
    l1= list(map(int, input().split()))
    m=max(l1)
    for x in range(len(l1)+1):
        if len(l1)==0:
            print("Yes")
        elif m<=l1[0]:
            l1.remove(l1[-1])
            #print(l1,"f")
        elif m<=l1[-1]:
            l1.remove(l1[0])
            #print(l1)

        else:

            print("No")
            break
