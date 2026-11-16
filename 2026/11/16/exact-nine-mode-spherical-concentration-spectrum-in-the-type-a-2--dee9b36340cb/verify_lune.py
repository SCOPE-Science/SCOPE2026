"""Exact quadratic-band spherical-lune concentration certificate.

Recompute symmetry blocks by elementary beta/trigonometric integration and
certify all nine eigenvalue intervals with rational Machin bounds on pi.
Requires SymPy; no external data.
"""
from fractions import Fraction as F
import sympy as sp

P=sp.pi; S=sp.sqrt(3); T=sp.sqrt(5)
# Orthonormal real sphere functions in z=cos(theta), phi centered on the lune.
z=sp.Symbol('z',real=True)
basis=[(sp.Integer(1),0,0,'c'),(T*(3*z*z-1)/2,0,0,'c'),
       (S,1,1,'c'),(S*T/2,2,2,'c'),
       (S,1,1,'s'),(S*T/2,2,2,'s'),
       (S*z,0,0,'c'),(S*T*z,1,1,'c'),(S*T*z,1,1,'s')]

def radial(a,b):
    ex=sp.Poly(sp.expand(a[0]*b[0]),z)
    q=a[1]+b[1]
    out=sp.Integer(0)
    for (k,),coef in ex.terms():
        if k%2==0:
            aa=sp.Rational(k+1,2); bb=sp.Rational(q+2,2)
            out+=coef*sp.gamma(aa)*sp.gamma(bb)/sp.gamma(aa+bb)
    return sp.simplify(sp.expand_func(out))

def ang(a,b):
    m=a[2]; n=b[2]; kind=a[3]
    if kind!=b[3]: return sp.Integer(0)
    if kind=='s' and (m==0 or n==0):return sp.Integer(0)
    def sinc(k): return P/3 if k==0 else sp.simplify(2*sp.sin(P*k/6)/k)
    return sp.simplify((sinc(m-n)+(1 if kind=='c' else -1)*sinc(m+n))/2)

def mat(ids):
    return sp.Matrix([[sp.simplify(radial(basis[i],basis[j])*ang(basis[i],basis[j])/(4*P))
                       for j in ids] for i in ids])

A=mat([0,1,2,3]); B=mat([4,5]); C=mat([6,7]); D=mat([8]);
A0=sp.Matrix([[sp.Rational(1,6),0,S/8,T/(4*P)],
              [0,sp.Rational(1,6),-S*T/64,-1/(4*P)],
              [S/8,-S*T/64,sp.Rational(1,6)+S/(4*P),15*T/128],
              [T/(4*P),-1/(4*P),15*T/128,sp.Rational(1,6)+S/(8*P)]])
B0=sp.Matrix([[sp.Rational(1,6)-S/(4*P),3*T/128],
              [3*T/128,sp.Rational(1,6)-S/(8*P)]])
C0=sp.Matrix([[sp.Rational(1,6),3*T/32],
              [3*T/32,sp.Rational(1,6)+S/(4*P)]])
D0=sp.Matrix([[sp.Rational(1,6)-S/(4*P)]])
for actual,expected in [(A,A0),(B,B0),(C,C0),(D,D0)]:
    assert all(sp.simplify(u-v)==0 for u,v in zip(actual,expected))
assert sp.simplify(sp.trace(A)+sp.trace(B)+sp.trace(C)+sp.trace(D)-sp.Rational(3,2))==0

# Scalar polynomial numerators; denominator is strictly positive.
def h4(l,p,s):
    return (5308416*p**3*l**4-3538944*p**3*l**3-1990656*s*p**2*l**3-
            1492992*p*l**2+251964*p**3*l**2+995328*s*p**2*l**2-
            351054*s*p**2*l+497664*s*l+497664*p*l+112620*p**3*l-
            13481*p**3-82944*s-39285*p+40077*s*p**2)
def h2b(l,p,s):
    return (147456*p**2*l**2-49152*p**2*l+55296*s*p*l-
            9216*s*p+13824+3691*p**2)
