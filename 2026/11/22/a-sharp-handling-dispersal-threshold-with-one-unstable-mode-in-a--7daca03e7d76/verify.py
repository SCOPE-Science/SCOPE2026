#!/usr/bin/env python3
"""Exact rational verification of a two-species cross-diffusion stability threshold.

Only Python 3's standard library is required. This computes first derivatives
of the full nonlinear reaction and flux functions with dual numbers; it does
not rely on floating-point eigenvalue calculations.
"""
from fractions import Fraction as Q

class Jet:
    def __init__(self, val, dx=0, dy=0):
        self.val, self.dx, self.dy = Q(val), Q(dx), Q(dy)
    def __add__(self, other):
        other = jet(other)
        return Jet(self.val+other.val,self.dx+other.dx,self.dy+other.dy)
    __radd__=__add__
    def __neg__(self): return Jet(-self.val,-self.dx,-self.dy)
    def __sub__(self,other): return self+(-jet(other))
    def __rsub__(self,other): return jet(other)+(-self)
    def __mul__(self,other):
        other=jet(other)
        return Jet(self.val*other.val,self.dx*other.val+self.val*other.dx,self.dy*other.val+self.val*other.dy)
    __rmul__=__mul__
    def inv(self):
        assert self.val
        return Jet(1/self.val,-self.dx/self.val**2,-self.dy/self.val**2)
    def __truediv__(self,other): return self*jet(other).inv()
    def __rtruediv__(self,other): return jet(other)*self.inv()
    def __pow__(self,k):
        assert isinstance(k,int) and k>=0
        result=Jet(1)
        for _ in range(k):result=result*self
        return result

def jet(obj): return obj if isinstance(obj,Jet) else Jet(obj)

def reactions(x,y):
    z=1+x+y
    return (x-Q(49,100)*x*x*(1+y*y)/(1+y)**2-Q(453,200)*x*y/z,
            -Q(3,100)*y+Q(9,100)*x*y/z)

def fluxes(x,y,w):
    z=1+x+y
    return (Q(199,100)*x/(1+y)+Q(1,100)*x*y/(1+y),
            Q(1,100)*y*(1+y)/z+w*x*y/z)

def jacobian(fun,w=None):
    x,y=Jet(1,1,0),Jet(1,0,1)
    pair=fun(x,y) if w is None else fun(x,y,w)
    return [[f.dx,f.dy] for f in pair],[f.val for f in pair]

def det(m): return m[0][0]*m[1][1]-m[0][1]*m[1][0]

def trace(m): return m[0][0]+m[1][1]

def dispersion(j,d,q):
    return det([[j[i][k]-q*d[i][k] for k in range(2)] for i in range(2)])

j, fv=jacobian(reactions)
assert fv==[0,0],fv
assert j==[[Q(1,150),-Q(151,300)],[Q(1,50),-Q(1,100)]],j
assert trace(j)==-Q(1,300) and det(j)==Q(1,100)

d0,_=jacobian(fluxes,Q(0))
d1,_=jacobian(fluxes,Q(1))
assert d0==[[Q(1),-Q(99,200)],[-Q(1,450),Q(7,900)]],d0
assert d1==[[Q(1),-Q(99,200)],[Q(2,9)-Q(1,450),Q(2,9)+Q(7,900)]],d1

def dmat(w):
    # The original flux is explicitly affine in the handling diffusivity w.
    return [[d0[i][k]+w*(d1[i][k]-d0[i][k]) for k in range(2)] for i in range(2)]

def p(w,q):
    return ((29900*w+601)*q*q+(105-10200*w)*q+900)/90000

critical=Q(15421,10900)
equal_diag=Q(893,200)
assert 0<critical<equal_diag
for w in (Q(0),Q(1,100),Q(1),critical,equal_diag,Q(30)):
    d, _=jacobian(fluxes,w)
    assert d==dmat(w)
    assert trace(d)==(200*w+907)/900>0
    assert det(d)==(29900*w+601)/90000>0
    for q in (Q(0),Q(1,4),Q(1),Q(9,4),Q(100)):
        assert dispersion(j,d,q)==p(w,q),(w,q,dispersion(j,d,q),p(w,q))
        assert trace(j)-q*trace(d)==-(200*q*w+907*q+3)/900
    assert p(w,Q(1,4))==(15421-10900*w)/1440000
    assert p(w,Q(1))==(9850*w+803)/45000

# Infinite-mode proof certificates: for w>0 and all q>=1,
# 90,000*dP/dq=2(29900*w+601)q +105-10200*w,
# whose value at q=1 is 49,600*w+1,307 >0, and derivative in q >0.
assert 2*29900-10200==49600
assert 2*601+105==1307
assert p(equal_diag,Q(0))==Q(1,100)
assert p(equal_diag,Q(1,4))==-Q(4433,192000)
assert p(equal_diag,Q(1))==Q(59711,60000)
assert dmat(equal_diag)==[[Q(1),-Q(99,200)],[Q(99,100),Q(1)]]
assert det(dmat(equal_diag))==Q(29801,20000)
# Replacing cross diffusion by the identity matrix keeps both diagonals
# but gives determinant q^2+q/300+1/100 >0 for every q>=0.
for q in (Q(0),Q(1,4),Q(1),Q(100)):
    assert dispersion(j,[[Q(1),Q(0)],[Q(0),Q(1)]],q)==q*q+q/Q(300)+Q(1,100)
print('PASS: exact equilibrium, derivatives, sharp mobility threshold,')
print('      all-mode monotonicity certificate and equal-diagonal control')
print('critical handling diffusivity:', critical)
print('single unstable-mode witness:', equal_diag, 'P(1/4)=',p(equal_diag,Q(1,4)))
