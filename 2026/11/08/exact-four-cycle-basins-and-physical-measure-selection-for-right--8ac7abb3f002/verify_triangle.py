"""Reproduce geometric/interval identities for an equilateral-leg right triangle.
Uses an independent perpendicular-projection construction and symbolic SymPy.
Finite trajectories are checks, not an exhaustive proof.
"""
from math import sqrt, hypot, isclose
from fractions import Fraction
from random import Random
import sympy as S

r=S.sqrt(2); s=r-1; k=r+1; d=s-s**2
intervals=[(s**2,s),(2*s**2-1,2*s-1),(4*s**2-3,4*s-3)]
assert S.simplify(d-(3*r-4))==0
assert S.simplify(sum(b-a for a,b in intervals)-7*d)==0
assert S.simplify(2*(1+r)*7*d-14*(2-r))==0
assert S.simplify(2*(1+r)*d/(2+r)-(6-4*r))==0
assert all(float(b)>float(a) for a,b in intervals)
assert float(intervals[2][0])>-float(k)
assert float(intervals[0][1])==float(s)

# Distinct projections onto the three complete support lines.
LINES = [((0.,0.),(1.,0.)), ((0.,0.),(0.,1.)), ((0.,1.),(1.,-1.))]
def belongs(pt,i,tol=1e-9):
    x,y=pt
    return (abs(y)<tol if i==0 else abs(x)<tol if i==1 else abs(x+y-1)<tol)
def proj(pt,i):
    (ax,ay),(vx,vy)=LINES[i]
    scale=((pt[0]-ax)*vx+(pt[1]-ay)*vy)/(vx*vx+vy*vy)
    return (ax+scale*vx,ay+scale*vy)
def F(pt):
    ix=[j for j in range(3) if belongs(pt,j)]
    assert ix, ('off support lines',pt)
    i=ix[0]
    available=[j for j in range(3) if j!=i]
    pp=[proj(pt,j) for j in available]
    dd=[(pt[0]-q[0])**2+(pt[1]-q[1])**2 for q in pp]
    if abs(dd[0]-dd[1]) <= 1.e-12:
        return pt
    return pp[0] if dd[0]>dd[1] else pp[1]

cycle=[(1/3,0.), (2/3,1/3), (0.,1/3), (1/3,2/3)]
for i in range(4):
    p=F(cycle[i]);q=cycle[(i+1)%4]
    assert hypot(p[0]-q[0],p[1]-q[1])<1.e-14
for t in (float(s),-float(k)):
    assert F((t,0.))==(t,0.)
    assert F((0.,t))==(0.,t)
assert F((0.5,0.5))==(0.5,0.5)
assert F((0.,0.))==(0.5,0.5)

lohi=[(float(a),float(b)) for a,b in intervals]
def in_basin_axis(t):
    return any(a<t<b for a,b in lohi)
def prediction(pt,i):
    if i<2:
        t=pt[i==1]
    else:
        u=pt[0]; t=min(u,1-u)
    return in_basin_axis(t)

def is_at_cycle(pt):
    return min(hypot(pt[0]-u,pt[1]-v) for u,v in cycle)<1.e-8
rng=Random(20261101)
checked=0
for line in range(3):
    for _ in range(2400):
        t=rng.uniform(-7,7)
        p=((t,0.) if line==0 else ((0.,t) if line==1 else (t,1-t)))
        if (line<2 and min(abs(t-c) for z in lohi for c in z)<1.e-5) or (line==2 and min(abs(min(t,1-t)-c) for z in lohi for c in z)<1.e-5):
            continue
        v=p
        for _ in range(120): v=F(v)
        if prediction(p,line):
            assert is_at_cycle(v),('cycle mismatch',line,t,v)
        else:
            assert hypot(v[0]-0.5,v[1]-0.5)<1.e-8,('midpoint mismatch',line,t,v)
        checked+=1
print('PASS: exact symbolic interval-length/perimeter identities; geometric period/fixed identities; independent direct trajectories:',checked)