def h2c(l,p,s):
    return 9216*p*l**2-3072*p*l-2304*s*l-149*p+384*s

def sign_approx_exact_poly(mat,func,den):
    l=sp.Symbol('lambda')
    lhs=sp.factor(mat.charpoly(l).as_expr())
    rhs=func(l,P,S)/den
    assert sp.simplify(lhs-rhs)==0
sign_approx_exact_poly(A,h4,5308416*P**3)
sign_approx_exact_poly(B,h2b,147456*P**2)
sign_approx_exact_poly(C,h2c,9216*P)

class I:
    def __init__(self,a,b=None):self.a=F(a);self.b=F(a if b is None else b)
    def __add__(self,v):
        v=v if isinstance(v,I) else I(v)
        return I(self.a+v.a,self.b+v.b)
    __radd__=__add__
    def __neg__(self):return I(-self.b,-self.a)
    def __sub__(self,v):return self+-v if isinstance(v,I) else self+I(-v)
    def __rsub__(self,v):return I(v)+-self
    def __mul__(self,v):
        v=v if isinstance(v,I) else I(v)
        candidates=[a*b for a in (self.a,self.b) for b in (v.a,v.b)]
        return I(min(candidates),max(candidates))
    __rmul__=__mul__
    def __pow__(self,k):
        assert isinstance(k,int) and k>=0
        q=I(1)
        for _ in range(k):q=q*self
        return q
    def sign(self):
        assert self.a>0 or self.b<0, ('ambiguous',float(self.a),float(self.b))
        return 1 if self.a>0 else -1

# Exact alternating-series error for arctan of a positive reciprocal.
def arctan_encl(q,n=20):
    val=sum((F(-1 if j%2 else 1,(2*j+1)*q**(2*j+1)) for j in range(n)),F(0))
    err=F(1,(2*n+1)*q**(2*n+1))
    return I(val-err,val+err)
a=arctan_encl(5);b=arctan_encl(239)
pi=16*a-4*b
assert pi.a>3 and pi.b<4
rt3=I(F(1732050807568877,10**15),F(1732050807568878,10**15))
assert rt3.a**2<3<rt3.b**2
# Decimal brackets are rational and disjoint, in spectral ascending order.
scale=10**9
brackets=[('A',341000-200,341000+200,h4),('B',571400-200,571400+200,h2b),
          ('A',3940400-200,3940400+200,h4),('C',14914000-300,14914000+300,h2c),
          ('D',28834400-300,28834400+300,None),('B',126013600-300,126013600+300,h2b),
          ('A',169560800-300,169560800+300,h4),('C',456251600-300,456251600+300,h2c),
          ('A',699572800-300,699572800+300,h4)]
assert all(0<l<h<scale for _,l,h,_ in brackets)
assert all(brackets[j][2]<brackets[j+1][1] for j in range(8))
counts={'A':0,'B':0,'C':0,'D':0}
for name,lo,hi,f in brackets:
    if f is None:
        f=lambda l,p,s:12*p*l-2*p+3*s
    sig1=f(I(F(lo,scale)),pi,rt3).sign()
    sig2=f(I(F(hi,scale)),pi,rt3).sign()
    assert sig1!=sig2,(name,lo,hi)
    counts[name]+=1
assert counts=={'A':4,'B':2,'C':2,'D':1}

# A symmetric Gram matrix has exactly as many real eigenvalues as its size.
# The disjoint certified sign crossings therefore account for every eigenvalue.
# Both extreme eigenvalues are simple and in the even-even 4x4 sector.
print('PASS exact beta/trigonometric block entries and nine rational eigenvalue enclosures')
for name,lo,hi,f in brackets:
    print(name, '[',F(lo,scale),',',F(hi,scale),']', (lo+hi)/(2*scale))
import math
max_eig=0.6995727837708233; min_eig=0.0003409937351035911
print('numeric condition of restriction',math.sqrt(max_eig/min_eig))
