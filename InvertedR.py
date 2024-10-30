def Inverted_Hollow(s,n):
    
    for i in range(n):
        pattern = "  " * i
        for j in range(n-i):
            if i == 0:
                pattern += str(s) + " "
                s += 1
            else:
                if j ==0 or j == n-i-1:
                    pattern += str(s) + " "
                    s += 1
                else:
                    pattern += " "
        print(pattern.rstrip())

s = int(input("Initial number: "))
n = int(input("Number of rows: "))
Inverted_Hollow(s,n)
        
    