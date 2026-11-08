"""Finite exact checks for the Euclidean diameter of two-level preorder polytopes.

These checks corroborate but do not establish the universal theorem; see RESULT.md.
Requires Python 3 standard library only.
"""
from itertools import product
from math import comb

CHECKS = 0

def check(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)

def sqdist(p, q):
    return sum((a-b)*(a-b) for a,b in zip(p,q))

def generating_points(m,n):
    out = set()
    for x in product((0,1),repeat=m):
        slack = m-sum(x)
        for b in product((0,1),repeat=n):
            for pos in range(n+1):
                y = list(b)
                if pos:
                    y[pos-1] += slack
                out.add(x+tuple(y))
    return sorted(out)

def feasible(v,m,n):
    x,y=v[:m],v[m:]
    if any(a<0 or a>1 for a in x) or any(a<0 for a in y):return False
    for mask in range(1<<n):
        S=sum(y[j] for j in range(n) if (mask>>j)&1)
        if sum(x)+S>m+mask.bit_count():return False
    return True

def expected_pairs(m,n):
    out=set()
    for i in range(n):
        for j in range(i+1,n):
            for bits in product((0,1),repeat=n-2):
                y1=[0]*n;y2=[0]*n
                y1[i]=m+1;y2[j]=m+1
                t=iter(bits)
                for l in range(n):
                    if l!=i and l!=j:
                        z=next(t);y1[l]=z;y2[l]=1-z
                a=(0,)*m+tuple(y1)
                b=(0,)*m+tuple(y2)
                out.add(tuple(sorted((a,b))))
    return out

def pairs_at_max(points, value):
    out=set()
    for i,a in enumerate(points):
        for b in points[i+1:]:
            if sqdist(a,b)==value:
                out.add((a,b))
    return out

for m in range(1,5):
    for n in range(2,6):
        pts=generating_points(m,n)
        d=2*(m+1)**2+n-2
        for p in pts:check(feasible(p,m,n),('infeasible generated point',m,n,p))
        mx=0
        achieved=set()
        for ix,p in enumerate(pts):
            for q in pts[ix+1:]:
                v=sqdist(p,q)
                check(v<=d,('diameter bound',m,n,p,q,v))
                if v>mx:mx=v
                if v==d:achieved.add((p,q))
        check(mx==d,('attained',m,n))
        expected=expected_pairs(m,n)
        check(achieved==expected,('extremal pair classification',m,n,achieved^expected))
        check(len(achieved)==comb(n,2)*2**(n-2),('pair count',m,n))

# Independent direct enumeration from the original order-ideal inequalities,
# without reliance on the Minkowski-generator representation.
for m in range(1,3):
    for n in range(2,4):
        lattice=[]
        for x in product((0,1),repeat=m):
            for y in product(range(m+2),repeat=n):
                v=x+y
                if feasible(v,m,n):lattice.append(v)
        optimum=2*(m+1)**2+n-2
        pairset=pairs_at_max(sorted(lattice),optimum)
        check(pairset==expected_pairs(m,n),('direct lattice enumeration',m,n))

print('EXACT_CHECKS_OK',CHECKS)
print('PARAMETER_RANGE: m=1..4, n=2..5; direct original-inequality lattice checks m=1..2, n=2..3')
print('NOTE: finite checks do not substitute for the proof of all m>=1,n>=2')
