#!/usr/bin/env python3
"""Exact fifth-period census and real Floquet isolation for a quadratic map.
Requires SymPy (tested with 1.13+). All root counts and bounds use exact rationals.
"""
from fractions import Fraction as Q
import sympy as s

x,y=s.symbols('x y'); A,B=x,y
for _ in range(5):
    A,B=B,s.expand(A*A-B*B)
G=s.groebner([A-x,B-y],x,y,order='lex',domain=s.QQ)
assert len(G.polys)==2
p=s.Poly(G.polys[0],x,y);h=s.Poly(G.polys[1],x,y)
assert s.degree(p.as_expr(),x)==1 and not s.degree(h.as_expr(),x)>0
assert p.coeff_monomial(x)!=0
# Univariate eliminant of the complete fixed-point scheme.
q15=1215*y**15-8640*y**13+2520*y**12+19890*y**11-9844*y**10-16290*y**9+8314*y**8+5303*y**7+1552*y**6-2010*y**5-4202*y**4+2060*y**3+1108*y**2-340*y-169
assert s.expand(h.as_expr()-y*q15/1215)==0
assert s.gcd(s.Poly(y*q15,y),s.diff(y*q15,y)).degree()==0
assert s.Poly(q15,y).count_roots(-s.oo,s.oo)==5
assert s.Poly(y*q15,y).count_roots(-s.oo,s.oo)==6
# Explicit sign-isolating rational intervals. Five nonzero real roots, no others.
roots=[(-2033905,-2033904),(-1646315,-1646314),(675684,675685),(1426417,1426418),(1578117,1578118)]
for l,r in roots:
    assert s.Poly(q15,y).count_roots(s.Rational(l,1000000),s.Rational(r,1000000))==1
# Choose the root in (0.675684, 0.675685); tighten with certified Sturm isolation.
iso=[I for I,m in s.intervals(q15,eps=s.Rational(1,10**18)) if s.Rational(675684,10**6)<I[0]<s.Rational(675685,10**6)]
assert len(iso)==1

def frac(z):
    n,d=s.fraction(z)
    return Q(int(n),int(d))

class IV:
    __slots__=('lo','hi')
    def __init__(self,lo,hi=None):
        if isinstance(lo, IV): self.lo,self.hi=lo.lo,lo.hi;return
        self.lo=Q(lo);self.hi=Q(lo if hi is None else hi)
        assert self.lo<=self.hi
    def __add__(self,v):
        v=IV(v);return IV(self.lo+v.lo,self.hi+v.hi)
    __radd__=__add__
    def __neg__(self):return IV(-self.hi,-self.lo)
    def __sub__(self,v):return self+-IV(v)
    def __rsub__(self,v):return IV(v)+-self
    def __mul__(self,v):
        v=IV(v);a=[self.lo*v.lo,self.lo*v.hi,self.hi*v.lo,self.hi*v.hi]
        return IV(min(a),max(a))
    __rmul__=__mul__
    def sq(self):
        if self.lo>=0:return IV(self.lo*self.lo,self.hi*self.hi)
        if self.hi<=0:return IV(self.hi*self.hi,self.lo*self.lo)
        return IV(0,max(self.lo*self.lo,self.hi*self.hi))
    def within(self,a,b):return Q(a)<self.lo<=self.hi<Q(b)

# Exact rational polynomial of y defining x at every fifth fixed point.
xpoly=s.Poly(-p.as_expr().subs(x,0)/p.coeff_monomial(x),y,domain=s.QQ)
Y=IV(frac(iso[0][0]),frac(iso[0][1]))
X=IV(0)
for c in xpoly.all_coeffs():X=X*Y+IV(frac(c))
assert X.within(s.Rational(1426,1000),s.Rational(1427,1000))

M=[[IV(int(i==j)) for j in range(2)] for i in range(2)]
xx,yy=X,Y
for _ in range(5):
    J=[[IV(0),IV(1)],[2*xx,-2*yy]]
    M=[[sum((J[i][k]*M[k][j] for k in range(2)),IV(0)) for j in range(2)] for i in range(2)]
    xx,yy=yy,xx.sq()-yy.sq()
assert (xx-X).lo<=0<=(xx-X).hi and (yy-Y).lo<=0<=(yy-Y).hi
trace=M[0][0]+M[1][1]
det=M[0][0]*M[1][1]-M[0][1]*M[1][0]
assert trace.within(-230,-220), (str(float(trace.lo)),str(float(trace.hi)))
assert det.within(-170,-150),(str(float(det.lo)),str(float(det.hi)))
assert (IV(1)-trace+det).lo>0
assert (IV(1)+trace+det).hi<0
# Negative determinant implies opposite-sign eigenvalues. The positive one is in (0,1)
# because chi(0)<0<chi(1), and the negative one is <-1 because chi(-1)<0.
print('FIFTH_PERIOD_UNIQUE_REAL_SADDLE_EXACT_OK')
print('roots_real_nonzero',5,'roots_complex_nonzero',10,'period_five_cycles_complex',3)
print('trace enclosure:',float(trace.lo),float(trace.hi))
print('det enclosure:',float(det.lo),float(det.hi))
