"""Exact verification of the standard-example preorder support-enumerator claim.

Python >=3.9, standard library only. Run: python standard_example_verify.py
"""
from fractions import Fraction
from itertools import combinations
from math import comb, gcd, lcm


def gamma_coeffs(m):
    return [comb(m,j)**2 - (m if j == 1 else 0) for j in range(m+1)]


def possible_matching(src, tgt):
    # Comparability in the standard-example poset: a_i < b_j iff i != j.
    def match(k, used):
        if k == len(src):
            return True
        return any((j != src[k]) and not (used & (1 << j))
                   and match(k + 1, used | (1 << j)) for j in tgt)
    return match(0, 0)


def gamma_by_hall(m):
    out = []
    for j in range(m+1):
        out.append(sum(possible_matching(b, t)
                       for b in combinations(range(m), j)
                       for t in combinations(range(m), j)))
    return out


def compositions_at_most(length, bound):
    state = [0]*length
    def visit(i, rem):
        if i == length:
            yield tuple(state)
            return
        for a in range(rem+1):
            state[i] = a
            yield from visit(i+1, rem-a)
    yield from visit(0, bound)


def ideals(m):
    # Vertices 0..m-1 are the lower elements a_i; m..2m-1 are b_i.
    pred = [1 << i for i in range(2*m)]
    for j in range(m):
        for i in range(m):
            if i != j:
                pred[m+j] |= 1 << i
    return [tuple(i for i in range(2*m) if bits & (1 << i))
            for bits in range(1 << (2*m))
            if all((bits & pred[i]) == pred[i]
                   for i in range(2*m) if bits & (1 << i))]


def h_by_ideals(m):
    n = 2*m
    ideal_collection = ideals(m)
    out = [0]*(n+1)
    for x in compositions_at_most(n,n):
        if all(sum(x[i] for i in I) <= len(I) for I in ideal_collection):
            out[sum(v != 0 for v in x)] += 1
    return out


def h_from_gamma(m):
    n=2*m
    out=[0]*(n+1)
    for j,c in enumerate(gamma_coeffs(m)):
        for t in range(n-2*j+1):
            out[t+j] += c*comb(n-2*j,t)
    return out


def strip(poly):
    while poly and poly[-1] == 0:
        poly.pop()
    return poly


def remainder(a,b):
    a=list(map(Fraction,a))
    b=list(map(Fraction,b))
    while len(a)>=len(b):
        scale=a[-1]/b[-1]
        shift=len(a)-len(b)
        for j,v in enumerate(b):
            a[shift+j] -= scale*v
        strip(a)
    return a


def sturm_chain(coefficients):
    a = list(map(Fraction,coefficients))
    b = [Fraction(j * coefficients[j]) for j in range(1,len(coefficients))]
    chain=[a,b]
    while chain[-1]:
        p=[-v for v in remainder(chain[-2],chain[-1])]
        if not p:
            break
        denom=lcm(*(v.denominator for v in p))
        z=[int(v*denom) for v in p]
        divisor=gcd(*z)
        chain.append([Fraction(v//divisor) for v in z])
    return chain


def variations(values):
    signs=[v>0 for v in values if v]
    return sum(a != b for a,b in zip(signs,signs[1:]))


def negative_distinct_roots(coefficients):
    chain=sturm_chain(coefficients)
    vleft=variations([p[-1] * (-1)**(len(p)-1) for p in chain])
    vright=variations([p[0] for p in chain])
    return vleft,vright,vleft-vright


def main():
    for m in range(1,8):
        assert gamma_by_hall(m) == gamma_coeffs(m), ('Hall',m)
    print('HALL_MATCHING_ENUMERATION m=1..7 PASS')
    for m in range(1,5):
        assert h_by_ideals(m) == h_from_gamma(m), ('Ideal',m)
    print('DIRECT_IDEAL_LATTICE_ENUMERATION m=1..4 PASS')
    counts=[]
    for m in range(2,13):
        a,b,num=negative_distinct_roots(gamma_coeffs(m))
        counts.append((m,a,b,num))
        assert num==(1 if m==2 else (m if m<12 else 10)), ('Sturm',m)
    # For m=2, the factor is (1+q)^2 and its sole distinct root is double.
    assert gamma_coeffs(2)==[1,2,1]
    # For m>=3 up through 11, 'm' distinct negative roots implies all are real.
    # For m=12, only ten distinct negative roots; Descartes' sign rule
    # excludes nonnegative real roots. The discriminant is known nonzero
    # by a rational gcd of the polynomial and its derivative.
    assert len(sturm_chain(gamma_coeffs(12)))==13
    print('STURM_VARIATIONS',counts)
    print('REAL_ROOT_THRESHOLD m=12 PASS')
    print('VERIFY_OK')

if __name__=='__main__':
    main()
