"""Supplementary finite-dimensional rational diagnostics of the stated channel formulas.
Only the finite calculations are checked; universal statements use the proof.
"""
from fractions import Fraction as F
from math import factorial

def mpow_on_diag(alpha,p,n):
    # alpha is a nonnegative integer, moments omega_j = factorial(j)*factorial(alpha+1)/factorial(j+alpha+1)
    o1=F(1,alpha+2)
    delta=lambda j:F(j+alpha+2,j+1)
    b=[1-o1*delta(j) for j in range(p+1)]
    a=[F(0)]+[o1*delta(j-1) for j in range(1,p+1)]
    v=[F(0)]*(p+1);v[p]=1
    for j in range(p-1,-1,-1):
        v[j]=a[j+1]*v[j+1]/(b[p]-b[j])
    c=F((p+1)**p,(alpha+1)**p)
    for j in range(p):c*=F(alpha+2+j,j+1)
    assert v[0]==c
    assert all(v[j]>v[j+1] for j in range(p))
    x=[F(0)]*p+[F(1)]
    for _ in range(n):
        y=[b[j]*x[j] for j in range(p+1)]
        for j in range(1,p+1):y[j-1]+=a[j]*x[j]
        x=y
    return b[p],c,x,v

def verify():
    assertions=0
    for alpha in range(4):
        for p in range(1,11):
            r,c,x,v=mpow_on_diag(alpha,p,65)
            assert r==F((alpha+1)*p,(alpha+2)*(p+1));assertions+=1
            assert c>0;assertions+=1
            # At t=65, the largest coordinate is index 0 for these small p;
            # compare exact rational error against the next eigenvalue scale.
            if p<9:
                assert x[0]==max(x);assertions+=1
            if p<=5:
                # the top eigencomponent is exact and errors are exponentially smaller
                next_rate=F((alpha+1)*(p-1),(alpha+2)*p)
                diff=max(abs(xx-r**65*vv) for xx,vv in zip(x,v))
                if p==1:
                    assert diff==0
                else:
                    assert diff < 100000000000000*next_rate**65
                assertions+=1
    for alpha in range(4):
        o1=F(1,alpha+2)
        delta=lambda j:F(j+alpha+2,j+1)
        for n in range(1,26):
            p=n+2
            x=[F(1)]*(p+1)
            for k in range(n):
                y=[(1-o1*delta(j))*x[j] for j in range(p+1)]
                for j in range(1,p+1):y[j-1]+=o1*delta(j-1)*x[j]
                x=y
            assert x[0]==1 and all(0<=t<=1 for t in x)
            assertions+=1
    print('Passed',assertions,'exact-rational assertions')

if __name__=='__main__':verify()
