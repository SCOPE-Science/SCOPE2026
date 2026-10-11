#!/usr/bin/env python3
from fractions import Fraction
import random

def vm(m):
    return Fraction(m*(m+1),3)

def qm(m):
    return Fraction(m*(m+1)*(3*m*m+3*m-1),15)

def chord(m, v):
    a,b = vm(m), vm(m+1)
    qa,qb = qm(m), qm(m+1)
    return (b-v)*qa/(b-a) + (v-a)*qb/(b-a)

def phase_formula(m, theta):
    a,b = vm(m),vm(m+1)
    v = a + theta*(b-a)
    kappa = chord(m,v)/(v*v)
    scaled = v*(kappa-Fraction(9,5))
    rhs = -Fraction(1,5) + Fraction(9,5)*theta*(1-theta)*(b-a)*(b-a)/v
    return v, scaled, rhs

def find_cell(v):
    m=0
    while vm(m+1) < v:
        m += 1
    return m

def run():
    moment_checks=0
    chord_checks=0
    equality_checks=0
    random_mix_checks=0
    phase_checks=0

    for m in range(0,501):
        v=vm(m); q=qm(m)
        assert q == (9*v*v-v)/5
        den = 2*m+1
        s2 = sum(j*j for j in range(-m,m+1))
        s4 = sum(j**4 for j in range(-m,m+1))
        assert Fraction(s2,den) == v
        assert Fraction(s4,den) == q
        moment_checks += 3

    for m in range(0,250):
        a,b=vm(m),vm(m+1)
        for r in list(range(0,m+1)) + list(range(m+1,320)):
            assert qm(r) >= chord(m,vm(r))
            chord_checks += 1

        for num in range(0,21):
            th=Fraction(num,20)
            v=a+th*(b-a)
            q=(1-th)*qm(m)+th*qm(m+1)
            assert q == chord(m,v)
            equality_checks += 1
            if v:
                vv,scaled,rhs=phase_formula(m,th)
                assert vv==v and scaled==rhs
                phase_checks += 1

    rng=random.Random(20261001)
    for _ in range(20000):
        support=sorted(set(rng.randrange(0,80) for __ in range(rng.randrange(2,7))))
        raw=[rng.randrange(1,20) for __ in support]
        total=sum(raw)
        weights=[Fraction(x,total) for x in raw]
        v=sum(w*vm(m) for w,m in zip(weights,support))
        q=sum(w*qm(m) for w,m in zip(weights,support))
        if v==0:
            continue
        cell=find_cell(v)
        assert q >= chord(cell,v)
        random_mix_checks += 1

    for th in (Fraction(0),Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(1)):
        target=-Fraction(1,5)+Fraction(12,5)*th*(1-th)
        prev=None
        for m in (100,300,1000,3000):
            a,b=vm(m),vm(m+1)
            v=a+th*(b-a)
            scaled=v*(chord(m,v)/(v*v)-Fraction(9,5))
            err=abs(float(scaled-target))
            if prev is not None:
                assert err <= prev + 1e-12
            prev=err
            phase_checks += 1

    print(
        "VERIFY_OK "
        f"moment_checks={moment_checks} "
        f"chord_checks={chord_checks} "
        f"equality_checks={equality_checks} "
        f"random_mix_checks={random_mix_checks} "
        f"phase_checks={phase_checks}"
    )

if __name__=="__main__":
    run()
