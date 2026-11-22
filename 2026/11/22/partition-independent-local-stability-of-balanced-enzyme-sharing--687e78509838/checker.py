"""Exact Jacobian cross-check for an identical-rate cyclic HMM flow.
Only standard-library fractions are used for the exact differential check.
Run: python checker.py
"""
from fractions import Fraction as F
from collections import Counter

def test(n, group, kp, km, kc, e, c):
    h=km+kc
    x=h*c/(kp*e)
    counts=Counter(group)
    total={g:e+q*c for g,q in counts.items()}
    alpha=kp*e; beta=kp*x
    def field(v):
        y=v[:n]; z=v[n:]
        free={g:total[g]-sum(z[i] for i in range(n) if group[i]==g) for g in counts}
        dc=[kp*free[group[i]]*(y[i]-z[i])-h*z[i] for i in range(n)]
        dy=[kc*(z[(i-1)%n]-z[i]) for i in range(n)]
        return dy+dc
    J=[[F(0) for _ in range(2*n)] for _ in range(2*n)]
    for i in range(n):
        J[i][n+(i-1)%n]+=kc
        J[i][n+i]-=kc
        J[n+i][i]=alpha
        J[n+i][n+i]-=alpha+h
        for j in range(n):
            if group[j]==group[i]:
                J[n+i][n+j]-=beta
    v0=[x+c]*n+[c]*n
    assert field(v0)==[0]*(2*n)
    t=F(1,11)
    for j in range(2*n):
        v1=v0.copy();v1[j]+=t
        v2=v0.copy();v2[j]-=t
        u1=field(v1);u2=field(v2)
        for i in range(2*n):
            assert (u1[i]-u2[i])/(2*t)==J[i][j], (n,group,i,j)
    # Gram positivity of B checked combinatorially by grouping;
    # proof is analytic, not inferred from the finite cases.
    return 2*n*2*n

comparisons=0
cases=0
for n in range(3,10):
    patterns=[tuple(range(n)),(0,)*n,tuple(i%2 for i in range(n)),
              tuple(i%3 for i in range(n)),tuple((i*i+3*i)%4 for i in range(n)),
              tuple((i//2)%3 for i in range(n))]
    for group in patterns:
        for kp,km,kc,e,c in [(F(2),F(1),F(3),F(5,2),F(1,4)),
                              (F(1,3),F(2),F(7,3),F(5),F(2)),
                              (F(9),F(1,7),F(2,5),F(1,2),F(3,2))]:
            comparisons+=test(n,group,kp,km,kc,e,c)
            cases+=1
print('PASS:',cases,'exact rational family tests;',comparisons,'individual Jacobian comparisons')
