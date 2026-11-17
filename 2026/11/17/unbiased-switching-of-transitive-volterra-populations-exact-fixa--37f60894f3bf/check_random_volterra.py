"""Finite exact checks for the randomly sign-switched transitive Volterra population map."""
from fractions import Fraction as F
from itertools import product

def update(x, sign, a):
    return tuple(x[i]*(1+sign*sum(a[i][j]*x[j] for j in range(len(x)))) for i in range(len(x)))

for n in (2,3,4):
    a=[[F(0) for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            a[i][j]=F(1+i+j, 3+n*2)
            a[j][i]=-a[i][j]
    x=tuple(F(2*i+1,n*n) for i in range(n))
    x=tuple(v/sum(x) for v in x)
    xp=update(x,1,a);xm=update(x,-1,a)
    assert all(v>0 for v in xp+xm)
    assert sum(xp)==sum(xm)==1
    assert all((xp[i]+xm[i])/2==x[i] for i in range(n))
    assert all(((xp[i]*xp[i]+xm[i]*xm[i])/2-x[i]*x[i]) == (x[i]*sum(a[i][j]*x[j] for j in range(n)))**2 for i in range(n))
    for k in range(1,9):
        t=[update(x,s[0],a) for s in product((1,-1),repeat=1)] if k==1 else None
        # cumulative exact weighted expectation over all 2^k sign sequences
        totals=[F(0)]*n
        for signs in product((1,-1),repeat=k):
            v=x
            for s in signs: v=update(v,s,a)
            for i in range(n):totals[i]+=v[i]
        assert all(totals[i]==2**k*x[i] for i in range(n))
print('RANDOM_VOLTERRA_TRANSITIVE_EXACT_OK dimensions=2,3,4 sign_words_total=1530 fair_mean_martingale=PASS quadratic_variation=PASS simplex=PASS')
