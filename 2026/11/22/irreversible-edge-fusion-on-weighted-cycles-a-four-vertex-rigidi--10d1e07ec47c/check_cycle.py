"""Exact arithmetic checks of weighted cycle TV KKT witnesses.

The analytic all-data result uses a separate proof; this script checks only
explicit finite certificates and the algebraic transition formulas.
"""
from fractions import Fraction as F

def validate(n, mass, weight, data, lam, sol, flux):
    assert all(F(v) > 0 for v in mass)
    assert all(F(v) > 0 for v in weight)
    for i in range(n):
        assert mass[i]*(sol[i]-data[i])+lam*(flux[(i-1)%n]-flux[i]) == 0
        delta=sol[(i+1)%n]-sol[i]
        assert abs(flux[i]) <= weight[i]
        if delta>0: assert flux[i]==weight[i]
        if delta<0: assert flux[i]==-weight[i]
    return True

def n4(lam):
    a=list(map(F,(1,2,3,4))); m=[F(1)]*4
    y=list(map(F,(5,-3,105,-107)))
    if lam<=2:
        q=[3-F(4)/lam,F(2),F(-3),F(4)]
        x=[F(1)-lam,F(1)-lam,F(105)-5*lam,F(-107)+7*lam]
    else:
        q=list(map(F,(1,2,-3,4)))
        x=[F(5)-3*lam,F(-3)+lam,F(105)-5*lam,F(-107)+7*lam]
    assert validate(4,m,a,y,lam,x,q)
    return x,q

def n3(lam):
    a=list(map(F,(1,1,4))); m=[F(1)]*3
    y=list(map(F,(5,0,-105)))
    if lam<=5:
        q=[F(3,2)-F(5,2)/lam,F(-1),F(4)]
        x=[(F(5)-5*lam)/2,(F(5)-5*lam)/2,F(-105)+5*lam]
    else:
        q=[F(1),F(-1),F(4)]
        x=[F(5)-3*lam,-2*lam,F(-105)+5*lam]
    assert validate(3,m,a,y,lam,x,q)
    return x,q

if __name__=='__main__':
    cases4=[F(1),F(5,4),F(3,2),F(7,4),F(2),F(9,4),F(5,2),F(3)]
    cases3=[F(1),F(2),F(3),F(4),F(5),F(11,2),F(6),F(7)]
    for t in cases4: n4(t)
    for t in cases3: n3(t)
    x_before,_=n4(F(3,2)); x_after,_=n4(F(5,2))
    assert x_before[0]==x_before[1] and x_after[0]!=x_after[1]
    x_before,_=n3(F(3)); x_after,_=n3(F(6))
    assert x_before[0]==x_before[1] and x_after[0]!=x_after[1]
    # A stable nonconstant triangle for all data by the analytic criterion.
    a=[F(1),F(2),F(2)];m=[F(1)]*3
    assert all(abs(m[(i+1)%3]*a[(i-1)%3]-m[i]*a[(i+1)%3]) <= (m[i]+m[(i+1)%3])*a[i] for i in range(3))
    # For nonconstant cycles with n>=4, a minimum adjacent to a larger
    # weight yields the strict local obstruction, for arbitrary masses.
    import random
    rng=random.Random(47)
    for n in range(4,21):
        for _ in range(100):
            w=[F(rng.randint(1,30)) for i in range(n)]
            if len(set(w))==1: continue
            mm=[F(rng.randint(1,30)) for i in range(n)]
            assert any((mm[i]+mm[(i+1)%n])*w[i] < mm[(i+1)%n]*w[(i-1)%n]+mm[i]*w[(i+1)%n] for i in range(n))
    print('PASS: 16 exact rational KKT certificates; 1700 finite cyclic minimum-obstruction trials; triangle exception')
