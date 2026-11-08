#!/usr/bin/env python3
"""Independent finite combinatorial and analytic checks for leaf counts of weighted fan spanning trees."""
from fractions import Fraction as F
from itertools import combinations
import math

checks = 0

def blockpoly(length):
    if length == 1: return {1:1}
    if length == 2: return {1:2}
    return {1:2, 2:length-2}

def polynomial_comp(n,t):
    # This computation independently combines positive-length compositions.
    dp=[{} for _ in range(n+1)]
    dp[0][0]=F(1)
    for i in range(1,n+1):
        for j in range(1,i+1):
            for prev, val in dp[i-j].items():
                for exp,coeff in blockpoly(j).items():
                    dp[i][prev+exp]=dp[i].get(prev+exp,F(0))+val*t*coeff
    # hub leaf if and only if one segment.
    for exp,coeff in blockpoly(n).items():
        dp[n][exp]-=t*coeff
        dp[n][exp+1]=dp[n].get(exp+1,F(0))+t*coeff
    return {e:c for e,c in dp[n].items() if c}

def exhaustive(n,t):
    # n path vertices 0,...,n-1 and an extra hub n.
    E=[(i,i+1,1) for i in range(n-1)]+[(i,n,t) for i in range(n)]
    dist={}
    for chosen in combinations(E,n):
        parent=list(range(n+1))
        def find(a):
            while parent[a]!=a: a=parent[a]
            return a
        degree=[0]*(n+1);weight=F(1)
        ok=True
        for a,b,w in chosen:
            ra,rb=find(a),find(b)
            if ra==rb:ok=False;break
            parent[ra]=rb
            degree[a]+=1;degree[b]+=1;weight*=w
        if not ok:continue
        leaves=sum(d==1 for d in degree)
        dist[leaves]=dist.get(leaves,F(0))+weight
    return dist

for n in range(1,8):
    for t in [F(1,2),F(1),F(2),F(5,3)]:
        a=polynomial_comp(n,t)
        b=exhaustive(n,t)
        assert a==b,(n,t,a,b)
        checks+=1

# An independent moment recurrence, using only block endpoint counts at z=1.
def moments(n,t):
    t=float(t)
    f=[0.0]*(n+1);g=f.copy();h=f.copy();f[0]=1.0
    for i in range(1,n+1):
        for j in range(1,i+1):
            b1=1 if j==1 else 2 if j==2 else j
            db=1 if j==1 else 2 if j==2 else 2*j-2
            d2b=0 if j<=2 else 2*(j-2)
            f[i]+=t*b1*f[i-j]
            g[i]+=t*(b1*g[i-j]+db*f[i-j])
            h[i]+=t*(b1*h[i-j]+2*db*g[i-j]+d2b*f[i-j])
    # correction (z-1)t*a_n(z), derivatives at 1: first t*n, second 2t*a_n'(1).
    g[n]+=t*n
    h[n]+=2*t*(1 if n==1 else 2 if n==2 else 2*n-2)
    mean=g[n]/f[n]
    var=h[n]/f[n]+mean-mean*mean
    return float(mean),float(var)

# Exact rational Sturm sequence; coefficients are low-to-high.
def trim(a):
    while a and a[-1]==0: a.pop()
    return a

def derivative(a):
    return trim([i*a[i] for i in range(1,len(a))])

def remainder(a,b):
    a=[F(x) for x in a];b=[F(x) for x in b]
    while len(a)>=len(b) and a:
        k=len(a)-len(b); c=a[-1]/b[-1]
        for j,v in enumerate(b):a[j+k]-=c*v
        trim(a)
    return a

def evalp(a,x):
    z=F(0)
    for c in reversed(a):z=z*x+c
    return z

def signs(a,x):
    y=evalp(a,x)
    return 1 if y>0 else -1 if y<0 else 0

def mult(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return trim(out)

def add(a,b):
    out=[F(0)]*max(len(a),len(b))
    for i,x in enumerate(a):out[i]+=x
    for i,x in enumerate(b):out[i]+=x
    return trim(out)

p=[F(x) for x in [-1,7,-16,12,3,-9,6,6]]
seq=[p,derivative(p)]
while len(seq[-1])>1:
    rem=remainder(seq[-2],seq[-1])
    assert rem
    seq.append([-x for x in rem])

lo,hi=F(0),F(1)
for _ in range(90):
    mid=(lo+hi)/2
    if evalp(p,mid)<0:lo=mid
    else:hi=mid
root=float((lo+hi)/2)
tstar=(1-root)**2/root
mu=(1-root)*(1+root**2)/(1+root)
v=root*(1-root)*(3*root**5+6*root**2-3*root+2)/(1+root)**3
for n in [20,50,100,150]:
    mean,var=moments(n,F(3,2))
    print('n',n,'mean/n',mean/n,'variance/n',var/n)
    checks+=1
sg0=[signs(q,F(0)) for q in seq]
sg1=[signs(q,F(1)) for q in seq]
assert sg0==[-1,1,1,1,-1,1,1,-1]
assert sg1==[1,1,1,-1,-1,1,-1,-1]
assert (sum(a!=b for a,b in zip(sg0,sg0[1:]))-sum(a!=b for a,b in zip(sg1,sg1[1:])))==1
checks+=3
# An exact polynomial identity certifies dv/dr = -2 p(r)/(1+r)^4.
# Set v=A/(1+r)^3, A=r(1-r)(3r^5+6r^2-3r+2).
A=mult(mult([F(0),F(1)], [F(1),F(-1)]), [F(2),F(-3),F(6),F(0),F(0),F(3)])
assert add(add(mult(derivative(A),[F(1),F(1)]), [-3*x for x in A]), [2*x for x in p]) == []
checks+=1
print('r_star',root,'t_star',tstar,'mean_density',mu,'maximum_variance_density',v)
print('VERIFY_OK',checks,'groups of independent exact/numerical checks')
