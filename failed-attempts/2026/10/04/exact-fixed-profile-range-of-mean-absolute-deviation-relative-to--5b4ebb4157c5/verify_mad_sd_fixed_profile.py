#!/usr/bin/env python3
from fractions import Fraction
import random

def normalize(raw):
    s=sum(raw)
    return [Fraction(x,s) for x in raw]

def stats(ps,xs):
    mu=sum(p*x for p,x in zip(ps,xs))
    z=[x-mu for x in xs]
    D=sum(p*abs(v) for p,v in zip(ps,z))
    V=sum(p*v*v for p,v in zip(ps,z))
    pos=sum(p*v for p,v in zip(ps,z) if v>0)
    neg=sum(p*(-v) for p,v in zip(ps,z) if v<0)
    return mu,D,V,pos,neg

def lower2(ps):
    return Fraction(4)*ps[0]*ps[-1]/(ps[0]+ps[-1])

def upper2(ps):
    P=Fraction(0)
    vals=[]
    for p in ps[:-1]:
        P+=p
        vals.append(Fraction(4)*P*(1-P))
    return max(vals)

def run():
    rng=random.Random(20261002)
    balance_checks=0
    lower_checks=0
    upper_checks=0
    strict_lower_checks=0
    strict_upper_checks=0
    binary_checks=0
    triple_equality_checks=0
    lower_approach_checks=0
    upper_approach_checks=0
    equal_mass_checks=0

    for _ in range(24000):
        m=rng.randrange(2,9)
        ps=normalize([rng.randrange(1,31) for __ in range(m)])
        xs=[Fraction(0)]
        for __ in range(1,m):
            xs.append(xs[-1]+Fraction(rng.randrange(1,31),rng.randrange(1,11)))

        mu,D,V,pos,neg=stats(ps,xs)
        assert pos==neg==D/2
        balance_checks+=2

        L2=lower2(ps)
        U2=upper2(ps)
        assert D*D >= L2*V
        assert D*D <= U2*V
        lower_checks+=1
        upper_checks+=1

        if m==2:
            assert D*D==L2*V==U2*V
            binary_checks+=1
        else:
            assert D*D < U2*V
            strict_upper_checks+=1
            if m>=4:
                assert D*D > L2*V
                strict_lower_checks+=1

    # Exact three-point lower equality: normalized support 0, c/(a+c), 1.
    for _ in range(8000):
        ps=normalize([rng.randrange(1,40) for __ in range(3)])
        a,b,c=ps
        t=c/(a+c)
        xs=[Fraction(0),t,Fraction(1)]
        mu,D,V,pos,neg=stats(ps,xs)
        assert mu==t
        assert D*D==lower2(ps)*V
        assert D*D<upper2(ps)*V
        triple_equality_checks+=3

    # Rational lower approach for m>=4.
    for _ in range(4000):
        m=rng.randrange(4,9)
        ps=normalize([rng.randrange(1,25) for __ in range(m)])
        eps=Fraction(1,10**7)
        ts=[Fraction(2*i-m+1, m) for i in range(1,m-1)]
        interior=[eps*t for t in ts]
        xm=Fraction(1)
        x1=-(ps[-1]*xm + sum(p*x for p,x in zip(ps[1:-1],interior)))/ps[0]
        xs=[x1]+interior+[xm]
        assert all(xs[i]<xs[i+1] for i in range(m-1))
        _,D,V,_,_=stats(ps,xs)
        L2=lower2(ps)
        assert D*D>L2*V
        # Relative squared gap is tiny.
        assert (D*D-L2*V)/(L2*V) < Fraction(1,10000)
        lower_approach_checks+=2

    # Rational upper approach at a maximizing cut.
    for _ in range(4000):
        m=rng.randrange(3,9)
        ps=normalize([rng.randrange(1,25) for __ in range(m)])
        P=Fraction(0)
        vals=[]
        for j,p in enumerate(ps[:-1],start=1):
            P+=p
            vals.append((P*(1-P),j))
        _,jstar=max(vals)
        eps=Fraction(1,10**8)
        left=[eps*i for i in range(jstar)]
        right=[Fraction(1)+eps*i for i in range(m-jstar)]
        xs=left+right
        assert all(xs[i]<xs[i+1] for i in range(m-1))
        _,D,V,_,_=stats(ps,xs)
        U2=upper2(ps)
        assert D*D<U2*V
        assert (U2*V-D*D)/(U2*V) < Fraction(1,10000)
        upper_approach_checks+=2

    for m in range(2,101):
        ps=[Fraction(1,m)]*m
        assert lower2(ps)==Fraction(2,m)
        if m%2==0:
            assert upper2(ps)==1
        else:
            assert upper2(ps)==Fraction(m*m-1,m*m)
        equal_mass_checks+=2

    print(
        "VERIFY_OK "
        f"balance_checks={balance_checks} "
        f"lower_checks={lower_checks} "
        f"upper_checks={upper_checks} "
        f"strict_lower_checks={strict_lower_checks} "
        f"strict_upper_checks={strict_upper_checks} "
        f"binary_checks={binary_checks} "
        f"triple_equality_checks={triple_equality_checks} "
        f"lower_approach_checks={lower_approach_checks} "
        f"upper_approach_checks={upper_approach_checks} "
        f"equal_mass_checks={equal_mass_checks}"
    )

if __name__=="__main__":
    run()
