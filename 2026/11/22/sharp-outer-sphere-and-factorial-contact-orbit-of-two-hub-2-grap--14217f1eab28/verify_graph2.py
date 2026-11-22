#!/usr/bin/env python3
"""Exact certificate and finite cross-checks for two-hub 2-graph polytopes."""
from fractions import Fraction as F
from itertools import permutations
from math import factorial

class Poly:
    def __init__(self, d=None):
        self.d = {k: int(v) for k, v in (d or {}).items() if v}
    @staticmethod
    def c(n): return Poly({(0,0,0):n})
    @staticmethod
    def v(i): return Poly({tuple(int(j==i) for j in range(3)):1})
    def __add__(self, other):
        other = other if isinstance(other,Poly) else Poly.c(other)
        d = self.d.copy()
        for e,c in other.d.items(): d[e] = d.get(e,0) + c
        return Poly(d)
    __radd__ = __add__
    def __neg__(self): return Poly({e:-c for e,c in self.d.items()})
    def __sub__(self,other): return self + (-other if isinstance(other,Poly) else -Poly.c(other))
    def __rsub__(self,other): return other + (-self)
    def __mul__(self,other):
        other = other if isinstance(other,Poly) else Poly.c(other)
        d={}
        for a,x in self.d.items():
            for b,y in other.d.items():
                e=tuple(a[i]+b[i] for i in range(3))
                d[e]=d.get(e,0)+x*y
        return Poly(d)
    __rmul__=__mul__
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        a=Poly.c(1)
        for _ in range(n):a=a*self
        return a
    def __eq__(self,other):
        return self.d==(other.d if isinstance(other,Poly) else Poly.c(other).d)

u,v,w=[Poly.v(i) for i in range(3)]
q=u+v+w; s=u; k=u+v
N=(q+2)*(-3*k**4-6*k**3+15*k**2+42*k-3*s**4-2*s**3+3*s**2+2*s)+(q-2)*(3*q**2+10*q+11)*(k*k+3*k+s*s+s)
P0=2*u*w*(6*u**3+9*u*u*w+22*u*u+3*u*w*w+22*u*w+16*u+6*w*w+8*w+4)
P1=(6*u**4+42*u**3*w+19*u**3+36*u*u*w*w+113*u*u*w+20*u*u+6*u*w**3+71*u*w*w+68*u*w+39*u+9*w**3+12*w*w+15*w+18)
P2=(9*u**3+45*u*u*w+19*u*u+27*u*w*w+96*u*w+22*u+3*w**3+31*w*w+30*w+23)
P3=(3*u*u+24*u*w+7*u+9*w*w+29*w+6)
P4=6*w+1
# Independent integer-polynomial derivation from consecutive square sums.
F2=lambda t:t*(t-1)*(2*t-1)
A2=2+s*(s+1); B2=2+k*(k+3)
V12_ind=(3*A2*A2+3*B2*B2+12*s
         +2*(F2(k)-F2(s))+24*(k*(k-1)-s*(s-1))+48*(k-s)
         +8*(F2(q)-F2(k))+96*(q*(q-1)-k*(k-1))+192*(q-k))
V12_formula=(3*k**4+6*k**3-15*k*k-42*k+3*s**4+2*s**3-3*s*s-2*s
             +16*q**3+72*q*q+104*q+24)
assert V12_ind == V12_formula
V12_endpoint0=16*q**3+72*q*q+104*q+24
N_ind=(q+2)*(V12_endpoint0-V12_ind)+(q-2)*(3*q*q+10*q+11)*(s*(s+1)+k*(k+3))
assert N_ind==N
assert N == P0 + v*P1 + v*v*P2 + v**3*P3 + v**4*P4
assert len(N.d)==41 and all(c>0 for c in N.d.values())
assert all((e[1]>0 or (e[0]>0 and e[2]>0)) for e in N.d)
print('POSITIVE_POLYNOMIAL_CERTIFICATE_PASS monomials=41')


def center(q):
    t=(q+1)*(q+2)
    x=F((q*q+3*q+8)*(3*q*q+7*q+6),12*(q+2)**2)
    y=F(t-2*x,q)
    return x,y

def radius_squared(q):
    x,y=center(q)
    a=2*(x-1)**2+sum(((4+2*j)-y)**2 for j in range(q))
    b=F(q*(q+1)*(9*q**5+111*q**4+523*q**3+1145*q*q+1256*q+484),72*(q+2)**3)
    assert a==b
    return a


def brute_vertices(q):
    n=q+2
    tubes=[(i,) for i in range(n)]
    tubes += [(h,i) for h in range(2) for i in range(2,n)]
    tubes += [(h,i,j) for h in range(2) for i in range(2,n) for j in range(i+1,n)]
    tubes += [(0,1,i) for i in range(2,n)]
    result=set()
    for order in permutations(range(n)):
        pos=[0]*n
        for j,t in enumerate(order):pos[t]=j
        coords=[0]*n
        for tube in tubes: coords[max(tube,key=lambda t:pos[t])]+=1
        result.add(tuple(coords))
    return result

for q0 in range(2,7):
    verts=brute_vertices(q0)
    x,y=center(q0)
    r2=radius_squared(q0)
    touch=0
    for p in verts:
        rr=(p[0]-x)**2+(p[1]-x)**2+sum((z-y)**2 for z in p[2:])
        assert rr<=r2, (q0,p,rr,r2)
        touch+=(rr==r2)
    count=factorial(q0)*(2*sum(F(q0-s+1,factorial(s)) for s in range(q0+1))-1)
    assert len(verts)==count and touch==factorial(q0)+2,(q0,len(verts),count,touch)
    print('EXHAUSTIVE_PASS q=%d vertices=%d contacts=%d R2=%s'%(q0,len(verts),touch,r2))
print('TWO_HUB_2_GRAPH_SPHERE_PASS')
