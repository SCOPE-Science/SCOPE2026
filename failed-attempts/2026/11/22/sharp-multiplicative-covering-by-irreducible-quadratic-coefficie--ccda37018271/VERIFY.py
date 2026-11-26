#!/usr/bin/env python3
"""Reproduce finite-field tests for a twofold coefficient-product theorem.

Requires only Python 3 standard library; no external dependencies.
"""
from itertools import product


def prime(p):
    assert p % 2 and all(p % d for d in range(2, int(p**0.5) + 1))
    return p, lambda a, b: a*b % p, lambda a, b: (a-b) % p


def quadratic_extension(p):
    # Encode a+b*u as a+p*b, with u^2=d nonsquare.
    d = next(z for z in range(2, p) if pow(z, (p-1)//2, p) == p-1)
    q = p*p
    def mul(x, y):
        a,b=x%p,x//p; c,e=y%p,y//p
        return (a*c+d*b*e)%p + p*((a*e+b*c)%p)
    def sub(x,y):
        return ((x%p-y%p)%p) + p*((x//p-y//p)%p)
    return q, mul, sub


def verify_field(field, all_constants=True):
    q, mul, sub = field
    # Construct the nonzero square class and its complement directly.
    squares = {mul(a,a) for a in range(1,q)}
    nonsquares = [z for z in range(1,q) if z not in squares]
    constants = nonsquares if all_constants else nonsquares[:1]
    for c in constants:
        # Prime-subfield element 4 is represented by 4 % characteristic.
        # Correct the scalar by repeated addition, using subtraction only.
        scalar4 = 0
        for _ in range(4): scalar4 = sub(scalar4, sub(0,1))
        four_c = mul(scalar4, c)
        A = {b for b in range(1,q) if sub(mul(b,b),four_c) in nonsquares}
        pair = {mul(a,b) for a in A for b in A}
        if q % 4 == 3:
            assert pair == set(range(1,q)), (q,c,'pair',pair)
        else:
            excluded = {four_c, sub(0,four_c)}
            assert pair == set(range(1,q)) - excluded, (q,c,'pair',pair,excluded)
            triple = {mul(t,a) for t in pair for a in A}
            assert (triple == set(range(1,q)) if q>5 else len(triple)==2), (q,c,'triple',triple)
    return len(constants)


def main():
    counts = []
    for p in [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197]:
        counts.append((p, verify_field(prime(p), all_constants=(p<=73))))
    for p in [3,5,7,11,13]:
        counts.append((p*p,verify_field(quadratic_extension(p), all_constants=(p<=7))))
    print('VERIFY_OK', 'field_cases=',len(counts),'nonsquare_constants=',sum(n for _,n in counts))
    print('examples', [v for v in counts if v[0] in (3,5,9,13,25,49)])

if __name__=='__main__': main()
