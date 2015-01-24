def fibonocci(n, k=1):
    i = (0, 1)
    for j in range(n-1):
        i = (i[1], i[1] + k*i[0])
    return i[1]

if __name__ == '__main__':
    print fibonocci(31, 5)
