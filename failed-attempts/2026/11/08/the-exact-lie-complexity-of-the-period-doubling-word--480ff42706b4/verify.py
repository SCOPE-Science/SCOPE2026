#!/usr/bin/env python3
"""Finite-factor check of the period-doubling Lie-complexity law.
No external packages required. This does not replace the all-length proof.
"""
from itertools import product

def mu(s):
    return ''.join('01' if c == '0' else '00' for c in s)

def factors_exact(n):
    k = (n-1).bit_length()  # 2**k >= n
    words = ['00', '01', '10']
    for _ in range(k):
        words = [mu(s) for s in words]
    return {s[i:i+n] for s in words for i in range(len(s)-n+1)}

def lie_classes(factors, n):
    unseen = set(factors)
    ans = []
    while unseen:
        w = unseen.pop()
        doubles = w + w
        orbit = {doubles[i:i+n] for i in range(n)}
        unseen.difference_update(orbit)
        if orbit <= factors:
            ans.append(min(orbit))
    return sorted(ans)

def main():
    totals = 0
    for n in range(1, 161):
        f = factors_exact(n)
        observed = lie_classes(f, n)
        x = n
        while x % 2 == 0:
            x //= 2
        target = 2 if x in (1, 3) else 0
        assert len(observed) == target, (n, observed, target)
        # Every length-n factor fits in two length-(power-of-2) substituted blocks,
        # and 00,01,10 all appear as adjacent source letters. The set is complete.
        totals += len(f)
    assert lie_classes(factors_exact(1),1) == ['0','1']
    assert lie_classes(factors_exact(3),3) == ['000','001']
    assert lie_classes(factors_exact(4),4) == ['0001','0101']
    print('VERIFY_OK lengths=1..160 exact-factor-cover=adjacent-substitution-blocks',
          'factor_instances=',totals, 'lie_formula=PASS')

if __name__ == '__main__':
    main()
