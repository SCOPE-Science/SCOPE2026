"""Independent exact checks of crossing–nesting covariance identities.

Requires only Python 3 standard library. Finite enumeration does not constitute
proof of the all-order theorem; proof is in RESULT.md.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import comb

checks = 0

def equal(a, b, tag):
    global checks
    checks += 1
    assert a == b, (tag, a, b)

# A polynomial in the two ordered chord endpoints 0<=l<=r<=1.
def plus(a, b):
    c = dict(a)
    for k,v in b.items():
        c[k] = c.get(k,F(0)) + v
    return {k:v for k,v in c.items() if v}

def mul(a, b):
    c = {}
    for (i,j),x in a.items():
        for (k,m),y in b.items():
            t=(i+k,j+m)
            c[t]=c.get(t,F(0))+x*y
    return {k:v for k,v in c.items() if v}

def scale(a,x):
    return {k:v*x for k,v in a.items() if v*x}

def mean(a):
    return sum((v*F(2,(i+1)*(i+j+2)) for (i,j),v in a.items()),F(0))

one={(0,0):F(1)}
l={(1,0):F(1)}
r={(0,1):F(1)}
t=plus(r,scale(l,-1))
pc=scale(mul(t,plus(one,scale(t,-1))),2)
pn=plus(mul(t,t),scale(mul(l,plus(one,scale(r,-1))),2))
pa=plus(one,scale(plus(pc,pn),-1))
for name,p in [('crossing',pc),('nesting',pn),('alignment',pa)]:
    equal(mean(p),F(1,3),name+' mean')
equal(mean(mul(pc,pc)),F(2,15),'cross projection squared')
equal(mean(mul(pn,pn)),F(2,15),'nest projection squared')
equal(mean(mul(pc,pn)),F(1,9),'orthogonality')
equal(mean(mul(pa,pa)),F(7,45),'alignment projection squared')
equal(mean(mul(pc,pa)),F(4,45),'cross-alignment projection')
equal(mean(mul(pn,pa)),F(4,45),'nest-alignment projection')

@lru_cache(None)
def matchings(vertices):
    if not vertices:
        return ((),)
    first, rest = vertices[0], vertices[1:]
    return tuple(((first,other),)+tail
                 for i,other in enumerate(rest)
                 for tail in matchings(rest[:i]+rest[i+1:]))

def classify(a,b):
    x,y=a;u,v=b
    if u<x:
        x,y,u,v=u,v,x,y
    if y<u: return 0 # separated/aligned
    if y<v: return 1 # crossing
    return 2 # nesting

for n in range(2,8):
    moments=[0,0,0]
    square=[0,0,0]
    mixed=[0,0,0] # A-C, A-N, C-N
    count=0
    for M in matchings(tuple(range(2*n))):
        count+=1
        stats=[0,0,0]
        for i in range(n):
            for j in range(i+1,n):
                stats[classify(M[i],M[j])]+=1
        for j in range(3):
            moments[j]+=stats[j]
            square[j]+=stats[j]*stats[j]
        mixed[0]+=stats[0]*stats[1]
        mixed[1]+=stats[0]*stats[2]
        mixed[2]+=stats[1]*stats[2]
    equal(count, __import__('math').prod(range(1,2*n,2)),('number matchings',n))
    m=F(n*(n-1),6)
    means=[F(x,count) for x in moments]
    for j in range(3):equal(means[j],m,('means',n,j))
    vars=[F(square[j],count)-means[j]**2 for j in range(3)]
    goalvars=[F(n*(n-1)*(2*n+1),45), F(n*(n-1)*(n+3),45),F(n*(n-1)*(n+3),45)]
    for j in range(3):equal(vars[j],goalvars[j],('variance',n,j))
    cov=[F(mixed[j],count)-means[[0,0,1][j]]*means[[1,2,2][j]] for j in range(3)]
    goalcov=[-F(n*(n-1)*(2*n+1),90)]*2+[-F(n*(n-1),18)]
    for j in range(3):equal(cov[j],goalcov[j],('covariance',n,j))
    equal(cov[2]/vars[1],-F(5,2*(n+3)),('correlation',n))
print('VERIFY_OK',checks,'exact assertions; exhaustive matchings through seven chords; polynomial integrals exact')
