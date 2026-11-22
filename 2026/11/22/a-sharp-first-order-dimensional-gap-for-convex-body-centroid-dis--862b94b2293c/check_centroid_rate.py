"""Exact-rational checks for the centroid-displacement asymptotic constant.

No external packages required. The analytic argument establishing the global
maximum and asymptotic expansion is in RESULT.md; this program checks the
polynomial identities, coefficient signs, and numeric root/coefficient bounds.
"""
from fractions import Fraction as Q
from math import factorial

class I:
    def __init__(self, lo, hi=None):
        self.lo=Q(lo)
        self.hi=Q(lo if hi is None else hi)
        assert self.lo<=self.hi
    def __add__(self, rhs):
        rhs=asI(rhs)
        return I(self.lo+rhs.lo,self.hi+rhs.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,rhs):return self+(-asI(rhs))
    def __rsub__(self,rhs):return asI(rhs)+(-self)
    def __mul__(self,rhs):
        rhs=asI(rhs)
        v=[a*b for a in (self.lo,self.hi) for b in (rhs.lo,rhs.hi)]
        return I(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,rhs):
        rhs=asI(rhs)
        assert rhs.lo>0 or rhs.hi<0,'division interval touches zero'
        return self*I(1/rhs.hi,1/rhs.lo)
    def __rtruediv__(self,rhs):return asI(rhs)/self
    def __pow__(self,k):
        assert k>=0
        out=I(1)
        for _ in range(k):out=out*self
        return out

def asI(x):return x if isinstance(x,I) else I(x)

def exp_bounds(x,N=85):
    # Exact rational lower and upper bounds for exp(x), x>=0.
    assert x>=0 and x<N+2
    term=Q(1)
    lower=term
    for j in range(1,N+1):
        term*=x/j
        lower+=term
    rem=term*x/Q(N+1)
    upper=lower+rem/(1-x/Q(N+2))
    return I(lower,upper)

def deriv_num(s):
    # Sign of d/dq F(q) at q=-s; the denominator is positive.
    e=exp_bounds(s)
    c3=-4-2*s+2*s*s-s**3
    c2=6+6*s-4*s*s
    c1=-4-6*s+2*s*s+s**3+s**4
    return e**4+c3*(e**3)+c2*(e**2)+c1*e+(1+2*s)

def b(k):
    # k! times the kth Taylor coefficient of the numerator above,
    # valid at k>=5.
    a=Q(k**3-9*k*k+26*k+108,27)
    c2= -k*k+4*k+6
    c1= k**4-5*k**3+10*k*k-12*k-4
    return 4**k-3**k*a+2**k*c2+c1

def falling(k,r):
    if k<r:return 0
    z=1
    for j in range(r):z*=k-j
    return z

def coefficient(k):
    # k! [s^k] of the explicit exponential polynomial P(s).
    out=4**k-4*3**k+6*2**k-4
    for power,degree,multiplier in [(-2,1,3),(2,2,3),(-1,3,3),
                                    (6,1,2),(-4,2,2),
                                    (-6,1,1),(2,2,1),(1,3,1),(1,4,1)]:
        if k>=degree:
            out+=power*falling(k,degree)*multiplier**(k-degree)
    if k==0:out+=1
    if k==1:out+=2
    return out

assert all(coefficient(k)==0 for k in range(8))
assert all(coefficient(k)==b(k) for k in range(8,60))

assert [b(k) for k in range(8,14)] == [Q(-factorial(8),144),Q(-7*factorial(9),720),Q(-29*factorial(10),4320),Q(-29*factorial(11),10080),Q(-659*factorial(12),907200),Q(-factorial(13),181440)]
assert b(14)>0
# For all k>=14, the paper proves b_k>0 by induction using
# A(k+1)<=4*A(k)/3, (k+1)^2 <=2*k^2, and 4^14>3^14*A(14)+2^14*14^2.
A=lambda k:Q(k**3-9*k*k+26*k+108,27)
assert 4**14>3**14*A(14)+2**14*14**2
assert Q(14**3-18*14**2+71*14+54,27)>0

lo=Q(2353317385,10**9)
hi=Q(2353317386,10**9)
assert deriv_num(lo).hi<0
assert deriv_num(hi).lo>0

S=I(lo,hi)
E=I(1)/I(exp_bounds(lo).lo,exp_bounds(hi).hi)

def J(k):
    p=I(0)
    for j in range(k+1):p=p+(S**j)*Q(1,factorial(j))
    return I(factorial(k))*(I(1)-E*p)/(S**(k+1))

j=[J(k) for k in range(5)]
D=j[2]/j[1]-j[1]/j[0]
G=-(S**2)/2*(j[4]/j[1]-j[2]*j[3]/(j[1]**2)-j[3]/j[0]+j[1]*j[2]/(j[0]**2))
C=-G
assert D.lo>Q(20160,100000) and D.hi<Q(20163,100000)
assert C.lo>Q(382,10000) and C.hi<Q(385,10000)

print('Unique positive critical point in [2.353317385, 2.353317386].')
print('D interval:', format(float(D.lo),'.13f'),format(float(D.hi),'.13f'))
print('c interval:',format(float(C.lo),'.13f'),format(float(C.hi),'.13f'))
print('All exact-rational assertion checks passed.')
