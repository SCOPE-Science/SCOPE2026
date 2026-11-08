"""Exact, dependency-free verification of a local-peak/cycle covariance law.

Runs exhaustive enumeration for n = 3,...,8, all position triples,
plus checks a conditional cycle-contraction identity on n <= 6.
The theorem for arbitrary n is proved separately in RESULT.md.
"""
from fractions import Fraction
from itertools import permutations, combinations
from math import factorial

checks = 0
for n in range(3, 9):
    triples = list(combinations(range(1, n + 1), 3))
    cycles_sum = 0
    peak_cycle = {t: 0 for t in triples}
    for perm in permutations(range(1, n + 1)):
        seen = set()
        c = 0
        for start in range(1, n + 1):
            if start not in seen:
                c += 1
                x = start
                while x not in seen:
                    seen.add(x)
                    x = perm[x-1]
        cycles_sum += c
        for t in triples:
            i, j, k = t
            if perm[i-1] < perm[j-1] > perm[k-1]:
                peak_cycle[t] += c
    avg = Fraction(cycles_sum, factorial(n))
    assert avg == sum((Fraction(1, t) for t in range(1,n+1)),Fraction(0))
    checks += 1
    for i, j, k in triples:
        empirical = Fraction(peak_cycle[i,j,k], factorial(n)) - avg / 3
        numerator = -3*i*i + 9*i + 6*j*j - 18*j - 3*k*k + 9*k + 2
        predicted = Fraction(numerator, 6*n*(n-1)*(n-2))
        assert empirical == predicted, (n,i,j,k,empirical,predicted)
        checks += 1

# Check the key partial-injection contraction rule on every prescription
# of three mapped positions, exhaustive for n <= 6.
for n in range(3, 7):
    all_perm = list(permutations(range(1,n+1)))
    hn3 = sum((Fraction(1,t) for t in range(1,n-2)),Fraction(0))
    for domains in combinations(range(1,n+1),3):
        for images in permutations(range(1,n+1),3):
            forced = dict(zip(domains,images))
            domain_set = set(domains)
            r = 0
            for start in domains:
                v = forced[start]
                steps = 1
                while v in domain_set and v != start and steps <= 3:
                    v = forced[v]
                    steps += 1
                if v == start:
                    r += Fraction(1, steps)
            # r counts each length-L forced cycle with 1/L per starting vertex
            r = int(r)
            subtotal = 0
            count = 0
            for p in all_perm:
                if all(p[u-1] == val for u,val in forced.items()):
                    count += 1
                    seen = set()
                    c = 0
                    for a in range(1,n+1):
                        if a not in seen:
                            c += 1
                            b=a
                            while b not in seen:
                                seen.add(b)
                                b=p[b-1]
                    subtotal += c
            assert count == factorial(n-3)
            assert Fraction(subtotal,count) == hn3+r,(n,domains,images,r)
            checks += 1

# First sign change: no positive covariances for n=3,4, but both signs for n=5.
for n in (3,4):
    assert all(-3*i*i+9*i+6*j*j-18*j-3*k*k+9*k+2 <= 0
               for i,j,k in combinations(range(1,n+1),3))
    checks+=1
assert -3*1+9+6*4**2-18*4-3*5**2+9*5+2 == 2
checks+=1

print(f'VERIFY_OK {checks} exact assertions')
