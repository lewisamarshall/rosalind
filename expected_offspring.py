def expected_offspring(parents):
    parents = [float(i) for i in parents.split()]
    prob = 0
    chances = [1, 1, 1, 3./4., 1./2., 0]
    prob = sum([n * chance for n, chance in zip(parents, chances)])
    return prob * 2

if __name__ == '__main__':
    print expected_offspring('16121 17118 16974 17021 17423 19504')
