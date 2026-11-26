"""Finite checks for q-ary Abelian-border return-count enumeration.
Standalone stdlib; formulas are also established for arbitrary lengths in RESULT.md.
"""
from collections import Counter
from itertools import product
from math import factorial, sqrt, pi


def compositions(total, q):
    if q == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for rest in compositions(total - first, q - 1):
                yield (first,) + rest


def return_counts(q, limit):
    u = []
    for j in range(limit + 1):
        v = 0
        for c in compositions(j, q):
            multinomial = factorial(j)
            for a in c:
                multinomial //= factorial(a)
            v += multinomial * multinomial
        u.append(v)
    # First positive return excursions, from 1 - 1/U.
    f = [0] * (limit + 1)
    for j in range(1, limit + 1):
        f[j] = u[j] - sum(f[i] * u[j - i] for i in range(1, j))
    # Last (possibly empty) return-free tail: 1 / ((1-q^2 z) U).
    t = [0] * (limit + 1)
    t[0] = 1
    for j in range(1, limit + 1):
        t[j] = q*q*t[j-1] - f[j]
    coeffs = []
    fpow = [1] + [0] * limit
    for r in range(limit + 1):
        coeffs.append([sum(fpow[i]*t[m-i] for i in range(m+1)) for m in range(limit+1)])
        fpow = [sum(f[i]*fpow[j-i] for i in range(1, j+1)) for j in range(limit+1)]
    return u, f, t, coeffs


def direct_distribution(q, m, odd=False):
    n = 2*m + int(odd)
    ans = [0] * (m+1)
    for word in product(range(q), repeat=n):
        borders = 0
        for j in range(1, m+1):
            borders += (Counter(word[:j]) == Counter(word[-j:]))
        ans[borders] += 1
    return ans



def direct_full_distribution(q, m, odd=False):
    n = 2*m + int(odd)
    ans = [0] * max(1,n)
    for word in product(range(q), repeat=n):
        borders = 0
        for j in range(1, n):
            borders += Counter(word[:j]) == Counter(word[-j:])
        ans[borders] += 1
    return ans


def full_distribution(q, m, odd=False):
    u, f, t, _ = return_counts(q,m)
    fpow = [[1] + [0]*m]
    for r in range(1,m+1):
        last=fpow[-1]
        fpow.append([sum(f[i]*last[j-i] for i in range(1,j+1)) for j in range(m+1)])
    arr=[0]*max(1, 2*m + int(odd))
    for r in range(m+1):
        if odd:
            arr[2*r] += q*sum(fpow[r][j]*t[m-j] for j in range(m+1))
        else:
            if 2*r < len(arr):
                arr[2*r] += sum(fpow[r][j]*t[m-j] for j in range(m)) if m else (r==0)
            if r>=1:
                arr[2*r-1] += fpow[r][m]
    return arr

def main():
    for q, lim in ((2, 6), (3, 5), (4, 4)):
        u, f, t, coeffs = return_counts(q, lim)
        for m in range(lim + 1):
            formula = [coeffs[r][m] for r in range(m+1)]
            assert sum(formula) == q ** (2*m), (q,m,formula)
            assert formula == direct_distribution(q, m), (q,m,formula,direct_distribution(q,m))
            assert formula[0] == t[m]
            if m <= 3:
                assert [q*a for a in formula] == direct_distribution(q, m, odd=True)
            if m <= 4:
                assert full_distribution(q,m) == direct_full_distribution(q,m), (q,m,full_distribution(q,m),direct_full_distribution(q,m))
            if m <= 3:
                assert full_distribution(q,m,odd=True) == direct_full_distribution(q,m,odd=True)
            if q == 2:
                from math import comb
                assert formula == [2**r * comb(2*m-r,m) for r in range(m+1)]
    u3, _, _, c3 = return_counts(3, 5)
    assert u3 == [1, 3, 15, 93, 639, 4653]
    assert [[c3[r][m] for r in range(m+1)] for m in range(1,6)] == [
        [6,3], [48,24,9], [402,210,90,27],
        [3438,1854,864,324,81], [29754,16434,8082,3402,1134,243]
    ]
    for m in (20,40,80):
        u = return_counts(3,m)[0][m]
        scaled = m*u/(9**m)
        assert abs(scaled-3*sqrt(3)/(4*pi)) < 0.025
    print('VERIFY_OK')

if __name__ == '__main__': main()
