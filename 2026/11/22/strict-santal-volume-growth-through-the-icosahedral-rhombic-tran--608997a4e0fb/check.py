"""Exact rational interval checks for the polar-volume derivative inequalities.
Optional convex-hull tests are numerical corroboration, not the theorem's proof.
"""
from fractions import Fraction as F
from math import isqrt, sqrt, sin, pi

N=10**18
class I:
    def __init__(self, lo, hi=None):
        self.lo=F(lo); self.hi=F(hi if hi is not None else lo)
        assert self.lo<=self.hi
    def __add__(self,o):
        o=i(o);return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,o):return self+-i(o)
    def __rsub__(self,o):return i(o)+-self
    def __mul__(self,o):
        o=i(o);p=[x*y for x in (self.lo,self.hi) for y in (o.lo,o.hi)]
        return I(min(p),max(p))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=i(o);assert o.lo*o.hi>0
        return self*I(1/o.hi,1/o.lo)
    def __rtruediv__(self,o):return i(o)/self
    def __pow__(self,n):
        assert n>=0
        z=I(1)
        for j in range(n):z=z*self
        return z
    def sqrt(self):
        assert self.lo>=0
        def floorroot(x):return isqrt((x.numerator*N*N)//x.denominator)
        return I(F(floorroot(self.lo),N),F(floorroot(self.hi)+1,N))
    def within(self,a,b):return self.lo>F(a) and self.hi<F(b)
    def above(self,b=0):return self.lo>F(b)
    def below(self,b=0):return self.hi<F(b)
    def show(self):return '%.15f..%.15f'%(float(self.lo),float(self.hi))
def i(x):return x if isinstance(x,I) else I(x)
r=I(5).sqrt(); g=I(3).sqrt()
a=((5+2*r)/15).sqrt(); c=r/3; q=(5+r)/15
L=(2-2/r).sqrt(); s=((10+2*r)/16).sqrt()
Vd=10*a*(1-a*a)*s
u0=2*a/(1+c)
assert a.within(F(79465,100000),F(79466,100000))
assert u0.within(F(91059,100000),F(91060,100000))
assert (Vd-5*g*(2+c)/9).above(0) # Lower-branch derivative strictly positive.
p2=20*a*a*s/q
p1=-40*a*s/q +5*g/(3*q*q)*(L*L*(1+c)**2-8*L*a*(1+c)/g+4*a*a/3)
pm=5*g/(3*q*q)*(4*a*a*L*L-16*a*L/g+F(4,3))
assert p2.within(F(24898,1000),F(24900,1000))
assert p1.within(F(-94001,1000),F(-93998,1000))
assert pm.within(F(-44567,1000),F(-44562,1000))
assert (2*p2+p1-pm).above(0) # derivative at right endpoint
assert (p2+pm).below(0) # second derivative negative throughout t<=1
print('exact rational certificates: PASS')
print('a:',a.show(),'switch:',u0.show(),'Vd:',Vd.show())
print('p2:',p2.show(),'p1:',p1.show(),'p(-1):',pm.show())
print('E-prime(1):',(2*p2+p1-pm).show())

# Independent direct convex hull and halfspace polar volume checks.
# This numerical part is optional in a minimal Python installation.
try:
    import numpy as np
    from itertools import product
    from scipy.spatial import ConvexHull, HalfspaceIntersection
except ImportError:
    print('SciPy unavailable: optional finite hull checks skipped')
else:
    phi=(1+sqrt(5))/2
    V=np.array([(0,x,y*phi) for x,y in product((-1,1),repeat=2)] +
               [(x,y*phi,0) for x,y in product((-1,1),repeat=2)] +
               [(y*phi,0,x) for x,y in product((-1,1),repeat=2)],dtype=float)
    V=V/np.linalg.norm(V[0])
    Ico=ConvexHull(V)
    U=Ico.equations[:,:3]
    af=float((5+2*sqrt(5))/15)**0.5
    cf=sqrt(5)/3; qf=(5+sqrt(5))/15
    Lf=sqrt(2-2/sqrt(5));sf=sin(2*pi/5)
    dvol=10*af*(1-af*af)*sf
    tf=2*af/(1+cf)
    def formulas(t):
        if t<=tf:
            primal=dvol*2*t/(1+cf)
            polar=dvol/af**3-5*sqrt(3)*(1+cf)/(af**3*(1-cf))*(1-af/t)**3
        else:
            primal=dvol*t*t/af
            mu=(1/t-af)/qf; lam=1-2*af*mu
            pent=5*qf*mu*mu*sf
            hexarea=sqrt(3)/4*((lam*Lf)**2+4*(lam*Lf)*(mu*2/sqrt(3))+(mu*2/sqrt(3))**2)
            polar=4*pent+20/(3*t)*hexarea
        return primal,polar
    for t in [af,.82,.85,.89,tf-.00001,tf+.00001,.93,.95,.97,1.0]:
        K=ConvexHull(np.vstack((V,t*U)))
        hs=np.vstack((np.column_stack((V,-np.ones(12))),np.column_stack((t*U,-np.ones(20)))))
        vertices=HalfspaceIntersection(hs,np.zeros(3)).intersections
        pol=ConvexHull(vertices)
        A,B=formulas(t)
        assert abs(K.volume-A)<1e-9,(t,K.volume,A)
        assert abs(pol.volume-B)<1e-9,(t,pol.volume,B)
    print('10 direct primal/polar hull comparisons: PASS')
