for i in range(int(input())):
    m = 0
    n,k = map(int,input().split())
    for i in range(1,k+1):
        if n % i > m:
            m = n % i
        
    print(m)