"""Exact-rational diagnostic checks for periodic seed-crop chronology formulas."""
from fractions import Fraction as F
from random import Random


def response(s, K, kind):
    if kind == 2:
        return s / (K + s)
    if kind == 3:
        return s*s / (K*K + s*s)
    raise ValueError(kind)


def cycle_loss(crop, rho, recruit, bg, K, kind):
    # periodic solution, obtained by closing the three-step linear recurrence
    assert len(crop) == 3
    p = (bg*(1+rho+rho*rho) + recruit*(crop[2] + rho*crop[1] + rho*rho*crop[0])) / (1-rho**3)
    total = F(0)
    for c in crop:
        total += p*response(c, K, kind)
        p = rho*p + bg + recruit*c
    return total


def formula(a,b,c,rho,recruit,K,kind):
    V = (a-b)*(a-c)*(b-c)
    if kind == 2:
        det = K*V/((K+a)*(K+b)*(K+c))
    else:
        det = K*K*V*(a*b+a*c+b*c-K*K)/((K*K+a*a)*(K*K+b*b)*(K*K+c*c))
    return recruit*det/(1+rho+rho*rho)


checks = 0
for a,b,c in [(F(3),F(2),F(1)),(F(5),F(3),F(2))]:
    for K in [F(1),F(2),F(3),F(4),F(7)]:
        for kind in [2,3]:
            for rho in [F(0),F(1,2),F(4,5)]:
                actual=cycle_loss((a,b,c),rho,F(1,20),F(0),K,kind)-cycle_loss((a,c,b),rho,F(1,20),F(0),K,kind)
                assert actual==formula(a,b,c,rho,F(1,20),K,kind)
                checks+=1
assert formula(F(3),F(2),F(1),F(1,2),F(1,20),F(2),3)==F(1,325)
assert formula(F(3),F(2),F(1),F(1,2),F(1,20),F(4),3)==-F(8,14875)
checks+=2
# Arbitrary exact rational tuple checks, includes background immigration and near-1 retention.
rng=Random(85371)
for _ in range(3000):
    crop=[F(rng.randrange(1,50),rng.randrange(1,13)) for j in range(3)]
    rho=F(rng.randrange(0,20),rng.randrange(20,40))
    recruit=F(rng.randrange(1,20),rng.randrange(1,21))
    bg=F(rng.randrange(0,20),rng.randrange(1,22))
    K=F(rng.randrange(1,30),rng.randrange(1,11))
    for kind in (2,3):
        v=cycle_loss(crop,rho,recruit,bg,K,kind)-cycle_loss((crop[0],crop[2],crop[1]),rho,recruit,bg,K,kind)
        assert v==formula(*crop,rho,recruit,K,kind)
        checks+=1
# Verify minimum period: cycles of 1 or 2 are equal up to rotation upon reversal.
for x,y in [(F(1),F(3)),(F(5,4),F(9,8))]:
    for rho in (F(0),F(1,2)):
        p0=F(1,20)
        p=(p0*(y+rho*x))/(1-rho*rho)
        Lxy=p*response(x,F(2),3)+(rho*p+p0*x)*response(y,F(2),3)
        pr=p0*(x+rho*y)/(1-rho*rho)
        Lyx=pr*response(y,F(2),3)+(rho*pr+p0*y)*response(x,F(2),3)
        assert Lxy==Lyx
        checks+=1
print(f"exact-rational assertions passed: {checks}")
