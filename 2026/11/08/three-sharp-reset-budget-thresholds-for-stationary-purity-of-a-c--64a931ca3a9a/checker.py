"""Exact-rational diagnostics for quarter-turn renewal qubit purity bounds.

Run with: python3 checker.py
Only Python standard library is required. Finite diagnostics complement, not replace,
the universal inequalities proved in RESULT.md.
"""
from fractions import Fraction as F
from itertools import combinations


def envelope(mu):
    mu = F(mu)
    assert mu >= 1
    lo = (1 + (2 - mu)**2) if mu <= F(3,2) else ((4-mu)**2/5 if mu <= 4 else F(0))
    hi = (2 + 2*(mu - 1)**2) if mu <= 2 else F(4)
    return F(lo), F(hi)


def moments(law):
    assert all(n >= 1 and p >= 0 for n,p in law.items())
    assert sum(law.values()) == 1
    mu = sum((n*p for n,p in law.items()), F(0))
    # w=1-E[i**L], with signed imaginary component.
    cs = (1,0,-1,0)
    sn = (0,1,0,-1)
    wr = 1 - sum((p*cs[n%4] for n,p in law.items()), F(0))
    wi = -sum((p*sn[n%4] for n,p in law.items()), F(0))
    return mu, wr**2 + wi**2, (wr,wi)


def age_coherence(law):
    mu = sum((n*p for n,p in law.items()), F(0))
    max_n=max(law)
    cs=(1,0,-1,0)
    sn=(0,1,0,-1)
    real=sum((sum((p for n,p in law.items() if n>a),F(0))*cs[a%4] for a in range(max_n)),F(0))/mu
    imag=sum((sum((p for n,p in law.items() if n>a),F(0))*sn[a%4] for a in range(max_n)),F(0))/mu
    return real**2+imag**2


def opt_min(mu):
    mu = F(mu)
    if mu <= F(3,2):
        return {1:(3-mu)/2, 3:(mu-1)/2}
    if mu <= 4:
        return {1:3*(4-mu)/10,3:(4-mu)/10,4:(2*mu-3)/5}
    # support entirely on the residue 0 mod 4
    k = (mu-4)//4
    n = 4+4*k
    return {n:F(n+4-mu,4), n+4:F(mu-n,4)}


def opt_max(mu):
    mu = F(mu)
    if mu <= 2:
        return {1:2-mu, 2:mu-1}
    k = (mu-2)//4
    n = 2+4*k
    return {n:F(n+4-mu,4),n+4:F(mu-n,4)}


def compositions(n,k):
    # weak compositions of n into k parts by selecting separator locations
    for cuts in combinations(range(n+k-1),k-1):
        edges=(-1,)+cuts+(n+k-1,)
        yield [edges[j+1]-edges[j]-1 for j in range(k)]


def main():
    asserts=0
    for num in range(1,401):
        mu = 1+F(num-1, 100)
        for make,ix in [(opt_min,0),(opt_max,1)]:
            law={n:p for n,p in make(mu).items() if p}
            mean,val,_=moments(law)
            assert mean==mu
            assert val==envelope(mu)[ix]
            asserts+=2
    # Exact polytope checks: all weak compositions of 7 into 12 pieces.
    for weights in compositions(7,12):
        law={n:F(v,7) for n,v in enumerate(weights,1) if v}
        mu,val,_=moments(law)
        lo,hi=envelope(mu)
        assert lo <= val <= hi, (law,mu,val,lo,hi)
        assert age_coherence(law) == val/(2*mu**2)
        asserts+=2
    # Universal dual inequalities checked over a finite diagnostic range;
    # proof for n>4 uses nonnegativity and 4-n<0, not this loop.
    for n in range(1,1001):
        re=1-(1,0,-1,0)[n%4]
        im=-(0,1,0,-1)[n%4]
        assert 2*re-im>=4-n
        for u in (F(1,2),F(3,4),F(1)):
            assert re-u*im>=1+2*u-u*n
        asserts+=4
    # Explicit geometric-clock benchmark at mu=2.
    z2=F(1,4)/F(5,4)  # |(1/2)/(1-i/2)|^2
    purity=F(1,2)*(1+z2)
    assert purity==F(3,5)
    lo,hi=envelope(F(2))
    assert F(1,2)+lo/F(16) == F(11,20)
    assert F(1,2)+hi/F(16) == F(3,4)
    asserts+=3
    print('PASS: exact rational optimization and renewal diagnostics; checks:',asserts)

if __name__=='__main__':
    main()
