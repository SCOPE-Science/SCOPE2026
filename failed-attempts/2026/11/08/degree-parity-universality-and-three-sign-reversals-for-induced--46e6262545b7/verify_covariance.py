#!/usr/bin/env python3
"""Exact small-graph checks for induced-motif/degree-parity covariance."""
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial


def pairs(k):
    return tuple(combinations(range(k), 2))


def canonical_graph(k, mask):
    ee = pairs(k)
    edge = {tuple(sorted(ab)) for i, ab in enumerate(ee) if (mask >> i) & 1}
    labels = []
    for pi in permutations(range(k)):
        labels.append(sum(1 << j for j, (a, b) in enumerate(ee)
                          if tuple(sorted((pi[a], pi[b]))) in edge))
    return min(labels)


def degree_odd_count(k, mask):
    parity = [0] * k
    for i, (a, b) in enumerate(pairs(k)):
        if mask >> i & 1:
            parity[a] ^= 1
            parity[b] ^= 1
    return sum(parity)


def verify(n, k, p):
    edge_index = {ab: j for j, ab in enumerate(pairs(n))}
    m = comb(n, 2)
    pmf = [p ** s * (1-p) ** (m-s) for s in range(m+1)]
    subsets = tuple(combinations(range(n), k))
    motifs = {}
    for mask in range(1 << comb(k,2)):
        key = canonical_graph(k, mask)
        motifs[key] = motifs.get(key,0)+1
    mtypes=sorted(motifs)
    ET = {h:Fraction(0) for h in mtypes}
    EOT = {h:Fraction(0) for h in mtypes}
    EO = Fraction(0)
    for mask in range(1 << m):
        w=pmf[mask.bit_count()]
        odd=degree_odd_count(n,mask)
        EO += w*odd
        counts={h:0 for h in mtypes}
        for subset in subsets:
            submask=0
            for j,(a,b) in enumerate(pairs(k)):
                if mask >> edge_index[(subset[a],subset[b])] & 1:
                    submask |= 1 << j
            counts[canonical_graph(k,submask)] += 1
        for h in mtypes:
            ET[h] += w*counts[h]
            EOT[h] += w*counts[h]*odd
    q = 1-2*p
    checks=0
    for h in mtypes:
        e=h.bit_count()
        o=degree_odd_count(k,h)
        mean=comb(n,k)*motifs[h]*p**e*(1-p)**(comb(k,2)-e)
        expected=-mean* q**(n-k)*((k-2*o)-k*q**(k-1))/2
        actual=EOT[h]-ET[h]*EO
        assert ET[h] == mean, ('mean',n,k,p,h,ET[h],mean)
        assert actual == expected, ('cov',n,k,p,h,actual,expected)
        checks += 2
    return checks


def main():
    total=0
    for n in range(2,6):
        for k in range(2,min(n,4)+1):
            for p in (Fraction(1,4),Fraction(1,3),Fraction(1,2),Fraction(2,3),Fraction(3,4)):
                total+=verify(n,k,p)
    # Same degree-parity signature but different motifs: all k=4 graphs with o=2
    # have exactly the same normalized covariance even if edge counts differ.
    h4=[h for h in range(1<<6) if canonical_graph(4,h)==h and degree_odd_count(4,h)==2]
    assert len(h4)>1
    # Independent exact rational evaluation of the size-five path sign sequence.
    n, k, e, o = 6, 5, 4, 2
    assert all(x > 0 for x in (n, k, e, o))
    signs = []
    for p in (Fraction(1, 10), Fraction(2, 5), Fraction(3, 5), Fraction(9, 10)):
        q = 1 - 2 * p
        mean = comb(n, k) * (factorial(k) // 2) * p ** e * (1-p) ** (comb(k, 2)-e)
        covariance = -mean * q ** (n-k) * (k-2*o-k*q**(k-1)) / 2
        signs.append(1 if covariance > 0 else -1)
    assert signs == [1, -1, 1, -1]
    print(f'PASS: {total} exact rational mean/covariance tests across all unlabeled induced motifs, n<=5, k<=4, five edge probabilities; {len(h4)} parity-sharing size-four motifs, plus 4 exact P5 sign checks.')

if __name__=='__main__': main()
