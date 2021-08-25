test = int(input())
list = []
def check_num(a,b,c,i,j,k):
    len = ((a-i)**2 + (b-j)**2)
    dir_minus = (c-k)**2
    dir_plus = (c+k)**2
    if (a,b) == (i,j):
        if dir_minus == 0:
            return -1
        else:
            return 0
    else:
        if dir_plus < len:
            return 0
        elif dir_plus == len:
            return 1
        elif dir_plus > len:
            if dir_minus == len:
                return 1
            if dir_minus > len:
                return 0
            else:
                return 2

def print_ans(array):
    for i in range(test):
        print(array[i])

for i in range(test):
    x1,y1,r1,x2,y2,r2=(map(int,input().split()))
    list.append(check_num(x1,y1,r1,x2,y2,r2))

print_ans(list)