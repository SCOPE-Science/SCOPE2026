"""Exact finite checks for the metric-extremal theorem of Marion central polytopes.

Requires only Python 3 standard library. Finite checks supplement the analytic proof.
"""
from fractions import Fraction as F
from math import comb
from itertools import combinations

checks = 0

def check(condition, msg):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(msg)

def vertex(N, mask):
    s = mask.bit_count()
    assert 0 < s < N
    den = N + s
    return tuple(F(1 + ((mask >> i) & 1), den) for i in range(N))

def squared(a, b):
    return sum((x-y)**2 for x,y in zip(a,b))

def predicted_diameter_sq(N):
    if N % 2 == 0:
        return F(4, 9*N)
    m = (N-1)//2
    return F(9*N*m*(m+1), (N+m)**2*(N+m+1)**2)

def radius_sq(N, s):
    return F(s*(N-s),N*(N+s)**2)

def predicted_outer_s(N):
    return (N+1)//3  # test against explicit mod-3 rule

def class_distance_sq(N,s,t,r):
    return (radius_sq(N,s)+radius_sq(N,t)
            - F(2*(N*r-s*t),N*(N+s)*(N+t)))

# Enumerate actual vertices and all ordered-pair distances; track equality sets.
for N in range(3,11):
    masks = list(range(1,(1<<N)-1))
    vectors = {mask:vertex(N,mask) for mask in masks}
    target = predicted_diameter_sq(N)
    contact = 0
    for m in masks:
        v = vectors[m]
        check(sum(v)==1 and min(v)>0, ('coordinate sum',N,m))
        check(max(v)==2*min(v),('ratio',N,m))
        for j in range(N):
            for i in range(N):
                check(v[i]<=2*v[j],('facet',N,m,i,j))
    for i, a in enumerate(masks):
        for b in masks[i+1:]:
            d = squared(vectors[a],vectors[b])
            check(d<=target,('diameter exceeded',N,a,b,d,target))
            qualifies = (a ^ b == (1<<N)-1 and
                         abs(a.bit_count()-b.bit_count()) <= 1)
            check((d==target)==qualifies,('diametral class',N,a,b,d,target))
            contact += (d==target)
    predicted_count = (comb(N,N//2)//2 if N%2==0 else comb(N,N//2))
    check(contact==predicted_count,('diametral multiplicity',N,contact,predicted_count))
    centroid = tuple(F(1,N) for _ in range(N))
    outer_s = predicted_outer_s(N)
    outer = radius_sq(N,outer_s)
    for a in masks:
        d = squared(vectors[a],centroid)
        check(d==radius_sq(N,a.bit_count()),('radial formula',N,a))
        check((d==outer)==(a.bit_count()==outer_s),('outer contacts',N,a))
    check(sum(s.bit_count()==outer_s for s in masks)==comb(N,outer_s),('outer count',N))

# Independently check the class formula, covering all feasible intersections.
for N in range(3,45):
    mx = F(-1)
    choices = []
    for s in range(1,N):
        for t in range(1,N):
            for r in range(max(0,s+t-N), min(s,t)+1):
                d = class_distance_sq(N,s,t,r)
                check(d<=predicted_diameter_sq(N),('class bound',N,s,t,r,d))
                if d>mx:
                    mx=d;choices=[(s,t,r)]
                elif d==mx:
                    choices.append((s,t,r))
    check(mx==predicted_diameter_sq(N),('class max',N))
    required={(N//2,(N+1)//2,0),((N+1)//2,N//2,0)}
    check(set(choices)==required,('class uniqueness',N,choices,required))
    dmax=max(radius_sq(N,s) for s in range(1,N))
    check(dmax==radius_sq(N,predicted_outer_s(N)),('outer s',N))
    check(sum(radius_sq(N,s)==dmax for s in range(1,N))==1,('outer layer uniqueness',N))
print('PASS exact assertions:',checks)
print('Brute vertex-pair dimensions: N=3,...,10; class-size/intersection dimensions: N=3,...,44')
