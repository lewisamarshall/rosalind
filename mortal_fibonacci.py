def mortal_fibonacci(n, m):
    k = [0]*(m-1) + [1]

    for i in range(n-1):
        k =k[1:] + [sum(k[:-1])]
        print k

    return sum(k)

if __name__ == '__main__':
    print mortal_fibonacci(88, 17)
