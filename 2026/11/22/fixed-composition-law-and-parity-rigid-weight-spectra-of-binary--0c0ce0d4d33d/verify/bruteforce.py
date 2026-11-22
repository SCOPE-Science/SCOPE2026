"""Direct exhaustive comparison of binary Abelian-border weight spectra."""
from collections import Counter
from math import comb


def formula(n):
    if n == 1:
        return {0: 1, 1: 1}
    m = n // 2
    values = Counter()
    for j in range(m):
        values[2*j+1] += 2*comb(m-1,j)**2
    for j in range(m-1):
        values[2*j+2] += 2*comb(m-1,j)*comb(m-1,j+1)
    if n % 2:
        old = dict(values)
        values = Counter()
        for k,v in old.items():
            values[k] += v
            values[k+1] += v
    return dict(values)


def direct(n):
    values = Counter()
    for mask in range(1 << n):
        w = [(mask >> i)&1 for i in range(n)]
        left = right = 0
        for j in range(n//2):
            left += w[j]
            right += w[n-1-j]
            if left == right:
                break
        else:
            values[sum(w)] += 1
    return dict(values)


def verify():
    for n in range(1,19):
        expected = formula(n)
        observed = direct(n)
        assert expected == observed, (n,expected,observed)
    print('PASS: exhaustive 1 <= n <= 18 (524,286 binary strings in total)')

if __name__=='__main__':verify()
