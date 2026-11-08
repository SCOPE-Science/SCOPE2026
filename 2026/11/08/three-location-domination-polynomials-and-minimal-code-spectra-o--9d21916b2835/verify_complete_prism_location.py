#!/usr/bin/env python3
"""Direct exhaustive checks for three location-domination variants on K_2 square K_n.

Run: python3 verify_complete_prism_location.py
No third-party packages needed. Finite checks corroborate, but do not replace, the proof.
"""
from collections import Counter
from math import comb


def closed_neighborhoods(n):
    return [sum(1 << j for j in range(2 * n)
                if i // n == j // n or i % n == j % n)
            for i in range(2 * n)]


def literal_properties(mask, n, h):
    outsiders = [v for v in range(2*n) if not mask >> v & 1]
    sig = [h[v] & mask for v in outsiders]
    if 0 in sig:
        return (False, False, False)
    ordinary = len(set(sig)) == len(sig)
    solid = all((sig[i] & ~sig[j]) != 0
                for i in range(len(sig)) for j in range(len(sig)) if i != j)
    universe = (1 << (2*n))-1
    self_locating = True
    for v, signature in zip(outsiders, sig):
        shared = universe
        for c in range(2*n):
            if signature >> c & 1:
                shared &= h[c]
        if shared != (1 << v):
            self_locating = False
            break
    return (ordinary, solid, self_locating)


def structural_properties(mask, n):
    states = [(bool(mask >> j & 1), bool(mask >> (j+n) & 1))
              for j in range(n)]
    e = states.count((False, False))
    a = states.count((True, False))
    b = states.count((False, True))
    c = states.count((True, True))
    ordinary = e == 0 or (e == 1 and a+c > 0 and b+c > 0)
    solid = (e == 0 and not (c == 0 and (a == 1 or b == 1))) or (e == 1 and c == n-1)
    self_locating = e == 0 and a+c >= 2 and b+c >= 2
    return (ordinary, solid, self_locating)


def expected(n):
    f = Counter()
    for a in range(n+1):
        for b in range(n-a+1):
            c = n-a-b
            f[a+b+2*c] += comb(n,a) * comb(n-a,b)
    ord_ = f.copy()
    for a in range(n):
        for b in range(n-1-a+1):
            c = n-1-a-b
            ord_[a+b+2*c] += n*comb(n-1,a)*comb(n-1-a,b)
    ord_[n-1] -= 2*n
    solid = f.copy()
    solid[n] -= 2*n
    solid[2*n-2] += n
    self_ = f.copy()
    self_[n] -= 2*(n+1)
    self_[n+1] -= 2*n
    return (ord_,solid,self_)


def expected_minimal(n):
    return (Counter({n-1: n*(2**(n-1)-2), n: 2}),
            Counter({n: 2**n-2*n, 2*n-2: n}),
            Counter({n: 2**n-2*n-2}))


def main():
    total = 0
    for n in range(4,9):
        h = closed_neighborhoods(n)
        polynomials = [Counter(),Counter(),Counter()]
        code_sets = [set(),set(),set()]
        for mask in range(1 << (2*n)):
            literal = literal_properties(mask,n,h)
            structural = structural_properties(mask,n)
            assert literal == structural, (n,mask,literal,structural)
            for j in range(3):
                if literal[j]:
                    polynomials[j][mask.bit_count()] += 1
                    code_sets[j].add(mask)
        for j in range(3):
            formula = +expected(n)[j]
            assert +polynomials[j] == formula, (n,j,polynomials[j],formula)
            minimum = Counter()
            for mask in code_sets[j]:
                if all((mask^(1<<v)) not in code_sets[j] for v in range(2*n) if mask>>v&1):
                    minimum[mask.bit_count()] += 1
            assert +minimum == +expected_minimal(n)[j], (n,j,minimum,expected_minimal(n)[j])
        total += 1 << (2*n)
        print('PROFILE_OK n',n,'subsets',1<<(2*n),'LD',sum(polynomials[0].values()),
              'DLD',sum(polynomials[1].values()),'SLD',sum(polynomials[2].values()))
    print('VERIFY_OK profiles=5 all_subsets=',total,
          'literal_identifying_sets=PASS three_polynomials=PASS',
          'three_minimal_code_spectra=PASS structural_criteria=PASS')

if __name__=='__main__':
    main()
