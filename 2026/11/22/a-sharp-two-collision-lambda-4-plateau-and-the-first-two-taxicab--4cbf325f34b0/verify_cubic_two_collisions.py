#!/usr/bin/env python3
"""Finite exact arithmetic checks for the two-collision Fourier theorem.

All pair sums and all fourth-moment identities are checked with integer
or rational arithmetic. The analytic supremum is proved in RESULT.md.
"""
from collections import defaultdict
from fractions import Fraction
from random import Random


def collisions(frequencies):
    pairs = defaultdict(list)
    for j, x in enumerate(frequencies):
        for k in range(j, len(frequencies)):
            pairs[x + frequencies[k]].append((j, k))
    return {s: v for s, v in pairs.items() if len(v) > 1}


def direct_moment(frequencies, coeffs):
    convolution = defaultdict(complex)
    for j, x in enumerate(frequencies):
        for k, y in enumerate(frequencies):
            convolution[x+y] += coeffs[j] * coeffs[k]
    return sum(int(v.real)**2+int(v.imag)**2 for v in convolution.values())


def formula_moment(coeffs, resonances):
    sq = [int(a.real)**2+int(a.imag)**2 for a in coeffs]
    s = sum(sq)
    base = 2*s*s-sum(t*t for t in sq)
    for i,j,k,l in resonances:
        base += 8*int((coeffs[i]*coeffs[j]*coeffs[k].conjugate()*coeffs[l].conjugate()).real)
    return base


def check():
    expected = {
        1729: [(0,11),(8,9)],
        4104: [(1,15),(8,14)],
    }
    pairs_checked=0
    for n in range(1,24):
        c = collisions([k**3 for k in range(1,n+1)])
        gold={key:[pair for pair in val if max(pair)<n] for key,val in expected.items()}
        gold={key:val for key,val in gold.items() if len(val)==2}
        assert c==gold,(n,c,gold)
        pairs_checked += n*(n+1)//2
    # N=24 is the next genuine collision, so the earlier interval is maximal.
    c24=collisions([k**3 for k in range(1,25)])
    assert len(c24)==3 and 13832 in c24
    assert c24[13832]==[(1,23),(17,19)]
    # The 7-element model contains exactly two off-diagonal collisions.
    idx=[1,2,9,10,12,15,16]
    frequencies=[k**3 for k in idx]
    c=collisions(frequencies)
    assert list(sorted(c))==[1729,4104]
    assert c[1729]==[(0,4),(2,3)]
    assert c[4104]==[(1,6),(2,5)]
    resonances=[(0,4,2,3),(1,6,2,5)]
    rng=Random(20261117)
    direct_checks=0
    for _ in range(700):
        coeffs=[complex(rng.randint(-3,3),rng.randint(-3,3)) for i in range(7)]
        exact=direct_moment(frequencies,coeffs)
        analytic=formula_moment(coeffs,resonances)
        assert exact==analytic,(exact,analytic)
        direct_checks+=1
    # Exact rational equality witnesses: 4 coefficients of magnitude 1/2.
    for support in [[0,2,3,4],[1,2,5,6]]:
        a=[Fraction(0,1) for i in idx]
        for j in support:a[j]=Fraction(1,2)
        s=sum(t*t for t in a)
        quartic={}
        for j,p in enumerate(frequencies):
            for k,q in enumerate(frequencies):
                quartic[p+q]=quartic.get(p+q,Fraction(0))+a[j]*a[k]
        val=sum(t*t for t in quartic.values())
        assert s==1 and val==Fraction(9,4)
    # Exact polynomial SOS identity for the balanced branch.
    import sympy as sp
    y=sp.symbols('y',real=True)
    lhs=15*y**4+6*y**2+5-32*y/sp.sqrt(6)
    rhs=15*(y**2-sp.Rational(1,4))**2+sp.Rational(27,2)*(y-32/(27*sp.sqrt(6)))**2+sp.Rational(1169,1296)
    assert sp.simplify(lhs-rhs)==0
    print('VERIFY_OK finite_prefixes=23 unordered_pairs='+str(pairs_checked)+' exact_moment_checks='+str(direct_checks)+' equality_witnesses=2 sos_identity=1')


if __name__=='__main__':check()
