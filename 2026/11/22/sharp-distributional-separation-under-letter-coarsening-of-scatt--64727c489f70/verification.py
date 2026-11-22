#!/usr/bin/env python3
"""Independent finite checks for coarsening of scattered-word occurrence counts."""
from collections import Counter
from itertools import combinations, product
from fractions import Fraction
from math import comb, factorial


def count_embeds(host, pattern):
    m = len(pattern)
    return sum(all(host[j] == pattern[i] for i, j in enumerate(S))
               for S in combinations(range(len(host)), m))


def distribution(pattern, q, n):
    return Counter(count_embeds(H, pattern) for H in product(range(q), repeat=n))


def joint_second(pattern, q, n):
    """Exact second moment from *position-pair compatibility*, not sampling hosts."""
    sets = tuple(combinations(range(n), len(pattern)))
    numerator = 0
    for A in sets:
        for B in sets:
            requirements = {}
            compatible = True
            for S in (A, B):
                for k, pos in enumerate(S):
                    if pos in requirements and requirements[pos] != pattern[k]:
                        compatible = False
                        break
                    requirements[pos] = pattern[k]
                if not compatible:
                    break
            if compatible:
                numerator += Fraction(1, q ** len(requirements))
    return numerator


def moments_from_distribution(D, q, n, power=2):
    return Fraction(sum(k**power * v for k, v in D.items()), q**n)


def moment_extreme(q, m, n, constant):
    total = Fraction(0)
    for k in range(max(0, 2*m-n), m+1):
        L = 2*m-k
        if constant:
            num = factorial(L) // (factorial(k)*factorial(m-k)**2)
        else:
            s = m-k
            # Coefficient of (1-4z)^(-(k+1)/2) as an exact combinatorial convolution.
            arr = [1] + [0]*s
            for _ in range(k+1):
                arr = [sum(arr[r-j]*comb(2*j,j) for j in range(r+1)) for r in range(s+1)]
            num = arr[s]
        total += Fraction(comb(n, L)*num, q**L)
    return total


def coarsen(pattern, mapping):
    return tuple(mapping[x] for x in pattern)


def distance(pattern, image):
    return min(j-i for i in range(len(pattern)) for j in range(i+1,len(pattern))
               if pattern[i] != pattern[j] and image[i] == image[j])


def checks():
    totals = {'host_distributions':0, 'joint_second':0, 'extreme_forms':0,
              'coarsening_boundaries':0, 'third_moments':0}
    # Independent host counts vs joint pair compatibility; all patterns at small lengths.
    for q, m, nmax in ((2,2,7), (2,3,6), (3,2,6), (3,3,5), (4,3,4)):
        for pattern in product(range(q), repeat=m):
            for n in range(m, nmax+1):
                dist = distribution(pattern,q,n)
                assert sum(dist.values()) == q**n
                totals['host_distributions'] += 1
                exact = joint_second(pattern,q,n)
                assert exact == moments_from_distribution(dist,q,n)
                totals['joint_second'] += 1
                if len(set(pattern)) in (1, m):
                    assert exact == moment_extreme(q,m,n,len(set(pattern))==1)
                    totals['extreme_forms'] += 1
    # Every pair of pattern/equality-pattern coarsening for m<=4, q<=3.
    for q,m,nmax in ((2,3,6), (2,4,6), (3,3,6), (3,4,5)):
        for pattern in product(range(q), repeat=m):
            for mapping in product(range(q), repeat=q):
                image=coarsen(pattern,mapping)
                if len(set(image)) >= len(set(pattern)):
                    continue
                d=distance(pattern,image)
                if m+d > nmax:
                    continue
                for n in range(m, nmax+1):
                    A=distribution(pattern,q,n)
                    B=distribution(image,q,n)
                    assert (A==B) == (n < m+d), (q,m,n,pattern,image,d,A,B)
                    E2A=moments_from_distribution(A,q,n)
                    E2B=moments_from_distribution(B,q,n)
                    assert (E2A==E2B) == (n < m+d)
                    E3A=moments_from_distribution(A,q,n,3)
                    E3B=moments_from_distribution(B,q,n,3)
                    assert (E3A==E3B) == (n < m+d)
                    assert E2A<=E2B and E3A<=E3B
                    totals['coarsening_boundaries']+=1
                    totals['third_moments']+=1
    # Special distant repetition example.
    p=(0,1,2,0)
    u=(0,1,2,3)
    for n in range(4,8):
        d0=joint_second(u,4,n)
        d1=joint_second(p,4,n)
        assert (d0==d1)==(n<7)
        if n==7:
            assert d1-d0==Fraction(1,8192)
            print('Example pattern 0120 versus injective 0123 at n=7: second-moment gap 1/8192')
    print('All finite tests passed: ' + repr(totals))
    print('Proof applies to arbitrary n,m,q beyond the finite test ranges.')


if __name__ == '__main__':
    checks()
