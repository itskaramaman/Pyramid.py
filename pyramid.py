n = int(input('Enter the length of pyramind you want '))
for i in range(n+1):
    for j in range(2*n):
        if j >= n-(i-1) and j <= n+(i-1):
            print('*', end='')
        else:
            print(' ', end='')
    print()
