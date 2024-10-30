#Numbers in inverted hollow right angled triangle
def Inverted_hollow(n):
    num = 1
    for i in range(n):
        patteren = ""
        for j in range(n-i):
            if i == 0:
                patteren += str(num) + " "
                num += 1
            else:
                if j == 0 or j ==n-i-1:
                    patteren += str(num) + ' '
                    num += 1
                else:
                    patteren +=  '  '
                    num += 1
        print(patteren)
n =int(input("Enter a number: "))
Inverted_hollow(n)