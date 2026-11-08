#!/usr/bin/env python3
"""Exact pair-line incidence certificate for the rational BKS octic over GF(343)."""
from collections import Counter
from math import isqrt

P, Q = 7, 343
# F_343=F_7[t]/(t^3+2), basis 1,t,t^2.
def coords(x):
    return x % P, (x // P) % P, x // (P*P)

def field():
    mul = [[0]*Q for _ in range(Q)]
    for x in range(Q):
        a,b,c = coords(x)
        for y in range(Q):
            d,e,f = coords(y)
            z0 = (a*d+5*(b*f+c*e)) % P
            z1 = (a*e+b*d+5*c*f) % P
            z2 = (a*f+b*e+c*d) % P
            mul[x][y] = z0+P*z1+P*P*z2
    add = [[sum((u+v)%P * P**i for i,(u,v) in enumerate(zip(coords(x),coords(y))))
            for y in range(Q)] for x in range(Q)]
    neg = [sum(((-u)%P)*P**i for i,u in enumerate(coords(x))) for x in range(Q)]
    inv = [0]*Q
    for x in range(1,Q):
        inv[x] = next(y for y in range(1,Q) if mul[x][y]==1)
    return mul,add,neg,inv

m,a,n,inv = field()
def A(x,y): return a[x][y]
def N(x): return n[x]
def S(x,y): return A(x,N(y))
def M(x,y): return m[x][y]
def powf(x,e):
    z=1
    while e:
        if e&1: z=M(z,x)
        x=M(x,x)
        e>>=1
    return z

def norm(p):
    v = next(x for x in p if x)
    iv=inv[v]
    return tuple(M(x,iv) for x in p)

def cross(p,q):
    x,y,z=p;u,v,w=q
    return norm((S(M(y,w),M(z,v)),S(M(z,u),M(x,w)),S(M(x,v),M(y,u))))

points=set()
for t in range(Q):
    x=M(2,powf(A(t,1),8))
    y=A(2,A(t,powf(t,7)))
    points.add((x,y,1))
points.add((1,0,0))
# The 21 F_7-rational nodes are the internal affine points of Y^2-2X=0.
for x in range(7):
    for y in range(7):
        if (y*y-2*x)%7 in {3,5,6}:
            points.add((x,y,1))
points=sorted(points)
assert len(points)==365

paircounts=Counter()
for i,p in enumerate(points):
    for q in points[i+1:]:
        paircounts[cross(p,q)]+=1
counts=Counter()
for value in paircounts.values():
    k=(1+isqrt(1+8*value))//2
    assert k*(k-1)//2==value
    counts[k]+=1
assert len(paircounts)==49945
Qlines=Q*Q+Q+1
counts[1]=len(points)*(Q+1)-sum(k*v for k,v in counts.items())
counts[0]=Qlines-sum(counts.values())
expected={0:48048,1:20000,2:46032,3:3528,4:21,5:28,8:336}
assert dict(counts)==expected, (counts,expected)
longlines=[line for line,value in paircounts.items() if value==28]
assert len(longlines)==336

cover=Counter()
for x,y,z in longlines:
    if y:
        for u in range(Q):
            v=M(inv[y],N(A(M(x,u),z)))
            cover[(u,v,1)]+=1
        cover[norm((y,N(x),0))]+=1
    elif x:
        u=M(inv[x],N(z))
        for v in range(Q): cover[(u,v,1)]+=1
        cover[(0,1,0)]+=1
    else:
        for v in range(Q):cover[(1,v,0)]+=1
        cover[(0,1,0)]+=1
hist=Counter(cover.values())
hist[0]=Qlines-len(cover)
assert dict(hist)=={0:51633,1:19152,2:46872,8:336},hist
on_curve=Counter(cover[p] for p in points)
assert dict(on_curve)=={0:29,8:336}, on_curve
ground={pt for pt in points if all(v<P for v in pt)}
assert len(ground)==29 and all(cover[pt]==0 for pt in ground)
assert sum(k*v for k,v in counts.items())==365*344
assert sum(k*(k-1)//2*v for k,v in counts.items())==365*364//2
assert sum(k*v for k,v in hist.items())==336*344
assert sum(k*(k-1)//2*v for k,v in hist.items())==336*335//2
print('GF(343), irreducible u^3+2')
print('curve points',len(points),'lines with >=2',len(paircounts))
print('line spectrum',sorted(counts.items()))
print('maximal secant point incidence',sorted(hist.items()))
print('curve point incidence',sorted(on_curve.items()))
print('uncovered exterior points',hist[0]-on_curve[0])
print('PAIRLINE_VERIFY_OK')
