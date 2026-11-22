#!/usr/bin/env python3
"""Independent small-case checks for finite monomial-algebra principal units.

Only prime fields are used in these checks. The theorem covers all finite fields.
"""
from itertools import product
from collections import Counter
from math import prod


def downset_box(lengths):
    return tuple(product(*(range(a) for a in lengths)))


def frobenius_counts(monomials, p):
    present = set(monomials)
    positive = [a for a in monomials if any(a)]
    out = []
    s = 0
    while True:
        r = sum(tuple((p**s) * z for z in a) in present for a in positive)
        out.append(r)
        if r == 0:
            break
        s += 1
    return out


def cyclic_invariants(lengths, p, f=1):
    m = downset_box(lengths)
    ranks = frobenius_counts(m, p)
    ranks += [0]
    return {p**s:f * (ranks[s - 1] - 2 * ranks[s] + ranks[s + 1])
            for s in range(1, len(ranks)-1)}


def multiply(u, v, monomials, p):
    ix = {a:i for i,a in enumerate(monomials)}
    out = [0]*len(monomials)
    for i, a in enumerate(monomials):
        if not u[i]:
            continue
        for j, b in enumerate(monomials):
            c = tuple(x+y for x,y in zip(a,b))
            if v[j] and c in ix:
                k = ix[c]
                out[k] = (out[k] + u[i]*v[j]) % p
    return tuple(out)


def power(v, exponent, monomials, p):
    identity = tuple(int(not any(a)) for a in monomials)
    ans, factor = identity, v
    while exponent:
        if exponent & 1:
            ans = multiply(ans, factor, monomials, p)
        factor = multiply(factor, factor, monomials, p)
        exponent //= 2
    return ans


def test_box(lengths, p, full=False):
    monomials = downset_box(lengths)
    n = len(monomials)
    counts = frobenius_counts(monomials, p)
    expected = cyclic_invariants(lengths, p)
    assert all(c >= 0 for c in expected.values())
    assert sum(next(s for s in range(1,n+1) if p**s == k) * v
               for k,v in expected.items()) == n - 1
    identity = tuple(int(not any(a)) for a in monomials)
    samples = product(range(p), repeat=n-1)
    if not full:
        from random import Random
        rng=Random(4096 + n * 33 + p)
        samples = ([rng.randrange(p) for _ in range(n-1)] for _ in range(80))
    observed = Counter()
    checked=0
    for coeff in samples:
        unit = (1,) + tuple(coeff)
        if unit == identity:
            observed[1] += 1
        else:
            highest = 0
            for s in range(1,len(counts)):
                if power(unit,p**s,monomials,p) == identity:
                    highest = s
                    break
            assert highest
            observed[p**highest] += 1
        checked += 1
    if full:
        assert checked == p**(n-1)
        # Number of units with order dividing p**s is q**(r0-rs).
        for s in range(1, len(counts)):
            assert sum(v for k,v in observed.items() if k<=p**s) == p**(counts[0]-counts[s])
    print('PASS', 'box', lengths, 'field', p, 'units checked',checked,
          'ranks',counts,'cyclic factors',expected,
          'unit orders',sorted(observed.items()))


def full_frobenius_histogram(lengths, p):
    """Enumerate all coefficient vectors; no group-theory classification is used."""
    monomials = downset_box(lengths)
    pos = monomials[1:]
    surviving = [tuple(p*z for z in a) in set(monomials) for a in pos]
    hist = Counter()
    for coeff in product(range(p), repeat=len(pos)):
        if not any(coeff):
            order = 1
        elif any(c and survive for c, survive in zip(coeff,surviving)):
            order = p*p
        else:
            order = p
        hist[order] += 1
    assert sum(hist.values()) == p**len(pos)
    return hist


def main():
    for L,p in [((2,4),2), ((2,3),2), ((2,3),3), ((2,6),3), ((3,4),3)]:
        test_box(L,p,full=(prod(L)<=8))
    for L in ((2,6), (3,4)):
        hist = full_frobenius_histogram(L, 3)
        assert hist == {1:1, 3:59048, 9:118098}
        print('PASS', 'complete principal-unit order histogram', L, hist)
    # Compare the odd-prime collision family and further box types.
    for p in [3,5,7,11]:
        a,b=(p-1,2*p),(p,2*p-2)
        assert cyclic_invariants(a,p,2)==cyclic_invariants(b,p,2)
        assert prod(a)==prod(b)
        assert sum(a)-1==3*p-2
        assert sum(b)-1==3*p-3
        assert frobenius_counts(downset_box(a),p)==[2*p*(p-1)-1,1,0]
        assert frobenius_counts(downset_box(b),p)==[2*p*(p-1)-1,1,0]
        print('PASS', 'collision',p,'dimensions',prod(a),'lengths',sum(a)-1,sum(b)-1,
              'cyclic factors (field degree 2)',cyclic_invariants(a,p,2))
    # Test one non-rectangular monomial downset (all monomials of degree <= 3).
    mon=tuple(a for a in product(range(4),repeat=2) if sum(a)<=3)
    counts=frobenius_counts(mon,2)
    assert counts==[9,2,0]
    print('PASS', 'nonrectangular downset', counts, 'principal group',
          {'C2':9-2*2,'C4':2})
    print('PRINCIPAL_UNIT_COLLISION_VERIFIED')

if __name__ == '__main__':
    main()
