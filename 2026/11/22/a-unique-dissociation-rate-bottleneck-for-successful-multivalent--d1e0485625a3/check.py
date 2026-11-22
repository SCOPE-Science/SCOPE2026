"""Exact finite checks for the homogeneous two-absorber bond chain.

Run: python3 check.py
Dependencies: Python standard library only.
These tests corroborate the algebra and finite examples; the all-threshold
uniqueness and asymptotic laws require the accompanying analytical proof.
"""
from fractions import Fraction as F
from decimal import Decimal, getcontext


def conv(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b): z[i+j]+=u*v
    return z


def polyadd(a,b,k=1):
    z=[0]*max(len(a),len(b))
    for i,u in enumerate(a): z[i]+=u
    for i,u in enumerate(b): z[i]+=k*u
    while len(z)>1 and z[-1]==0:z.pop()
    return z


def derivative(a):
    return [(k+1)*a[k+1] for k in range(len(a)-1)] or [0]


def recurrence(n):
    # D_n(s) at s=0 and its s derivative, as polynomials in x.
    d0, d1=[1],[1,1]
    v0,v1=[0],[1]
    if n==0:return d0,v0
    for k in range(2,n+1):
        d=polyadd(conv([1,1],d1),conv([0,1],d0),-1)
        v=polyadd(polyadd(d1,conv([1,1],v1)),conv([0,1],v0),-1)
        d0,d1=d1,d
        v0,v1=v1,v
    return d1,v1


def solve(a,b):
    n=len(b)
    t=[[F(v) for v in a[i]]+[F(b[i])] for i in range(n)]
    for k in range(n):
        pivot=next(i for i in range(k,n) if t[i][k])
        t[k],t[pivot]=t[pivot],t[k]
        v=t[k][k];t[k]=[w/v for w in t[k]]
        for i in range(n):
            if i==k:continue
            v=t[i][k]
            if v:t[i]=[u-v*w for u,w in zip(t[i],t[k])]
    return [r[-1] for r in t]


def direct_conditional_time(n,x):
    # Interior states 1,...,n; upper absorbing state n+1.
    # Solve Qg=-h without using determinants or spectral representation.
    h=[F(0)]+[sum(x**j for j in range(i))/sum(x**j for j in range(n+1))
                 for i in range(1,n+1)]+[F(1)]
    a=[[F(0)]*n for _ in range(n)]
    for i in range(n):
        a[i][i]=1+x
        if i>0:a[i][i-1]=-x
        if i+1<n:a[i][i+1]=-1
    g=solve(a,h[1:-1])
    return g[0]/h[1]


count=0
for n in range(1,23):
    d,v=recurrence(n)
    want_d=[1]*(n+1)
    want_v=[(i+1)*(n-i) for i in range(n)]
    assert d==want_d and v==want_v,(n,d,v)
    r=polyadd(conv(derivative(v),d),conv(v,derivative(d)),-1)
    r += [0]*((2*n-1)-len(r))
    for j,c in enumerate(r):
        if j <= n-2:
            want=(j+1)*(j+2)*(j+3)*(n-j-2)//6
        else:
            want=(j-2*n)*(j-2*n-1)*(j-2*n+1)*(j-n+2)//6
        assert c==want,(n,j,c,want)
        count+=1

for n in range(1,10):
    for x in [F(0),F(1,5),F(1,2),F(1),F(2),F(5)]:
        expected=sum(F((i+1)*(n-i))*x**i for i in range(n))/sum(x**i for i in range(n+1))
        result=direct_conditional_time(n,x)
        assert expected==result,(n,x,expected,result)
        count+=1

# Bisection of the exact rational derivative numerator via high-precision Horner.
getcontext().prec=70

def optimum(n):
    d,v=recurrence(n)
    r=polyadd(conv(derivative(v),d),conv(v,derivative(d)),-1)
    def val(x):
        y=Decimal(0)
        for c in r[::-1]: y=y*x+Decimal(c)
        return y
    l=Decimal(0);h=Decimal(1)
    assert val(l)>0 and val(h)<0
    for _ in range(220):
        mid=(l+h)/2
        if val(mid)>0:l=mid
        else:h=mid
    return (l+h)/2

for m in (4,5,8,20,40,80,160):
    x=optimum(m-1)
    print(f'm={m:3d}  optimal rho={x:.16f}  m^2(1-rho)={(Decimal(m)**2)*(1-x):.12f}')
    count+=1
assert Decimal('0.28281476')<optimum(3)<Decimal('0.28281477')
print(f'PASS: {count} exact coefficient, independent rational-chain, and high-precision threshold checks')
