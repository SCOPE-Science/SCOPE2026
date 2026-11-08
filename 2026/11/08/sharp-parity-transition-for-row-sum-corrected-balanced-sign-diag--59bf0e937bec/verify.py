"""Exact finite consistency checks for exchangeable fixed-count sign diagonal probes.
The symbolic all-dimension result is proved separately in RESULT.md.
"""
from itertools import product
from fractions import Fraction as F
from math import comb

assertions=0

def chk(a,b):
    global assertions
    assertions+=1
    assert a==b, (a,b)

for n in range(2,10):
    a=[[F(((13*i+7*j+3*i*j)%17)-8,5) for j in range(n)] for i in range(n)]
    r=[sum(row) for row in a]
    for c in range(n+1):
        signs=[z for z in product((-1,1),repeat=n) if z.count(1)==c]
        S=2*c-n
        rho=F(S*S-n,n*(n-1))
        chk(F(sum(z[0]*z[1] for z in signs),len(signs)),rho)
        if rho==1:
            continue
        for i in range(n):
            v=[F(sum(z[i]*sum(a[i][j]*z[j] for j in range(n)) for z in signs),len(signs))]
            chk(v[0],(1-rho)*a[i][i]+rho*r[i])
            est=[(z[i]*sum(a[i][j]*z[j] for j in range(n))-rho*r[i])/(1-rho) for z in signs]
            chk(F(sum(est),len(est)),a[i][i])
            empirical=F(sum((e-a[i][i])**2 for e in est),len(est))
            row=[a[i][j] for j in range(n) if j!=i]
            theoretical=(sum(x*x for x in row)+rho*sum(row)**2)/(1-rho)
            chk(empirical,theoretical)
            lower=F(0 if n%2==0 else 1,n*(n-1))-F(1,n-1)
            chk(rho>=lower,True)
            opt=(sum(x*x for x in row)+lower*sum(row)**2)/(1-lower)
            chk(empirical>=opt,True)
    # balanced optimal envelope is uniformly below independent signs
    best=F(-1,n-1) if n%2==0 else F(-1,n)
    for i in range(n):
        row=[a[i][j] for j in range(n) if j!=i]
        v=(sum(x*x for x in row)+best*sum(row)**2)/(1-best)
        chk(v<=sum(x*x for x in row),True)
        if n%2==0:
            chk(v,(F(n-1)*sum(x*x for x in row)-sum(row)**2)/n)
        else:
            chk(v,(F(n)*sum(x*x for x in row)-sum(row)**2)/(n+1))
# constant-off-diagonal example, diagonal arbitrary
for n in range(2,10):
    best=F(-1,n-1) if n%2==0 else F(-1,n)
    off=[F(3,7)]*(n-1)
    v=(sum(x*x for x in off)+best*sum(off)**2)/(1-best)
    if n%2==0:
        chk(v,F(0))
    else:
        chk(v,F(n-1,n+1)*F(9,49))
# Equal-total-query-budget comparison: one deterministic all-ones product plus
# m balanced products against m+1 independent-sign products.
for n in range(2,10):
    b=[[F(0) for j in range(n)] for i in range(n)]
    if n==2:
        b[0][1]=F(2)
        b[1][0]=F(3)
    else:
        for i in range(n):
            other=[j for j in range(n) if j!=i]
            b[i][other[0]]=F(2)
            b[i][other[1]]=F(-2)
    fro=sum(b[i][j]**2 for i in range(n) for j in range(n))
    sums=sum(sum(row)**2 for row in b)
    chk(fro>0,True)
    if n>=3:chk(sums,F(0))
    rho=F(-1,n-1) if n%2==0 else F(-1,n)
    for m in range(1,n+3):
        opt=(fro+rho*sums)/(m*(1-rho))
        iid=fro/F(m+1)
        if n==2:cmp=-1
        elif n%2==0:cmp=1 if m<n-1 else (0 if m==n-1 else -1)
        else:cmp=1 if m<n else (0 if m==n else -1)
        chk((opt>iid)-(opt<iid),cmp)

print(f"PASS {assertions} exact-rational assertions; n=2..9, fixed-count sign orbits and matched query budgets")
