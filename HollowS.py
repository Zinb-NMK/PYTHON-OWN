def Hollow_square(s,n):
    space = 2 * n-3
    
    for i in range(1,n+1):
        pattern = ""
        
        for j in range(1,n+1):
            if i == 1 or i ==n:
                pattern += str(s) + " "
            else:
                pattern = str(s - n + 1) + " " * space + str(s)
            s+=1
        print(pattern)
    
s = int(input())
n = int(input())
Hollow_square(s,n)