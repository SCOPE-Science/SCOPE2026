#!/usr/bin/env python3
"""Exact small-field tests for threefold sums of the punctured inverse graph.

Finite fields use binary polynomial bases; counting is by integer arithmetic.
These tests supplement, but do not replace, the general elliptic-curve proof.
"""
from collections import Counter

# Binary irreducible polynomials (coefficients low degree first).
MODULI = {1:(1,1), 2:(1,1,1), 3:(1,1,0,1),
          4:(1,1,0,0,1), 5:(1,0,1,0,0,1)}


def field(m):
    q = 1 << m
    polynomial = sum(bit << j for j, bit in enumerate(MODULI[m]))
    def mul(a,b):
        z=0
        while b:
            if b&1: z^=a
            a<<=1
            if a&q: a^=polynomial
            b>>=1
        return z
    def pow_f(a,k):
        z=1
        while k:
            if k&1:z=mul(z,a)
            a=mul(a,a)
            k>>=1
        return z
    inverses={a:pow_f(a,q-2) for a in range(1,q)}
    assert all(mul(a,b)==1 for a,b in inverses.items())
    def tr(x):
        accum=0
        for _ in range(m):
            accum^=x
            x=mul(x,x)
        assert accum in (0,1)
        return accum
    return q,mul,inverses,tr


def threefold(q,inverses):
    step=[(x,inverses[x]) for x in range(1,q)]
    two=Counter((x^y,inverses[x]^inverses[y]) for x in inverses for y in inverses)
    three=Counter()
    for (a,b),count in two.items():
        for x,y in step:
            three[(a^x,b^y)]+=count
    assert sum(three.values())==(q-1)**3
    return three


def check(m):
    q,mul,inv,tr=field(m)
    counts=threefold(q,inv)
    expected_origin=2*(q-1) if m%2==0 else 0
    expected_axis=q-4 if m%2==0 else q-2
    assert counts.get((0,0),0)==expected_origin
    for x in range(1,q):
        assert counts.get((x,0),0)==expected_axis
        assert counts.get((0,x),0)==expected_axis
    for s in range(1,q):
        for t in range(1,q):
            c=mul(s,t)
            count=counts.get((s,t),0)
            if c==1:
                assert count==3*q-5
                continue
            # Every finite unramified u other than u=1 gives either 0 or 2 points.
            elliptic_affine=0
            for u in range(q):
                d=mul(u, (mul(c,u)^c^1))
                if d==0 or u==1: continue
                value=mul(u^1,inv[d])
                elliptic_affine+=2 if tr(value)==0 else 0
            assert count==elliptic_affine, (q,s,t,count,elliptic_affine)
            rational_points=elliptic_affine+6
            assert (rational_points-(q+1))**2<=4*q
    support={point for point,count in counts.items() if count>0}
    if m==1:
        assert support=={(1,1)}
    elif m==2:
        assert support=={(x,inv[x]) for x in range(1,q)}|{(0,0)}
    elif m==3:
        assert len(support)==42
        one={(x,inv[x]) for x in range(1,q)}
        two={(x^y,inv[x]^inv[y]) for x in inv for y in inv}
        assert len(support | one | two | {(0,0)})==q*q
        for s in range(1,q):
            for t in range(1,q):
                c=mul(s,t)
                assert ((s,t) in support)==(c==1 or tr(c)==0)
    elif m%2==0:
        assert len(support)==q*q
    else:
        assert len(support)==q*q-1
        assert (0,0) not in support
    print(f'q={q}: support={len(support)}/{q*q}, r3(0,0)={counts.get((0,0),0)}, r3(1,1)={counts.get((1,1),0)}')


if __name__=='__main__':
    for degree in sorted(MODULI):check(degree)
    print('BINARY_HYPERBOLA_THREE_STEP_EXACT_CHECKS_PASS')
