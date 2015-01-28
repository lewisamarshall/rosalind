def mendel(k, m, n):
    k = float(k)
    m = float(m)
    n = float(n)
    pop = k + m + n
    # chance = 0
    # chance += k/pop
    # chance += (m/pop) * ((m-1)/(pop-1))*3./4.
    # chance += (m/pop) * ((n/pop-1))/2.
    # chance += (1-k/pop)*(k/(pop-1))
    # chance += (n/pop) * (m/(pop-1))/2.

    kk = k/pop * (k-1)/(pop-1)
    km = k/pop * (m)/(pop-1) + m/pop * k/(pop-1)
    kn = k/pop * (n)/(pop-1) + n/pop * k/(pop-1)
    mm = m/pop * (m-1)/(pop-1)
    mn = m/pop * (n)/(pop-1) + n/pop * m/(pop-1)
    # nn = 0
    return kk + km + kn + mm *3./4. + mn/2.

print mendel(21, 24, 18)
