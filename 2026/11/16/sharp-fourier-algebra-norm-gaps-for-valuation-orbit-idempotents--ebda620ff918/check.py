"""Recompute exact Fourier-algebra norms of finite valuation-shell indicators.

All finite enumeration is supplemental evidence; the proof for arbitrary depth
is the subgroup-character decomposition in RESULT.md.
"""
from fractions import Fraction
from itertools import product
from math import pi
from cmath import exp


def valuation_shell_norm(q, k, bits):
    """Exact norm from the annihilator expansion; bits index shells 0..k-1, centre k."""
    assert q >= 2 and k >= 1 and len(bits) == k + 1
    jump = [bits[j] - bits[j - 1] for j in range(1, k + 1)]
    density = Fraction(bits[0]) + sum((Fraction(jump[j-1], q**j) for j in range(1,k+1)), Fraction(0))
    return density + (q-1) * sum((q**(s-1) * abs(sum((Fraction(jump[j-1],q**j) for j in range(s,k+1)),Fraction(0))) for s in range(1,k+1)), Fraction(0))


def expected(q,k,bits):
    if not any(bits): return Fraction(0)
    first=bits.index(1)
    if all(b==1 for b in bits[first:]): return Fraction(1) # ball
    if all(b==0 for b in bits[first+1:]): return Fraction(2*(q-1),q) # shell
    if q==2 and first<=k-2:
        if tuple(bits[first:]) in ((1,1)+tuple(0 for _ in range(k-first-1)),
                                  (1,0)+tuple(1 for _ in range(k-first-1))):
            return Fraction(3,2)
    return None


def full_dft_norm(p,d,k,bits):
    mod=p**k
    elems=list(product(range(mod),repeat=d))
    def val(n):
        if n==0:return k
        j=0
        while n%p==0:
            j+=1;n//=p
        return j
    S=[int(bool(bits[min(map(val,x))])) for x in elems]
    size=len(elems)
    total=0.
    for f in elems:
        z=sum(S[i]*exp(-2j*pi*sum(a*b for a,b in zip(f,x))/mod) for i,x in enumerate(elems))/size
        total+=abs(z)
    return total


def run():
    cases=0; classes={}
    for q in (2,3,4,5,7,9,16):
        for k in range(1,8):
            for bits in product((0,1),repeat=k+1):
                a=valuation_shell_norm(q,k,bits)
                e=expected(q,k,bits)
                if q==2:
                    assert a in (Fraction(0),Fraction(1)) or a>=Fraction(3,2), (q,k,bits,a)
                    if a==Fraction(3,2): assert e==a, (q,k,bits,a,e)
                else:
                    assert a in (Fraction(0),Fraction(1)) or a>=Fraction(2*(q-1),q), (q,k,bits,a)
                    if a==Fraction(2*(q-1),q): assert e==a, (q,k,bits,a,e)
                if e is not None: assert a==e, (q,k,bits,a,e)
                cases+=1
    # Complex finite-group Fourier transform checks separate from character-count formula.
    dft=0
    for p,d,k in ((2,1,1),(2,1,2),(2,1,3),(2,1,4),(3,1,1),(3,1,2),(3,1,3),(2,2,1),(2,2,2),(3,2,1)):
        for bits in product((0,1),repeat=k+1):
            exact=float(valuation_shell_norm(p**d,k,bits))
            actual=full_dft_norm(p,d,k,bits)
            assert abs(actual-exact)<1.e-9, (p,d,k,bits,actual,exact)
            dft+=1
    print(f'PASS: {cases} exact rational pattern checks; {dft} direct complex DFT checks.')

if __name__=='__main__': run()
