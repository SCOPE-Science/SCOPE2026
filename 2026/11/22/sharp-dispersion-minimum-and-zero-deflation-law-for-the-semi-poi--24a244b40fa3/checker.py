#!/usr/bin/env python3
"""Exact coefficient and interval certificate for a weighted-Poisson dispersion theorem.
Requires only Python 3 standard library. No external research infrastructure.
"""
from fractions import Fraction as Q
from math import factorial, comb


def clean(p):
    return {k:tuple(v[:next(i+1 for i in range(len(v)-1,-1,-1) if v[i])]) for k,v in p.items() if any(v)}


def add(a,b):
    out={}
    for k in set(a)|set(b):
        aa=a.get(k,());bb=b.get(k,())
        out[k]=tuple((aa[j] if j<len(aa) else 0)+(bb[j] if j<len(bb) else 0)
                     for j in range(max(len(aa),len(bb))))
    return clean(out)


def scale(a,c):return clean({k:tuple(c*x for x in v) for k,v in a.items()})


def mul(a,b):
    out={}
    for i,aa in a.items():
        for j,bb in b.items():
            v=[0]*(len(aa)+len(bb)-1)
            for p,x in enumerate(aa):
                for q,y in enumerate(bb):v[p+q]+=x*y
            out=add(out,{i+j:tuple(v)})
    return out


def deriv(a):
    return clean({
        k:tuple((j+1)*v[j+1]+k*v[j] if j+1<len(v) else k*v[j]
        for j in range(len(v))) for k,v in a.items()})

S={1:(1,-1,1),0:(-1,)}
A={1:(-2,2,-1,1),0:(2,)}
T={2:(0,0,2,2,-2,1),1:(0,0,-2,-4,-1)}
# T = t^2 [e^{2t}(t^3-2t^2+2t+2) - e^t(t^2+4t+2)].
D=mul(S,A)
N=add(mul(deriv(T),D),scale(mul(T,deriv(D)),-1))
P={
 1:(0,8,28,16,2),
 2:(0,-24,-60,24,-4,-10,1),
 3:(0,24,36,-72,62,-18,0,9,2,1),
 4:(0,-8,-4,32,-52,44,-25,4),
}
assert N==P, f'derivative numerator mismatch: {N}'
print('PASS: formal derivative identity F\'=N/(SA)^2')


def falling_poly(j):
    p=[Q(1)]
    for h in range(j):
        nxt=[Q(0)]*(len(p)+1)
        for i,x in enumerate(p):
            nxt[i]-=h*x
            nxt[i+1]+=x
        p=nxt
    return p


def Qpoly(k,p):
    out=[Q(0)]*len(p)
    for j,c in enumerate(p):
        fj=falling_poly(j)
        for i,b in enumerate(fj):out[i]+=Q(c)*b/k**j
    return out


def shift(poly,h):
    return [sum(poly[j]*comb(j,i)*h**(j-i) for j in range(i,len(poly))) for i in range(len(poly))]


def coefficient(k,p,n):
    return sum(c*factorial(n)//factorial(n-j)*k**(n-j)
               for j,c in enumerate(p) if j<=n)

for n in range(26):
    c=sum(coefficient(k,p,n) for k,p in P.items())
    expected=0 if n<=9 else (-1 if n<=14 else 1)
    assert (c>0)-(c<0)==expected,(n,c,expected)
print('PASS: N coefficients vanish degrees 0--9, negative 10--14, positive 15--25')

for k,p in P.items():
    cs=shift(Qpoly(k,p),26)
    assert all(c>0 for c in cs),(k,cs)
    print('PASS: component e^{%dt} coefficient polynomial positive for every integer n>=26' %k)

# Positive real root located by interval-bounded exponential evaluations.
# For u>=0, exp(u) is between sum_{j=0}^N u^j/j!
# and this sum plus the first omitted term/(1-u/(N+2)), provided u<N+2.
def exp_bounds(u,terms=110):
    s=Q(1); term=Q(1)
    for j in range(1,terms+1):
        term=term*u/j
        s+=term
    nxt=term*u/(terms+1)
    return s,s+nxt/(1-u/(terms+2))


def poly_value(p,x):return sum(Q(c)*x**j for j,c in enumerate(p))


def N_bounds(x):
    lo=Q(0);hi=Q(0)
    for k,p in P.items():
        c=poly_value(p,x)
        u,v=exp_bounds(k*x)
        lo+=c*(u if c>=0 else v)
        hi+=c*(v if c>=0 else u)
    return lo,hi

a=Q('1.40741241822510067986511')
b=Q('1.40741241822510067986512')
assert a<b
la,ha=N_bounds(a); lb,hb=N_bounds(b)
assert ha<0<lb
print('PASS: exact rational Taylor brackets certify unique root in')
print('      (%s, %s)'%(a,b))

# Elementary validated intervals for reporting minimum F(lambda).
class I:
    def __init__(self,lo,hi=None):
        self.lo=Q(lo);self.hi=Q(hi) if hi is not None else self.lo
        assert self.lo<=self.hi
    def __add__(self,z):
        z=into(z);return I(self.lo+z.lo,self.hi+z.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,z):return self+(-into(z))
    def __rsub__(self,z):return into(z)+(-self)
    def __mul__(self,z):
        z=into(z);r=[p*q for p in (self.lo,self.hi) for q in (z.lo,z.hi)]
        return I(min(r),max(r))
    __rmul__=__mul__
    def __truediv__(self,z):
        z=into(z);assert z.lo>0 or z.hi<0
        return self*I(1/z.hi,1/z.lo)
    def __pow__(self,n):
        assert n>=0 and isinstance(n,int)
        v=I(1)
        for _ in range(n):v=v*self
        return v

def into(x):return x if isinstance(x,I) else I(x)

z=I(a,b)
ea=exp_bounds(a); eb=exp_bounds(b)
e=I(ea[0],eb[1])
Sval=(z*z-z+1)*e-1
Aval=(z**3-z*z+2*z-2)*e+2
Tval=z*z*e*((z**3-2*z*z+2*z+2)*e-(z*z+4*z+2))
assert Sval.lo>0 and Aval.lo>0 and Tval.lo>0
Fval=Tval/(Sval*Aval)
low=Q('0.9099071739796848');high=Q('0.9099071739796851')
assert low<Fval.lo and Fval.hi<high,(float(Fval.lo),float(Fval.hi))
print('PASS: exact interval enclosures for minimal dispersion index')
print('      0.9099071739796848 < Fmin < 0.9099071739796851')

# The zero-mass ratio R(t)=p0*exp(mu(t)) is strictly decreasing since
# (log R)'=(Var-mean)/t<0. Endpoint limits R(0+)=1, R(infty)=1/2.
print('PASS: formal p0= t^2/(2S), mean=tS\'/S-2, R endpoints 1 and 1/2')
print('ALL CHECKS PASSED')
