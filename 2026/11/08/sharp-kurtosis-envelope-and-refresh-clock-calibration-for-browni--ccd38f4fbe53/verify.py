"""Exact-arithmetic checks of moment identities for rate-refreshed Brownian resetting.
Run: python verify.py
The universal inequalities in the accompanying proof are analytic; finite tests
provide independent algebraic and generator-consistency diagnostics.
"""
from fractions import Fraction as Q
from itertools import product

def check(rates, probs, mu, D):
    assert len(rates)==len(probs) and sum(probs)==1
    assert mu>0 and D>0 and any(z>0 for z in rates)
    B1=sum((p/(mu+z) for p,z in zip(probs,rates)),Q(0))
    B2=sum((p/(mu+z)**2 for p,z in zip(probs,rates)),Q(0))
    B3=sum((p/(mu+z)**3 for p,z in zip(probs,rates)),Q(0))
    B4=sum((p/(mu+z)**4 for p,z in zip(probs,rates)),Q(0))
    T=1-mu*B1
    assert T>0
    m2=2*D*B1/T
    m4=24*D*D*B2/T**2
    # Independently solve the stationary generator's conditional moment equations.
    cond2=[(2*D*p+mu*p*m2)/(mu+z) for p,z in zip(probs,rates)]
    cond4=[(12*D*v+mu*p*m4)/(mu+z) for p,z,v in zip(probs,rates,cond2)]
    assert sum(cond2)==m2 and sum(cond4)==m4
    for p,z,v,w in zip(probs,rates,cond2,cond4):
        assert 2*D*p-(mu+z)*v+mu*p*m2==0
        assert 12*D*v-(mu+z)*w+mu*p*m4==0
    excess=m4/m2**2-3
    assert excess == 6*B2/B1**2-3
    assert excess>=3
    lo,hi=min(rates),max(rates)
    bound=3+Q(3,2)*(hi-lo)**2/((mu+lo)*(mu+hi))
    assert excess<=bound
    # The exact derivative is a negative square-moment defect.
    deriv=12*(B2*B2-B1*B3)/B1**3
    pair=sum((p*q*u*v*(u-v)**2 for p,u in zip(probs,[1/(mu+z) for z in rates])
              for q,v in zip(probs,[1/(mu+z) for z in rates])),Q(0))
    assert B1*B3-B2*B2==pair/2
    assert deriv == -6*pair/B1**3
    second=36*(B1*B1*B4-2*B1*B2*B3+B2**3)/B1**4
    weighted_positive=sum((p*u*u*(u-B2/B1)**2 for p,u in zip(probs,[1/(mu+z) for z in rates])),Q(0))
    assert second==36*weighted_positive/B1**2
    if len(set(rates))>1: assert deriv<0 and second>0 and excess>3
    else: assert deriv==0 and second==0 and excess==3
    return excess

count=0
for rates in [(Q(1),Q(3)), (Q(0),Q(7)), (Q(2),Q(2)),
              (Q(1,3),Q(5),Q(17)), (Q(0),Q(3,2),Q(11))]:
    for p in [Q(1,7),Q(2,5),Q(5,7)]:
        ps=(p,1-p) if len(rates)==2 else (p,(1-p)/3,2*(1-p)/3)
        for mu in [Q(1,20),Q(1,2),Q(5),Q(100)]:
            for D in [Q(1,7),Q(1),Q(11,3)]:
                check(rates,ps,mu,D)
                count+=1
        if len(rates)==2 and rates[0]!=rates[1]:
            a,b=rates
            c=p*b+(1-p)*a
            for mu in [Q(1,20),Q(1,2),Q(5),Q(100)]:
                kapp=check(rates,(p,1-p),mu,Q(1))
                assert kapp==3+6*p*(1-p)*(b-a)**2/(mu+c)**2
                count+=1
# Verify the exact support-envelope equality cases for endpoint rates.
for a,b in [(Q(0),Q(3)), (Q(1),Q(5)), (Q(2,7),Q(11,3))]:
    for mu in [Q(1,9),Q(1),Q(9)]:
        p=(mu+a)/(2*mu+a+b)
        got=check((a,b),(p,1-p),mu,Q(1))
        target=3+Q(3,2)*(b-a)**2/((mu+a)*(mu+b))
        assert got==target
        count+=1
# Verify strict monotonicity between different refresh speeds in exact arithmetic.
for rates,ps in [((Q(1),Q(4)),(Q(2,5),Q(3,5))),
                 ((Q(0),Q(7)),(Q(1,3),Q(2,3))),
                 ((Q(1,2),Q(3),Q(9)),(Q(1,3),Q(1,4),Q(5,12)))]:
    ks=[check(rates,ps,u,Q(1)) for u in [Q(1,100),Q(1,5),Q(1),Q(10),Q(1000)]]
    assert all(u>v>3 for u,v in zip(ks,ks[1:]))
    count+=len(ks)
print(f"PASS: {count} exact-arithmetic parameter evaluations, plus generator and derivative identities")
