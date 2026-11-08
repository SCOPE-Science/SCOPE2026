"""Independent exact state-space verification of a fixed-size SI surveillance theorem.
Uses Python standard library only; the analytic interval proof is in RESULT.md.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb

A = frozenset(range(3))
B = frozenset(range(3, 7))
N = 7
assert len(A) == 3 and len(B) == 4
# Terms c * t^j * exp(-r*t), in units of one edge's infection rate.
terms = {
 0:[(F(135,280),0,3),(F(336,280),0,4),(F(-405,280),0,5),(F(105,280),0,7),(F(-11,280),0,9)],
 1:[(F(107,126),0,3),(F(228,126),0,4),(F(-594,126),0,5),(F(352,126),0,6),(F(-21,126),0,7),(F(120,126),1,6)],
 2:[(F(23,28),0,3),(F(32,28),0,4),(F(-72,28),0,5),(F(40,28),0,6),(F(-7,28),0,7)],
 3:[(F(4,7),0,3)],
}
checks=0
for a in range(4):
    sensors=set(range(a))|set(range(3,3+(3-a)))
    uns=sorted(set(range(N))-sensors)
    assert len(uns)==4
    states=sorted((frozenset(s) for z in range(1,5) for s in combinations(uns,z)),key=lambda s:(len(s),tuple(sorted(s))))
    dim=len(states)
    assert dim==15
    pos={s:i for i,s in enumerate(states)}
    Q=[[F(0) for j in range(dim)] for i in range(dim)]
    alpha=[F(1,7) if len(s)==1 else F(0) for s in states]
    for i,s in enumerate(states):
        for v in set(range(N))-s:
            hazard=sum(1 for w in s if (v in A)!=(w in A))
            if hazard:
                Q[i][i]-=hazard
                if v not in sensors:
                    Q[i][pos[s|{v}]]+=hazard
    diag=[int(-Q[i][i]) for i in range(dim)]
    for c,p,r in terms[a]:
        assert diag.count(r)>=p+1,(a,p,r,diag)
        checks+=1
    # F(t)=alpha * exp(Qt) * 1. First dim derivatives determine solution
    # since every term in the proposed formula is annihilated by det(DI-Q).
    vec=[F(1)]*dim
    for k in range(dim):
        actual=sum(alpha[i]*vec[i] for i in range(dim))
        predicted=sum(c*comb(k,p)*(-r)**(k-p) for c,p,r in terms[a] if k>=p)
        assert actual==predicted,(a,k,actual,predicted)
        checks+=1
        vec=[sum(Q[i][j]*vec[j] for j in range(dim)) for i in range(dim)]
    # Survival at zero is fraction starting unmonitored (4 of 7).
    assert sum(c for c,p,r in terms[a] if p==0)==F(4,7)
    checks+=1

# Coefficient identities for (1-x) R(x), and for (1-x) P(x).
def poly_mul(x,y):
    out=[F(0)]*(len(x)+len(y)-1)
    for i,u in enumerate(x):
        for j,v in enumerate(y):out[i+j]+=u*v
    return out

# Differences after factor x^3 (unit infection hazard normalization).
D03=[F(-25),F(336),F(-405),F(0),F(105),F(0),F(-11)]
R=[F(-25),F(311),F(-94),F(-94),F(11),F(11)]
assert poly_mul([F(1),F(-1)],R)==D03
checks+=1
D23=[F(7),F(32),F(-72),F(40),F(-7)]
P23=[F(7),F(39),F(-33),F(7)]
assert poly_mul([F(1),F(-1)],P23)==D23
checks+=1
D13lower=[F(35),F(228),F(-594),F(472),F(-141)]
P13=[F(35),F(263),F(-331),F(141)]
assert poly_mul([F(1),F(-1)],P13)==D13lower
checks+=1
assert 331**2 -4*141*263 == -38771
checks+=1
assert R[0]<0 and sum(R)>0
checks+=1
# The mean of T_0 and T_3 = integrals of the displayed survival functions.
means={a:sum(c*F(1,r**(p+1))*(1 if p==0 else 1) for c,p,r in terms[a]) for a in [0,2,3]}
# For p=1, integral t exp(-r t)=r^-2; for p=0 integral exp(-r t)=r^-1.
assert means[0]==F(139,630),(means[0])
assert means[3]==F(4,21),(means[3])
assert means[0]-means[3]==F(19,630)
checks+=3
print('PASS: full independent 15-state exact-generator derivative matching, term spectra, mean values, polynomial identities; checks=',checks)
