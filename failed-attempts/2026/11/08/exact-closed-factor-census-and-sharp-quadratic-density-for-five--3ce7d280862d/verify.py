#!/usr/bin/env python3
"""Independent finite checks for closed-factor counts of five-run binary words.
All runtime requirements are Python standard library only.
Finite tests support, but do not prove, the universal assertions.
"""
from itertools import product
from random import Random


def direct_closed(u):
    if len(u) <= 1:
        return True
    for k in range(1, len(u)):
        border = u[:k]
        if u[-k:] == border:
            occurrences = sum(u[i:i+k] == border for i in range(len(u)-k+1))
            if occurrences == 2:
                return True
    return False


def direct_count(w):
    factors = {''}
    for i in range(len(w)):
        for j in range(i+1, len(w)+1):
            sub = w[i:j]
            if direct_closed(sub):
                factors.add(sub)
    return len(factors)


def proposed(a, b, c, d, e):
    x, y, z = min(a, c), min(c, e), min(b, d)
    n = a+b+c+d+e
    return n+1+z*(x+y)+(x*y-min(x,y) if b == d else 0)


def word(a,b,c,d,e):
    return '0'*a+'1'*b+'0'*c+'1'*d+'0'*e


def main():
    cases = 0
    for t in product(range(1, 6), repeat=5):
        assert direct_count(word(*t)) == proposed(*t), t
        cases += 1
    rng = Random(20130528)
    for _ in range(160):
        t = tuple(rng.randint(1, 13) for j in range(5))
        assert direct_count(word(*t)) == proposed(*t), t
        cases += 1
    for k in range(1, 25):
        a,b,c,d,e = 2*k,k,2*k,k,2*k
        n=8*k
        assert proposed(a,b,c,d,e) == 8*k*k+6*k+1
        assert proposed(a,b,c,d,e) <= n*n/8+n+1
    # Brute maxima for small lengths; optimize only over exactly five runs.
    maxima = []
    for n in range(5, 18):
        values = []
        for a in range(1,n-3):
            for b in range(1,n-a-2):
                for c in range(1,n-a-b-1):
                    for d in range(1,n-a-b-c):
                        e = n-a-b-c-d
                        values.append(proposed(a,b,c,d,e))
        maxima.append(max(values))
    assert maxima == [8,9,12,15,17,21,24,27,32,35,40,45,48], maxima
    print('VERIFY_OK finite_five_run_parameter_cases='+str(cases)+' asymptotic_family_checks=24 small_length_maxima='+str(maxima))


if __name__ == '__main__':
    main()
